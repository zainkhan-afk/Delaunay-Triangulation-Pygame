from utils import *

class Edge:
	def __init__(self, point1, point2):
		self.points = []
		self.points.append(point1)
		self.points.append(point2)

		self.point_distance = GetDistance(point1, point2)

	def __str__(self):
		out_str = "\nEdge - "

		for point in self.points:
			out_str += str(point)

		return out_str

	def __eq__(self, other):
		condition1 = self.points[0] == other.points[0] and self.points[1] == other.points[1]
		condition2 = self.points[0] == other.points[1] and self.points[1] == other.points[0]
		
		return  condition1 or condition2 