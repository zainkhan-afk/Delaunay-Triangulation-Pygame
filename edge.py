class Edge:
	def __init__(self, point1, point2):
		self.points = []
		self.points.append(point1)
		self.points.append(point2)

	def AddPoint(self, point):
		if len(self.points) < 2:
			self.points.append(point)
		else:
			print("Edge already has 2 points, can't add more.")

	def __str__(self):
		out_str = "Edge - "

		for point in self.points:
			out_str += str(point)

		return out_str