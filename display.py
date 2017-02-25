import Tkinter
from Tkinter import *
from board import Board
class Display:
	def __init__(self, master=Tk(),board=Board()):
		self.master = master
		self.board = board
		
		self.master.title("Tetris")
		
		Label(master, text = "Play Tetris!\n\n").pack()
		
		self.gameGrid = Tk()
		
		self.buttons = {"down":Button(master,text="down",command=self.downPressed),
			"left":Button(master,text="left",command=self.leftPressed),
			"right":Button(master,text="right",command=self.rightPressed),
			"endTurn":Button(master,text="endTurn",command=self.endTurn),
			"printGrid":Button(master,text="printGrid",command=self.printGrid)}
		for key in self.buttons:
			self.buttons[key].pack()
		#I'm making the boxes checkbuttons to help with debugging
		self.checkVars = [[None for col in range(self.board.width)] for row in range(self.board.height)]#I think checkbuttons needs this
		self.checks = [[None for col in range(self.board.width)] for row in range(self.board.height)]
		for row in range(0,self.board.height):
			for col in range(0,self.board.width):
				self.checkVars[row][col] = IntVar()
				self.checks[row][col] = Checkbutton(self.gameGrid,variable=self.checkVars[row][col])
				#self.checks[row][col].var = self.checkVars[row][col]
				self.checks[row][col].grid(row=row,column=col)
			
		mainloop()
	def switchVar(self,row,col):
		print "switching."
		print " before: ",self.checkVars[row][col].get()
		self.checkVars[row][col] = int((not (self.checkVars[row][col].get())))
		print " after: ",self.checkVars[row][col]
	def downPressed(self):
		print "The user has pressed down"
	def leftPressed(self):
		print "The user has pressed left"
	def rightPressed(self):
		print "The user has pressed right"
	def endTurn(self): #This is called when a piece lands at the bottom
		#This is not yet optimized. It is only for testing.
		for row in range(0,self.board.height):
			if self.checkFullRow(row):
				print "YE A ROW IS FULL"
	def checkFullRow(self,row):
		#rowChecks = []
		#for col in range(0,self.board.width):
		#	rowChecks.append(self.checks[row][col])
		#rowChecks = [self.checks[row][col] for col in range(0,self.board.width)]
		#rowBools = [check.variable() for check in rowChecks]
		for intVar in self.checkVars[row]:
			intVal = intVar.get()
			if intVal==1:
				return 1
		return 0
		#if 0 in [self.checkVars[row].get()]: return 0
		#else: return 1
		#for val in self.checkVars[row]:
		#	print val.get()
	def printGrid(self):
		for row in range(0,self.board.height):
			#for col in range(0,self.board.width):
				#iv = self.checkVars[row][col]
				#print iv.get()
				#check = self.checks[row,col]
				#check.toggle()
			#print [intVar.get() for intVar in self.checkVars[row]]
			print [che.get() for che in self.checkVars[row]]
		print "\n\n"