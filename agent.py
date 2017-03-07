#So, this will be just an addition method of input, I think. Also, maybe this can hold both the agents AND the keyboard input.
import display
#from display import Direction
import Tkinter
from Tkinter import *
from board import *
class Input:
	def __init__(self, parent):
		self.parent = parent
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
class Agent(Input):
	def __init__(self, parent):
		self.parent = parent
	def getPath(self):
		#Call when a new tetro is added
		#This should return a list of actions (directions) to get the tetro to a good place
	def getCost(self):
		print "nope"
		#Do we need this? Does Tetris really have a "cost" for the movement of tetros?
	def getHeuristic(self):
		