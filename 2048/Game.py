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
                      [None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None]]
        
        self.win = win

        self.done = False

        self.cells = []
        self.nums = []

        self.generateCells()
        self.generateNums()
        self.getHighestScore()
        self.drawScore()
        self.gameLoop()

    def generateEmptyBoard(self):
        return [[None]*4 for i in range(4)]

    def updateScore(self, points):
        self.score += points
        if self.score > self.highestScore:
            self.highestScore = self.score
            self.updateHighestScore()
        self.currentScore.undraw()
        self.drawScore()

    def drawScore(self):
        self.currentScore = Text(Point(265, 45), self.score)
        self.currentScore.setStyle("bold")
        self.currentScore.setFill(C.GAME_MAIN_COLOR)
        self.currentScore.setSize(17)
        self.currentScore.draw(self.win)

    def getHighestScore(self):
        file = open("2048/highest.txt", "r")
        self.highestScore = file.read()
        if len(self.highestScore) == 0:
            self.highestScore = 0
        else:
            self.highestScore = int(self.highestScore)
        file.close()

        self.drawHighestScore()

    def saveScore(self):
        if self.score > int(self.highestScore):
            file = open("2048/highest.txt", "w")
            file.write(str(self.score))
            file.close()
            self.score = 0
            return True
        self.score = 0
        return False
    
    def drawHighestScore(self):
        self.recordScore = Text(Point(265, 105), self.highestScore)
        self.recordScore.setStyle("bold")
        self.recordScore.setFill(C.GAME_MAIN_COLOR)
        self.recordScore.setSize(17)
        self.recordScore.draw(self.win)

    def updateHighestScore(self):
        self.recordScore.undraw()
        self.recordScore = Text(Point(265, 105), self.highestScore)
        self.recordScore.setStyle("bold")
        self.recordScore.setFill(C.GAME_MAIN_COLOR)
        self.recordScore.setSize(17)
        self.recordScore.draw(self.win)

    def generateRandomPiece(self):
        if self.checkEmptyCells():
            while True:
                rowIndex = random.randint(0,3)
                columnIndex = random.randint(0,3)
                
                if self.board[rowIndex][columnIndex] == None:
                    self.board[rowIndex][columnIndex] = 2
                    
                    self.drawPieces()
                    return True
                    
        return False
    
    def checkEmptyCells(self):
        for row in range(0, 4):
            for column in range(0, 4):
                if self.board[row][column] == None:
                    return True   
        return False
    
    def checkBoard(self):
        if self.checkEmptyCells():
            return True
        
        for row in range(0, 4):
            for column in range(0, 3):          
                if self.board[row][column] == self.board[row][column + 1]:
                    return True
                
        for row in range(0, 3):
            for column in range(0, 4):          
                if self.board[row][column] == self.board[row + 1][column]:
                    return True
            
        return False
    
    def generateCells(self):
        for row in range(0, 4):
            row_cells = []
            for column in range(0, 4):
                cell = Rectangle(Point(0, 0), Point(0, 0))
                row_cells.append(cell)
            self.cells.append(row_cells)
            
        self.drawNewCells()

    def drawNewCells(self):
        for row in range(0, 4):
            for column in range(0, 4):
                 self.cells[row][column].draw(self.win)

    def generateNums(self):
        for row in range(0, 4):
            row_nums = []
            for column in range(0, 4):
                num = Text(Point(0,0), "")
                row_nums.append(num)
            self.nums.append(row_nums)

        self.drawNewNums()

    def drawNewNums(self):
        for row in range(0, 4):
            for column in range(0, 4):
                 self.nums[row][column].draw(self.win)

    def drawPieces(self):
        if self.checkBoard:
            for row in range(0, 4):
                for column in range(0, 4):
                    num = self.board[row][column]
                    self.drawPiece(row,column,num)
            return True
        return False
          
    def drawPiece(self,row,column,num):
        X = 7 + (column * 105)
        Y = 152 + (row * 105)
        
        #Square:
        cell = self.cells[row][column]
        cell.undraw()
        cell = Rectangle(Point(X, Y), Point(X + 96, Y + 96))
        cell.setWidth(0)
        if num != None:
            cell.setFill(C.CELL_COLOR_DICT[num])
        else:
            cell.setFill(C.BACKGROUND_COLOR_CELL_EMPTY)
        cell.draw(self.win)
        self.cells[row][column] = cell

        #Num:
        if num != None:
            numCell = self.nums[row][column]
            numCell.undraw()
            numCell = Text(self.cells[row][column].getCenter(), num)
            numCell.setStyle("bold")
            numCell.setFill(C.NUM_COLOR_DICT[num])
            numCell.setSize(22)
            numCell.draw(self.win)  
          
    def moveUp(self):
        self.compressUp()
        #Merge cells:
        for row in range(1, 4):
            for column in range(0, 4):
                if self.board[row][column] == self.board[row - 1][column] and self.board[row][column] != None:
                    self.board[row - 1][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column] = None

        self.compressUp()

    def compressUp(self):
        emptyBoard = self.generateEmptyBoard()
        for column in range(0, 4):
            count = 0
            for row in range(0, 4):
                if self.board[row][column] != None:
                    emptyBoard[count][column] = self.board[row][column]
                    count += 1
        
        self.board = emptyBoard

    def moveLeft(self):
        self.compressLeft()
        #Merge cells:
        for row in range(0, 4):
            for column in range(1, 4):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != None:
                    self.board[row][column - 1] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column] = None

        self.compressLeft()

    def compressLeft(self):
        emptyBoard = self.generateEmptyBoard()
        for row in range(0, 4):
            count = 0
            for column in range(0, 4):
                if self.board[row][column] != None:
                    emptyBoard[row][count] = self.board[row][column]
                    count += 1
        
        self.board = emptyBoard

    def moveDown(self):
        self.compressDown()
        #Merge cells:
        for row in range(3, 0, -1):
            for column in range(0, 4):
                if self.board[row][column] == self.board[row - 1][column] and self.board[row][column] != None:
                    self.board[row][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row - 1][column] = None
        self.compressDown()

    def compressDown(self):
        emptyBoard = self.generateEmptyBoard()
        for column in range(0, 4):
            count = 3
            for row in range(3, -1, -1):
                if self.board[row][column] != None:
                    emptyBoard[count][column] = self.board[row][column]
                    count -= 1

        self.board = emptyBoard
        
    def moveRight(self):
        self.compressRight()
        #Merge cells:
        for row in range(0, 4):
            for column in range(3, 0, -1):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != None:
                    self.board[row][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column - 1] = None    

        self.compressRight() 

    def compressRight(self): 
        emptyBoard = self.generateEmptyBoard()
        for row in range(0, 4):
            count = 3
            for column in range(3, -1, -1):
                if self.board[row][column] != None:
                    emptyBoard[row][count] = self.board[row][column]
                    count -= 1

        self.board = emptyBoard

    def gameOver(self):
        for row in range(0, 4):
            for column in range(0, 4):
                self.cells[row][column].undraw()

        for row in range(0, 4):
            for column in range(0, 4):
                self.nums[row][column].undraw()

        self.saveScore()

        self.done = True
        return

    def gameLoop(self):
        while not self.done:
            self.generateRandomPiece()

            if not self.checkBoard():
                self.gameOver()

            if not self.done:
                moveKey = self.win.getKey()

                if moveKey == "Up" or moveKey == "W" or moveKey == "w":
                    self.moveUp()

                if moveKey == "Left" or moveKey == "A" or moveKey == "a":
                    self.moveLeft()
                    
                if moveKey == "Down" or moveKey == "S" or moveKey == "s":
                    self.moveDown()

                if moveKey == "Right" or moveKey == "D" or moveKey == "d":
                    self.moveRight()
    