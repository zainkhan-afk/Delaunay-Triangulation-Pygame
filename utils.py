import numpy as np

def GetDistance(p1, p2 = None):
	if p2 is None:
		return np.sqrt((p1.x - 0)**2 + (p1.y - 0)**2)
	return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def GetSlope(p1, p2):
	m = (p2.y - p1.y) / (p2.x - p1.x)

	return m

# def GetTriangleArea(e1, e2, e3):
# 	s = 1/2 * (e1.point_distance + e2.point_distance + e3.point_distance)

# 	v1 = (s - e1.point_distance)
# 	v2 = (s - e2.point_distance)
# 	v3 = (s - e3.point_distance)

# 	area = np.sqrt(s*v1*v2*v3)

# 	return area
def GetTriangleArea(p1, p2, p3):
	# m = np.array([
	# 				[p1.x, p1.y, 1],
	# 				[p2.x, p2.y, 1],
	# 				[p3.x, p3.y, 1],
	# 				])
	# area = np.linalg.det(m)*0.5
	area = 0.5*((p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y))
	return abs(area)