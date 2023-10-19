from renderer import Renderer
from point import Point
from edge import Edge
from triangle import Triangle
from delaunayTriangulation import DelaunayTriangulation

import random
from random import randint
import pygame
import numpy as np

random.seed(15)
N = 100
DT = DelaunayTriangulation()

for i in range(N):
	point = Point(randint(50, 950), randint(50, 650), randint(0, 50))

	DT.AddPoint(point)

DT.Triangulate()

renderer = Renderer()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()

			point = Point(pos[0], pos[1], randint(30, 50))
			print("Point Added")
			print(point)
			DT.AddPoint(point)
			DT.Triangulate()
			renderer.Clear()

	renderer.Render(DT.mesh)
