#This is for testing short bits of code without having to change directories
import Tkinter
from Tkinter import *

class Test:
	def __init__(self):
		self.master=Tk()
		self.checkVar = IntVar()
		self.check = Checkbutton(self.master,variable=self.checkVar)
		self.check.grid(row=0,column=0)
		self.printCheck = Button(self.master,text="PrintIt",command=self.printIt)
		self.printCheck.grid(row=1,column=0)
		mainloop()
	def printIt(self):
		print self.checkVar.get()
t = Test()
print "hi"