from circumCircle import CircumCircle
class Triangle:
	def __init__(self, edge1, edge2, edge3):
		self.edges = []
		self.edges.append(edge1)
		self.edges.append(edge2)
		self.edges.append(edge3)

		self.circum_circle = CircumCircle(self)

	def IsInCircumCircle(self, point):
		return self.circum_circle.IsPointInside(point)

	def __repr__(self):
		out_str = "Triangle - "

		for edge in self.edges:
			out_str += str(edge)

		return repr(out_str)

	def __str__(self):
		return self.__repr__()