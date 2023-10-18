import pygame

class Renderer:
	def __init__(self, width = 1000, height = 700, title = "Delaunay Triangulation"):
		self.width  = width
		self.height = height
		self.title = title

		self.background_color = (0, 0, 0)
		self.edge_color = (0, 255, 0)
		self.point_color = (0, 255, 255)
		self.point_radius = 5

		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.title)

	def Clear(self):
		self.screen.fill(self.background_color)

	def Render(self, mesh):
		for triangle in mesh:
			# pygame.draw.circle(self.screen, (125, 125, 125), (triangle.circum_circle.circum_center.x, triangle.circum_circle.circum_center.y), 2)
			# pygame.draw.circle(self.screen, (125, 125, 125), (triangle.circum_circle.circum_center.x, triangle.circum_circle.circum_center.y), triangle.circum_circle.radius, width = 3)
			for edge in triangle.edges:
				pygame.draw.line(self.screen, self.edge_color, (edge.points[0].x, edge.points[0].y), (edge.points[1].x, edge.points[1].y), 1)
				for point in edge.points:
					pygame.draw.circle(self.screen, self.point_color, (point.x, point.y), self.point_radius)


		pygame.display.flip()

