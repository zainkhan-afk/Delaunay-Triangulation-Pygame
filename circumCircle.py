from utils import *
from point import Point

class CircumCircle:
	def __init__(self, triangle):
		p1 = triangle.edges[0].points[0]
		p2 = triangle.edges[1].points[0]
		p3 = triangle.edges[2].points[0]


		side1 = triangle.edges[0].point_distance
		side2 = triangle.edges[1].point_distance
		side3 = triangle.edges[2].point_distance
		
		self.circum_center = self.GetCircumCenter(p1, p2, p3)

		r1 = GetDistance(self.circum_center, p1)
		r2 = GetDistance(self.circum_center, p2)
		r3 = GetDistance(self.circum_center, p3)

		# self.radius = (r1 + r2 + r3)/3

		self.radius = self.GetCircumRadius(side1, side2, side3)

		# print(r1, r2, r3, r, self.radius)

	def GetCircumRadius(self, side1, side2, side3):
		num = side1*side2*side3

		a = ( side1 + side2 + side3)
		b = (-side1 + side2 + side3)
		c = ( side1 - side2 + side3)
		d = ( side1 + side2 - side3)
		den = np.sqrt(abs(a*b*c*d))

		return num / den

	def GetCircumCenter(self, p1, p2, p3):
		a1, b1, c1 = self.GetLineEquationFromPoints(p1, p2)
		a2, b2, c2 = self.GetLineEquationFromPoints(p2, p3)

		a1, b1, c1 = self.GetPerpendicularBisectorLineEquation(p1, p2, a1, b1, c1)
		a2, b2, c2 = self.GetPerpendicularBisectorLineEquation(p2, p3, a2, b2, c2)

		circum_center = self.GetLinesIntersection(a1, b1, c1, a2, b2, c2)


		return circum_center


	def GetLineEquationFromPoints(self, p1, p2):
		a = p2.y - p1.y
		b = p1.x - p2.x
		c = a * p1.x + b * p1.y
		return a, b, c

	def GetPerpendicularBisectorLineEquation(self, p1, p2, a, b, c):
		mid_point = (p1 + p2)/2
	 
		c = -b*mid_point.x + a*mid_point.y
		temp = a
		a = -b
		b = temp
		return a, b, c


	def GetLinesIntersection(self, a1, b1, c1, a2, b2, c2):
		determinant = a1 * b2 - a2 * b1
		if (determinant == 0):
			return None
		else:
			x = (b2 * c1 - b1 * c2)//determinant
			y = (a1 * c2 - a2 * c1)//determinant
			return Point(x, y, 1)

	def IsPointInside(self, point):
		dist = GetDistance(point, self.circum_center)
		return dist < self.radius

	def __repr__(self):
		return f"Circum Circle - Center: {self.circum_center}, Radius: {self.radius}"

	def __str__(self):
		return self.__repr__()