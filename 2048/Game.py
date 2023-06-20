import random

##############################################
#                                            #
#                                            #
#             LOGIC - 2048 GAME              #
#                                            #
#                                            # 
##############################################

class Game:
    def __init__(self, player):
        self.score = 0
        self.board = [[None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None]]

    def updateScore(self, points):
        self.score += points

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
    
    def gameLoop(self):
        playerMovement = ""

        done = False
        while not done:
        
            self.movePieces(playerMovement)

    