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
		self.fallingBlocks = [] #This will hold the four blocks of the current tetro
		
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
			
		#print "Adding an L tetro"
		L = Tetro("L",self.board)
		self.addTetro(L)
		#print "Finished adding L tetro"
		mainloop()
	def downPressed(self):
		print "The user has pressed down"
		#Check to see if there's anything below
		oldBoxes = self.fallingBlocks
		deepest = max([oldBox.row for oldBox in oldBoxes])
		print "Deepest: ",deepest
		if deepest == self.board.depth-1:
			self.endTurn()
			return
		newBoxes = [self.getBoxDown(oldBox) for oldBox in oldBoxes]
		if self.directionBlocked(oldBoxes,newBoxes): #This will end the turn
			self.endTurn()
			return #We dont' want to update the boxes below if the turn ends
		for oldBox in oldBoxes: oldBox.activate()
		for newBox in newBoxes: newBox.activate()
		self.fallingBlocks = newBoxes
	def leftPressed(self):
		print "The user has pressed left"
		#Check to see if there's anything to the left
		oldBoxes = self.fallingBlocks
		newBoxes = [self.getBoxLeft(oldBox) for oldBox in oldBoxes]
		if self.directionBlocked(oldBoxes,newBoxes):
			print "That direction is blocked."
			return
		for oldBox in oldBoxes: oldBox.activate()
		for newBox in newBoxes: newBox.activate()
		self.fallingBlocks = newBoxes
	def rightPressed(self):
		print "The user has pressed right"
		#Check to see if there's anything to the right
		oldBoxes = self.fallingBlocks
		newBoxes = [self.getBoxRight(oldBox) for oldBox in oldBoxes]
		if self.directionBlocked(oldBoxes,newBoxes):
			print "That direction is blocked."
			return
		for oldBox in oldBoxes: oldBox.activate()
		for newBox in newBoxes: newBox.activate()
		self.fallingBlocks = newBoxes
	def directionBlocked(self,oldBoxes,newBoxes):
		for newBox in newBoxes:
			if newBox not in oldBoxes:
				if newBox.get():
					return True
		return False
	def endTurn(self): #This is called when a piece lands at the bottom
		#This is not yet optimized. It is only for testing.
		print "1:"
		print self.gameGrid
		for row in range(1,self.board.depth):
			if self.gameGrid.rowIsFull(row):
				#add points
				print "You've cleared a row!"
				for row2 in range(row,0,-1):
					for col in range(0,self.board.width):
						toBeReplaced = self.gameGrid.boxes[row2][col]
						toReplace = self.gameGrid.boxes[row2-1][col]
						if not (toBeReplaced.get() == toReplace.get()):
							toBeReplaced.activate()
				self.gameGrid.emptyRow(0) #Clearing the top row
				#print "YE A ROW IS FULL"
		print "2:"
		print self.gameGrid
		self.addTetro(Tetro("L",self.board))#Make it so the type of tetro is random
		print "3:"
		print self.gameGrid
	#def hasBlock(self,dimensions): return self.getBox(dimensions).get()
	def addTetro(self, tetro):
		self.fallingTetro = tetro
		self.fallingBlocks = []
		for startingPos in tetro.spaces:
			currentBox = self.getBox(startingPos)
			if currentBox.get():#If there's already something there
				print "A tetro should have been added, but there was a box already checked."
			currentBox.activate()
			self.fallingBlocks.append(currentBox)
		self.fallingTetro = tetro
	def getBox(self, dimensions): 
		return self.gameGrid.getBox(dimensions)
	def getBoxDown(self, oldBox):
		direction = Direction.D
		dimensions = [oldBox.col,oldBox.row]
		return self.gameGrid.getBox([dimensions[0]+Direction.colMod[direction],dimensions[1]+Direction.rowMod[direction]])
	def getBoxLeft(self, oldBox):
		direction = Direction.L
		dimensions = [oldBox.col,oldBox.row]
		return self.gameGrid.getBox([dimensions[0]+Direction.colMod[direction],dimensions[1]+Direction.rowMod[direction]])
	def getBoxRight(self, oldBox):
		direction = Direction.R
		dimensions = [oldBox.col,oldBox.row]
		return self.gameGrid.getBox([dimensions[0]+Direction.colMod[direction],dimensions[1]+Direction.rowMod[direction]])
			
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
	def emptyRow(self, row):
		for col in range(0,self.father.board.width):
			if self.boxes[row][col].get():
				self.boxes[row][col].activate()
class Box:
	def __init__(self,master):
		self.intVar = IntVar()
		self.isChecked = False #This is stupid, but I've tried for HOURS getting the other way to work and it won't. LIterally hours. 2/25/17 from 8am to 3:13pm.
		self.master = master
		self.checkBox = Checkbutton(self.master,variable=self.intVar,command=self.hitBox)
		self.checkBox.var = self.intVar
		self.row = -1
		self.col = -1
	def get(self):
		return self.isChecked
	def grid(self,row,col):
		self.checkBox.grid(row=row,column=col)
		self.row = row
		self.col = col
	def hitBox(self):
		#print "You hit a box. Good for you."
		self.isChecked = not self.isChecked
	def __str__(self):
		return "#" if self.get() else "0"
	def activate(self): self.checkBox.invoke()
class Direction:
	#def __init__(self,rowModifier,colModifier,letterRep):
	#	self.rowModifier = rowModifier
	#	self.colModifier = colModifier
	#	self.letterRep = letterRep
	D = "Down"#Direction(1,0,"D")#Down
	L = "Left"#Direction(0,-1,"L")#Left
	R = "Right"#Direction(0,1,"R")#Right
	rowMod = {D:1,L:0,R:0}
	colMod = {D:0,L:-1,R:1}
	