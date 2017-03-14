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
class AgentState:
	def __init__(self,boolGrid,tetroBoxList):
		#boolGrid is without the starting tetro
		self.boolGrid = boolGrid
		self.tetroBoxList = tetroBoxList
		
class Agent(Input):
	def __init__(self, parent):
		self.parent = parent
		self.grid = parent.gameGrid.getBoolGrid()
		self.state = None
	def newTurn(self):
		self.grid = parent.gameGrid.getBoolGrid()
		self.state = AgentState(self.grid,self.parent.fallingTetro.getStartBoxPointList)
	def getActions(self):
		#Call when a new tetro is added
		#This should return a list of actions (directions) to get the tetro to a good place
		startState = self.getStartState()
		endState = self.getEndState(startState)
		return getPath(startState,endState)
	#def getCost(self):
	#	print "nope"
		#Do we need this? Does Tetris really have a "cost" for the movement of tetros?
	#def getHeuristic(self):
	def getBoolListWithoutTetro(self):
		tempGridList = [[boolSpot[0],boolSpot[1]] for boolSpot in boolGrid]
		tetroList = self.parent.fallingTetro.getStartBoxPointList
		for tetroSpot in tetroList:
			tempGridList[tetroSpot] = False
		return tempGridList
	def getStartState(self):
		tetroList = self.parent.fallingTetro.getStartBoxPointList
		startState = AgentState(self.getBoolListWithoutTetro,tetroList)
		return startState
	def getEndState(self,startState):
		possibleStates = getEachEndPlacement(self,startState)
		possibleStateVals = [self.evaluateEndState(endState) for endState in possibleStates]
		bestIndex = possibleStateVals.index(min(possibleStateVals))
		bestStateTemp = possibleStates[bestIndex]
		endState = AgentState(self.getBoolListWithoutTetro(),bestStateTemp)
		return endState
		#return possibleStates[bestIndex]
		#Could we try doing this for each of the rotations of the piece,
		#then get the best from each, then choose the best of the four rotations?
		
	def evaluateEndState(self, endState):
		numRowsFilled = len([row for row in range(self.father.board.width) if self.parent.gameGrid.rowIsFull(row)])
		return numRowsFilled
	def getEachEndPlacement(self,startState):
		tetro = self.parent.fallingTetro
		startBoxPlaces = tetro.getStartBoxPointList
		startBoxCols = [startBoxPlace[0] for startBoxPlace in startBoxPlaces]
		leftMostBox = min(startBoxCols)
		rightMostBox = max(startBoxCols)
		boxesWidth = 1+rightMostBox-leftMostBox
		possibleEndBoxesPlacements = []
		leftMostBoxPlacements = [[startBoxPlace[0]-leftMostBox,startBoxPlace[1]] for startBoxPlace in startBoxPlaces]
		#possibleEndBoxPlacements.append(leftMostBoxPlaces)
		for rightPush in range(0,self.parent.board.width-boxesWidth):
			possibleEndBoxesPlacement = [leftMostBoxPlacements[0]+rightPush,leftMostBoxPlacements[1]]
			possibleEndBoxesPlacements.append(possibleEndBoxesPlacement)
		botBoxesList = [[possibleEndBoxesPlacement[0],possibleEndBoxesPlacement[1]+self.parent.depth-1] for possibleEndBoxesPlacement in possibleEndBoxesPlacements]
		endPlacements = []
		for botBoxes in botBoxesList:
			while True:
				if True in [self.parent.gameGrid.get(botBox) for botBox in botBoxes]:
					botBoxes = [[boxBox[0],botBox[1]+1] for botBox in botBoxes]
					continue
				else:
					endPlacements.append(botBoxes)
					break
		return endPlacements
class Search:
	def getPath(startState,endState):
		