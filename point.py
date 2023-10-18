class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return f"\nPoint - X: {self.x}, Y: {self.y}, Z: {self.z} "

	def __str__(self):
		return self.__repr__()