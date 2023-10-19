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
WIDTH = 1000
HEIGHT = 700
DT = DelaunayTriangulation()
renderer = Renderer(width = WIDTH, height = HEIGHT, show_mesh = True)

for i in range(N):
	point = Point(randint(50, WIDTH - 50), randint(50, HEIGHT - 50), randint(0, 50))

	DT.AddPoint(point)

DT.Triangulate()


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
