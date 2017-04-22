import pickle
from common import *

class MapGenerator:	
	def __init__(self, name, w, h):
		self.w = w
		self.h = h
		self.name = name
		self.start = None
		self.goal = None

	def setStart(self, p):
		self.start = p

	def setGoal(self, p):
		self.goal = p

	def generate(self):
		content = "%s\n%s" % (self.start.x, self.start.y)
		newLine = "\n"
		for l in range(0, self.h):
			content += newLine
			for c in range(0, self.w):
				if self.goal.x == c and self.goal.y == l:
					content += "2"
				else:
					content += "0"

		filePath = os.path.join(PATH, "maps", self.name)
		myfile = open(filePath, "w")
		myfile.write(content)
		myfile.close()


if __name__ == '__main__':
	generator = MapGenerator("hard.txt", 500, 500)
	start = Point(0, 0)
	goal = Point(499, 499)
	generator.setStart(start)
	generator.setGoal(goal)
	generator.generate()

