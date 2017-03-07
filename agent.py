#So, this will be just an addition method of input, I think. Also, maybe this can hold both the agents AND the keyboard input.
import display
#from display import Direction
import Tkinter
from Tkinter import *
from board import *
class Input:
	def __init__(self, parent):
		self.parent = parent
	#def moveDown():
	#	parent.directionPressed(Direction.D)
	#def moveLeft():
	#	parent.directionPressed(Direction.L)
	#def moveRight():
	#	parent.directionPressed(Direction.R)
#class Agent(Input):
#	print "hi"
class KeyboardInput(Input):
	def __init__(self, parent):
		self.parent = parent
		self.master = Tk()
		self.master.title("Tetris")
		self.master.geometry("300x300")
		Label(self.master, text = "Play Tetris!\n\n").pack()
		Label(self.master,text="Click here for keyboard input").pack()
		self.master.bind("<Key>",self.pressedKey)
	def pressedKey(self,key):
		self.parent.pressedKey(key)
		#keyChar = key.char
		#if keyChar in Direction.keyCharToDirection:
		#	self.directionPressed(Direction.keyCharToDirection[keyChar])