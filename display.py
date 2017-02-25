import Tkinter
from Tkinter import *
from board import Board
class Display:
	def __init__(self, master=Tk(),board=Board()):
		self.master = master
		self.board = board
		
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
			
		mainloop()
	def downPressed(self):
		print "The user has pressed down"
	def leftPressed(self):
		print "The user has pressed left"
	def rightPressed(self):
		print "The user has pressed right"
	def endTurn(self): #This is called when a piece lands at the bottom
		#This is not yet optimized. It is only for testing.
		for row in range(0,self.board.height):
			if self.gameGrid.rowIsFull(row):
				print "YE A ROW IS FULL"
class GameGrid:
	def __init__(self,father,master=Tk()):
		self.master = master
		self.father = father
		self.boxes = [[Box(self.master) for col in range(self.father.board.width)] for row in range(self.father.board.height)]
		for row in range(0,self.father.board.height):
			for col in range(0,self.father.board.width):
				self.boxes[row][col].grid(row,col)
	def printGrid(self):
		print(str(self))
	def getBoolGrid(self):
		boolGrid = [[False for col in range(self.father.board.width)] for row in range(self.father.board.height)]
		for row in range(0,self.father.board.height):
			for col in range(0,self.father.board.width):
				boolGrid[row][col] = self.boxes[row][col].get()
		return boolGrid
	def __str__(self):
		boolGrid = self.getBoolGrid()
		s=""
		for row in range(0,self.father.board.height):
			for col in range(0,self.father.board.width):
				s+=str(self.boxes[row][col])
			s+="\n"
		return s
	def rowIsFull(self,row):
		boolGrid = self.getBoolGrid()
		for col in range(0,self.father.board.width):
			if not boolGrid[row][col]: return False
		return True
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