from renderer import Renderer
from point import Point
from edge import Edge
from triangle import Triangle
from delaunayTriangulation import DelaunayTriangulation

import random
from random import randint
import pygame

random.seed(15)
N = 500
DT = DelaunayTriangulation()

for i in range(N):
	point = Point(randint(50, 750), randint(50, 550), 1)
	DT.AddPoint(point)

DT.Triangulate()

renderer = Renderer()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	renderer.Render(DT.mesh)
