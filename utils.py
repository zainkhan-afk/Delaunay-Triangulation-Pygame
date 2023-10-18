import numpy as np

def GetDistance(p1, p2):
	return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)