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
		
		triangles = self.RemoveSuperTriangle(triangles, super_triangle)

		self.mesh = triangles


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
			e3 = Edge(point, edge.points[0])

			triangle = Triangle(e1, e2, e3)

			good_triangles.append(triangle)

		return good_triangles

	def GetUniqueEdges(self, edges):
		unique_edges = []

		for i in range(len(edges)):
			edge1 = edges[i]
			is_unique_edge = True
			for j in range(len(edges)):
				edge2 = edges[j]
				if i != j and edge1 == edge2:
					is_unique_edge = False
					break

			if is_unique_edge:
				unique_edges.append(edge1)

		return unique_edges

	def RemoveSuperTriangle(self, triangles, super_triangle):
		mesh_triangles = []

		super_tri_p1 = super_triangle.edges[0].points[0]
		super_tri_p2 = super_triangle.edges[1].points[0]
		super_tri_p3 = super_triangle.edges[2].points[0]
		
		for triangle in triangles:
			p1 = triangle.edges[0].points[0]
			p2 = triangle.edges[1].points[0]
			p3 = triangle.edges[2].points[0]

			if not (p1 == super_tri_p1 or p1 == super_tri_p2 or p1 == super_tri_p3 or
					p2 == super_tri_p1 or p2 == super_tri_p2 or p2 == super_tri_p3 or
					p3 == super_tri_p1 or p3 == super_tri_p2 or p3 == super_tri_p3):
				mesh_triangles.append(triangle)



		return mesh_triangles


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


		dx = (x_max - x_min)*10
		dy = (y_max - y_min)*10

		p1 = Point(x = x_min - dx    , y = y_min - dy * 3, z = 1)
		p2 = Point(x = x_min - dx    , y = y_max + dy    , z = 1)
		p3 = Point(x = x_max + dx * 3, y = y_max + dy    , z = 1)

		e1 = Edge(p1, p2)
		e2 = Edge(p2, p3)
		e3 = Edge(p3, p1)

		return Triangle(e1, e2, e3)