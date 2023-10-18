class Triangle:
	def __init__(self, edge1, edge2, edge3):
		self.edges = []
		self.edges.append(edge1)
		self.edges.append(edge2)
		self.edges.append(edge3)

	def __str__(self):
		out_str = "Triangle - "

		for edge in self.edges:
			out_str += str(edge)

		return out_str