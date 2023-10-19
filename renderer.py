import pygame
import numpy as np
from point import Point
from edge import Edge
from utils import *

class Renderer:
	def __init__(self, width = 1000, height = 700, title = "Delaunay Triangulation", show_circum_circles = False, fill_mesh = True):
		self.width  = width
		self.height = height
		self.title = title
		self.show_circum_circles = show_circum_circles
		self.fill_mesh = fill_mesh

		self.background_color = (0, 0, 0)
		self.edge_color = (100, 200, 50)
		self.point_radius = 5

		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.title)

		self.regenerate_mesh_fill = True

	def Clear(self):
		self.regenerate_mesh_fill = True
		self.screen.fill(self.background_color)

	def GenerteMeshFill(self, mesh):
		# pxarray = pygame.PixelArray(self.screen)
		for triangle in mesh:
			p1 = triangle.edges[0].points[0]
			p2 = triangle.edges[1].points[0]
			p3 = triangle.edges[2].points[0]

			p12 = p2 - p1
			p13 = p3 - p1

			v1 = np.array([p12.x, p12.y, p12.z])
			v2 = np.array([p13.x, p13.y, p13.z])

			eq = np.cross(v1, v2)

			a = eq[0]
			b = eq[1]
			c = eq[2]

			d = a*p1.x + b*p1.y + c*p1.z

			min_x = min(p1.x, p2.x, p3.x)
			max_x = max(p1.x, p2.x, p3.x)

			min_y = min(p1.y, p2.y, p3.y)
			max_y = max(p1.y, p2.y, p3.y)

			min_z = min(p1.z, p2.z, p3.z)
			max_z = max(p1.z, p2.z, p3.z)

			total_area = GetTriangleArea(p1, p2, p3)

			for x in range(min_x, max_x, 5):
				for y in range(min_y, max_y, 5):
					z = (d - a*x - b*y)/c
					p_temp = Point(x, y, z)

					area_1 = GetTriangleArea(p_temp, p1, p2)
					area_2 = GetTriangleArea(p_temp, p1, p3)
					area_3 = GetTriangleArea(p_temp, p2, p3)

					if (area_1 + area_2 + area_3)>total_area:
						continue


					r_color = int(255 * z/50)
					g_color = 0
					b_color = int(255 * (50 - z)/50) 

					if r_color>255:
						r_color = 255

					if r_color<0:
						r_color = 0

					if b_color>0:
						b_color = 255

					if b_color<0:
						b_color = 0
					color = (r_color, g_color, b_color)
					# pxarray[x, y] = color
					pygame.draw.circle(self.screen, color, (x, y), 5)

		self.regenerate_mesh_fill = False

	def Render(self, mesh):
		if self.regenerate_mesh_fill and self.fill_mesh:
			self.GenerteMeshFill(mesh)

		if self.show_circum_circles:
			for triangle in mesh:
				pygame.draw.circle(self.screen, (225, 225, 225), (triangle.circum_circle.circum_center.x, triangle.circum_circle.circum_center.y), 2)
				pygame.draw.circle(self.screen, (50, 50, 50), (triangle.circum_circle.circum_center.x, triangle.circum_circle.circum_center.y), triangle.circum_circle.radius, width = 1)

		for triangle in mesh:
			for edge in triangle.edges:
				pygame.draw.line(self.screen, self.edge_color, (edge.points[0].x, edge.points[0].y), (edge.points[1].x, edge.points[1].y), 3)
				for point in edge.points:
					color = (255 * point.z/50, 0, 255 * (50 - point.z)/50)
					pygame.draw.circle(self.screen, color, (point.x, point.y), self.point_radius)


		pygame.display.flip()

