class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return f"\nPoint - X: {self.x}, Y: {self.y}, Z: {self.z} "

	def __str__(self):
		return self.__repr__()

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y, self.z + other.z)

	def __truediv__ (self, value):
		return Point(self.x/value, self.y/value, self.z/value)