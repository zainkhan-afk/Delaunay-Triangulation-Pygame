from point import Point
from edge import Edge
from triangle import Triangle

class DelaunayTriangulation:
	def __init__(self):
		self.mesh = []
		self.points = []

	def Triangulate(self):
		self.mesh = []
		super_triangle = self.CalculateSuperTriangle()

		triangles = [super_triangle]

		for point in self.points:
			triangles = self.AddPointToMesh(point, triangles)

	def AddPointToMesh(self, point, triangles):
		edges = []
		good_triangles = []

		for triangle in triangles:
			if triangle.IsInCircumCircle(point):
				edges += triangle.edges

			else:
				good_triangles.append(triangle)


		edges = self.GetUniqueEdges(edges)

		for edge in edges:
			e1 = Edge(edge.points[0], edge.points[1])
			e2 = Edge(edge.points[1], point)
			e3 = Edge(point, edge.points[1])

			triangle = Triangle(e1, e2, e2)

			good_triangles.append(triangle)

		return good_triangles

	def GetUniqueEdges(self, edges):
		unique_edges = []

		for edge1 in edges:
			is_unique_edge = True
			for edge2 in edges:

			if edge1 == edge2:
				is_unique_edge = False
				break

			if is_unique_edge:
				unique_edges.append(edge1)

		return unique_edges

	def AddPoint(self, point):
		self.points.append(point)


	def CalculateSuperTriangle(self):
		x_min = 1000
		x_max = 0
		y_min = 1000
		y_max = 0

		for point in self.points:
			if point.x > x_max:
				x_max = point.x
			if point.x < x_min:
				x_min = point.x

			if point.y > y_max:
				y_max = point.y
			if point.y < y_min:
				y_min = point.y


		dx = (x_max - x_max)*10
		dy = (y_max - y_max)*10

		p1 = Point(x = x_min - dx    , y = y_min - dy * 3)
		p2 = Point(x = x_min - dx    , y = y_max + dy)
		p3 = Point(x = x_max + dx * 3, y = y_max + dy)

		e1 = Edge(p1, p2)
		e2 = Edge(p2, p3)
		e3 = Edge(p3, p1)

		return Triangle(e1, e2, e3)