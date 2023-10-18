from utils import *

class Edge:
	def __init__(self, point1, point2):
		self.points = []
		self.points.append(point1)
		self.points.append(point2)

		self.point_distance = GetDistance(point1, point2)

	def AddPoint(self, point):
		if len(self.points) < 2:
			self.points.append(point)
		else:
			print("Edge already has 2 points, can't add more.")

	def __str__(self):
		out_str = "\nEdge - "

		for point in self.points:
			out_str += str(point)

		return out_str

	def __eq__(self, other):
		return (self.points[0] == other.points[0] and self.points[1] == other.points[1]) or (self.points[0] == other.points[1] and self.points[1] == other.points[0])