import Tkinter
from Tkinter import *
from board import *
#Note: A "Box" is just a space. A "block" is a box that holds a piece. A "Tetro" is one of the four-blocked pieces in a Tetris game.
#I need to work on the dimensions. I think I"m confusing rows and columns. It can either be [column,row] or [row][column]
#Rows should count down.
class Display:
	def __init__(self, master=Tk(),board=Board()):
		self.master = master
		self.board = board
		
		self.fallingTetro = None
		self.fallingSpaces = [] #This will hold the four blocks of the current tetro
		
		self.master.title("Tetris")
		self.master.geometry("300x300")
		Label(master, text = "Play Tetris!\n\n").pack()
		
		self.gameGrid = GameGrid(self)
		
		self.buttons = {"down":Button(master,text="down",command=self.downPressed),
			"left":Button(master,text="left",command=self.leftPressed),
			"right":Button(master,text="right",command=self.rightPressed),
			"endTurn":Button(master,text="endTurn",command=self.endTurn),
			"printGrid":Button(master,text="printGrid",command=self.gameGrid.printGrid)}
		for key in self.buttons:
			self.buttons[key].pack()
			
		print "Adding an L tetro"
		L = Tetro("L",self.board)
		self.addTetro(L)
		print "Finished adding L tetro"
		mainloop()
	def downPressed(self):
		print "The user has pressed down"
		#Check to see if there's anything below
		for space in self.fallingSpaces:
			oldBox = self.getBox(space)
			newBox = self.getBox(
	def leftPressed(self):
		print "The user has pressed left"
	def rightPressed(self):
		print "The user has pressed right"
	def endTurn(self): #This is called when a piece lands at the bottom
		#This is not yet optimized. It is only for testing.
		for row in range(0,self.board.depth):
			if self.gameGrid.rowIsFull(row):
				print "YE A ROW IS FULL"
	#def hasBlock(self,dimensions): return self.getBox(dimensions).get()
	def addTetro(self, tetro):
		for startingPos in tetro.spaces:
			currentBox = self.getBox(startingPos)
			if currentBox.get():#If there's already something there
				print "A tetro should have been added, but there was a box already checked."
			currentBox.activate()
			self.fallingSpaces.append(startingPos)
		self.fallingTetro = tetro
	def getBox(self, dimensions): 
		return self.gameGrid.getBox(dimensions)
	#def getBoxBelow(self, dimensions):
	#	return self.gameGrid.getBox([dimensions[0],dimensions[1]
			
class GameGrid:
	def __init__(self,father,master=Tk()):
		self.master = master
		self.father = father
		self.boxes = [[Box(self.master) for col in range(self.father.board.width)] for row in range(self.father.board.depth)]
		for row in range(0,self.father.board.depth):
			for col in range(0,self.father.board.width):
				self.boxes[row][col].grid(row,col)
	def printGrid(self):
		print(str(self))
	def getBoolGrid(self):
		boolGrid = [[False for col in range(self.father.board.width)] for row in range(self.father.board.depth)]
		for row in range(0,self.father.board.depth):
			for col in range(0,self.father.board.width):
				boolGrid[row][col] = self.boxes[row][col].get()
		return boolGrid
	def __str__(self):
		boolGrid = self.getBoolGrid()
		s=""
		for row in range(0,self.father.board.depth):
			for col in range(0,self.father.board.width):
				s+=str(self.boxes[row][col])
			s+="\n"
		return s
	def rowIsFull(self,row):
		boolGrid = self.getBoolGrid()
		for col in range(0,self.father.board.width):
			if not boolGrid[row][col]: return False
		return True
	def getBox(self, dimensions):
		return self.boxes[dimensions[1]][dimensions[0]]
class Box:
	def __init__(self,master):
		self.intVar = IntVar()
		self.isChecked = False #This is stupid, but I've tried for HOURS getting the other way to work and it won't. LIterally hours. 2/25/17 from 8am to 3:13pm.
		self.master = master
		self.checkBox = Checkbutton(self.master,variable=self.intVar,command=self.hitBox)
		self.checkBox.var = self.intVar
	def get(self):
		return self.isChecked
	def grid(self,row,col):
		self.checkBox.grid(row=row,column=col)
	def hitBox(self):
		#print "You hit a box. Good for you."
		self.isChecked = not self.isChecked
	def __str__(self):
		return "#" if self.get() else "0"
	def activate(self): self.checkBox.invoke()