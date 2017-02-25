class Board:
	def __init__(self,height=20,width=10):
		self.height = height
		self.width = width
class Tetro:#"Tetronimo" is the name of the combination of four blocks
	def __init__(self, type):
		self.type = type #Type can be J,L,O,T,S,Z,I