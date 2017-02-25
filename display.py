import Tkinter
from Tkinter import *
from board import Board
class Display:
	def __init__(self, master=Tk(),board=Board()):
		self.master = master
		self.board = board
		
		master.title("Tetris")
		
		Label(master, text = "Play Tetris!\n\n").pack()
		
		self.buttons = {"down":Button(master,text="down",command=self.downPressed),
			"left":Button(master,text="left",command=self.leftPressed),
			"right":Button(master,text="right",command=self.rightPressed)}
		for key in self.buttons:
			self.buttons[key].pack()
		mainloop()
	def downPressed(self):
		print "The user has pressed down"
	def leftPressed(self):
		print "The user has pressed left"
	def rightPressed(self):
		print "The user has pressed right"