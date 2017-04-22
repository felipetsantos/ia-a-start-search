class Node:	

	def __init__(self, point, cost, heuristic):
		self.point = point
		self.cost = cost
		self.heuristic = heuristic
		self.parent = None

	def getPoint(self):
		return self.point

	def getPriority(self):
		return self.cost + self.heuristic

	def getX(self):
		return self.point.x

	def getY(self):
		return self.point.y

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent

	def getKey(self):
		return "%s,%s"%(self.point.x,self.point.y)

	def getCost(self):
		return self.cost

	def setCost(self, cost):
		self.cost = cost

	def setHeuristic(self, heuristic):
		self.heuristic = heuristic
	
	def getHeuristic(self):
		return self.heuristic