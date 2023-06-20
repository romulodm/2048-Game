import random
from graphics import *
import consts as C

##############################################
#                                            #
#                                            #
#             LOGIC - 2048 GAME              #
#                                            #
#                                            #
############################################## 

class Game:
    def __init__(self, win):
        self.score = 0
        self.board = [[None,None,None,None],
                      [None,2,None,None],
                      [None,None,None,None],
                      [None,None,65536,2]]
        
        self.win = win

        self.drawScore()
        self.gameLoop()


    def updateScore(self, points):
        self.score += points

        self.currentScore.undraw()
        self.drawScore()

    def drawScore(self):
        self.currentScore = Text(Point(265, 80), self.score)
        self.currentScore.setStyle("bold")
        self.currentScore.setFill(C.GAME_MAIN_COLOR)
        self.currentScore.setSize(20)
        self.currentScore.draw(self.win)

    def generateNewPiece(self):
        done = False
        while not done:
            rowIndex = random.randint(0,3)
            columnIndex = random.randint(0,3)
            
            if self.board[rowIndex, columnIndex] == None:
                self.board[rowIndex, columnIndex] = 2
                done = True
                
    def checkBoard(self):
        for row in self.board:
            for column in row:
                if column == None:
                    return True
    
        for row in self.board:
            for column in row:
                try:            
                    if self.board[row][column] == self.board[row + 1][column] or self.board[row][column] == self.board[row][column + 1]:
                            return True
                except IndexError:
                    continue
            
        return False
                         
    def movePieces(self, movement):
        if movement == "L":
            for row in self.board:
                for column in row:
                    if column - 1 == None:
                        self.board[column - 1] = column 

    def drawPieces(self):
        for row in range(0, 4):
            for column in range(0, 4):
                if self.board[row][column] != None:
                    num = self.board[row][column]
                    self.drawPiece(row,column,num)

                

    def drawPiece(self,row,column,num):
        VALOR_X = 7 + (column * 105)
        VALOR_Y = 152 + (row * 105)

        piece = Rectangle(Point(VALOR_X, VALOR_Y), Point(VALOR_X + 96, VALOR_Y + 96))
        piece.setFill(C.CELL_COLOR_DICT[num])
        piece.setWidth(0)
        piece.draw(self.win)
    
    def gameLoop(self):

        done = False
        while not done:

            moveKey = self.win.getKey()

            self.drawPieces()

            if moveKey == "Right" or moveKey == "D" or moveKey == "d":
                pass

            if moveKey == "Up" or moveKey == "W" or moveKey == "w":
                pass

            if moveKey == "Down" or moveKey == "S" or moveKey == "s":
                pass

            if moveKey == "Left" or moveKey == "A" or moveKey == "a":
                pass

    