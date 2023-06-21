import random
import time
from graphics import *
from visual import game_over_screen
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

        self.lastMove = None

        self.cells = []
        self.nums = []

        self.gameOverScreen = game_over_screen()

        self.generateCells()
        self.generateNums()
        self.getHighestScore()
        self.drawScore()

        self.gameLoop()

    def generateEmptyBoard(self):
        return [[None]*4 for i in range(4)]
    
    def resetLastMove(self):
        self.lastMove = None
        return True

    def updateScore(self, points):
        self.score += points
        if self.score > self.highestScore:
            self.highestScore = self.score
            self.updateHighestScore()
            self.saveScore()
        self.currentScore.undraw()
        self.drawScore()

    def drawScore(self):
        self.currentScore = Text(Point(320, 105), self.score)
        self.currentScore.setStyle("bold")
        self.currentScore.setFill(C.GAME_MAIN_COLOR)
        self.currentScore.setSize(17)
        self.currentScore.draw(self.win)

    def resetScore(self):
        self.score = 0

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
        if self.score >= int(self.highestScore):
            file = open("2048/highest.txt", "w")
            file.write(str(self.score))
            file.close()
            return True
        return False
    
    def drawHighestScore(self):
        self.recordScore = Text(Point(320, 45), self.highestScore)
        self.recordScore.setStyle("bold")
        self.recordScore.setFill(C.GAME_MAIN_COLOR)
        self.recordScore.setSize(17)
        self.recordScore.draw(self.win)

    def updateHighestScore(self):
        self.recordScore.undraw()
        self.recordScore = Text(Point(320, 45), self.highestScore)
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
    
    def checkCellQuantity(self):
        n = 0
        for row in range(0, 4):
            for column in range(0, 4):
                if self.board[row][column] != None:
                    n += 1
        return n
    
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
            self.nums[row][column].undraw()
            self.nums[row][column] = Text(self.cells[row][column].getCenter(), num)
            self.nums[row][column].setStyle("bold")
            self.nums[row][column].setFill(C.NUM_COLOR_DICT[num])
            self.nums[row][column].setSize(22)
            self.nums[row][column].draw(self.win)  
          
    def moveUp(self, move):
        if self.lastMove == "Up" or self.lastMove == "W" or self.lastMove == "w":
            quantity = self.checkCellQuantity()
            if quantity == 1:
                self.resetLastMove()
                return False
            
        self.compressUp()
        #Merge cells:
        for row in range(1, 4):
            for column in range(0, 4):
                if self.board[row][column] == self.board[row - 1][column] and self.board[row][column] != None:
                    self.board[row - 1][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column] = None

        self.compressUp()
        self.generateRandomPiece()

        self.lastMove = move
        return True

    def compressUp(self):
        emptyBoard = self.generateEmptyBoard()
        for column in range(0, 4):
            count = 0
            for row in range(0, 4):
                if self.board[row][column] != None:
                    emptyBoard[count][column] = self.board[row][column]
                    count += 1
        
        self.board = emptyBoard
        return True

    def moveLeft(self, move):
        if self.lastMove == "Left" or self.lastMove == "A" or self.lastMove == "a":
            quantity = self.checkCellQuantity()
            if quantity == 1:
                self.resetLastMove()
                return False
            
        self.compressLeft()
        #Merge cells:
        for row in range(0, 4):
            for column in range(1, 4):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != None:
                    self.board[row][column - 1] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column] = None

        self.compressLeft()
        self.generateRandomPiece()

        self.lastMove = move
        return True

    def compressLeft(self):
        emptyBoard = self.generateEmptyBoard()
        for row in range(0, 4):
            count = 0
            for column in range(0, 4):
                if self.board[row][column] != None:
                    emptyBoard[row][count] = self.board[row][column]
                    count += 1
        
        self.board = emptyBoard
        return True

    def moveDown(self, move):
        if self.lastMove == "Down" or self.lastMove == "S" or self.lastMove == "s":
            quantity = self.checkCellQuantity()
            if quantity == 1:
                self.resetLastMove()
                return False

        self.compressDown()
        #Merge cells:
        for row in range(3, 0, -1):
            for column in range(0, 4):
                if self.board[row][column] == self.board[row - 1][column] and self.board[row][column] != None:
                    self.board[row][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row - 1][column] = None
        
        self.compressDown()
        self.generateRandomPiece()

        self.lastMove = move
        return True

    def compressDown(self):
        emptyBoard = self.generateEmptyBoard()
        for column in range(0, 4):
            count = 3
            for row in range(3, -1, -1):
                if self.board[row][column] != None:
                    emptyBoard[count][column] = self.board[row][column]
                    self.cells[count][column].move(0,105)
                    update(20)
                    count -= 1

        self.board = emptyBoard
        return True
        
    def moveRight(self, move):
        if self.lastMove == "Right" or self.lastMove == "D" or self.lastMove == "d":
            quantity = self.checkCellQuantity()
            if quantity == 1:
                self.resetLastMove()
                return False
            
        self.compressRight()
        #Merge cells:
        for row in range(0, 4):
            for column in range(3, 0, -1):
                if self.board[row][column] == self.board[row][column - 1] and self.board[row][column] != None:
                    self.board[row][column] = self.board[row][column] * 2
                    self.updateScore(self.board[row][column] * 2)
                    self.board[row][column - 1] = None    
        
        self.compressRight()
        self.generateRandomPiece()

        self.lastMove = move
        return True

    def compressRight(self): 
        emptyBoard = self.generateEmptyBoard()
        for row in range(0, 4):
            count = 3
            for column in range(3, -1, -1):
                if self.board[row][column] != None:
                    emptyBoard[row][count] = self.board[row][column]
                    count -= 1

        self.board = emptyBoard
        return True

    def resetGame(self):
        for row in range(0, 4):
            for column in range(0, 4):
                self.cells[row][column].undraw()

        for row in range(0, 4):
            for column in range(0, 4):
                self.nums[row][column].undraw()

        self.saveScore()
        self.resetScore()
        self.updateScore(0)
        self.board = self.generateEmptyBoard()
        self.drawPieces()

        return self.gameLoop()

    def gameOver(self):
        for item in self.gameOverScreen:
            item.draw(self.win)

        done = False
        while not done:
            click = self.win.checkMouse()
            if click:
                if click.getX() >= 50 and click.getX() <= 170 and click.getY() >= 75 and click.getY() <= 115:
                    for item in self.gameOverScreen:
                        item.undraw()
                    done = True
        return True 

    def gameLoop(self):
        self.generateRandomPiece()
        
        self.done = False
        while not self.done:
            if not self.checkBoard():
                if self.gameOver():
                    self.done = True
                    return self.resetGame()
                
            click = self.win.checkMouse()
            if click and click.getX() >= 50 and click.getX() <= 170 and click.getY() >= 75 and click.getY() <= 115:
                self.done = True
                return self.resetGame()

            moveKey = self.win.checkKey()
            if moveKey:
                if moveKey == "Up" or moveKey == "W" or moveKey == "w":
                    self.moveUp(moveKey)
                    moveKey = None
                    time.sleep(0.1)

                if moveKey == "Left" or moveKey == "A" or moveKey == "a":
                    self.moveLeft(moveKey)
                    moveKey = None
                    time.sleep(0.1)

                if moveKey == "Down" or moveKey == "S" or moveKey == "s":
                    self.moveDown(moveKey)   
                    moveKey = None
                    time.sleep(0.1)

                if moveKey == "Right" or moveKey == "D" or moveKey == "d":
                    self.moveRight(moveKey)
                    moveKey = None
                    time.sleep(0.1)