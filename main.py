from renderer import Renderer
from point import Point
from edge import Edge
from triangle import Triangle

from random import randint
import pygame

p1 = Point(randint(50, 600), randint(50, 600), 1)
p2 = Point(randint(50, 600), randint(50, 600), 1)
p3 = Point(randint(50, 600), randint(50, 600), 1)

e1 = Edge(p1, p2)
e2 = Edge(p2, p3)
e3 = Edge(p3, p1)

t1 = Triangle(e1, e2, e3)

print(t1)

mesh = [t1]

renderer = Renderer()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	renderer.Render(mesh)
