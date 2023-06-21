from graphics import *
import consts as C

def staticVisual():
    GAME_VISUAL = []

    squaresWindow = Rectangle(Point(0, 145), Point(425, 570))
    squaresWindow.setFill(C.CELL_BORDER_COLOR)
    squaresWindow.setWidth(0)
    GAME_VISUAL.append(squaresWindow)

    gameName = Text(Point(110, 35), "2048")
    gameName.setStyle("bold")
    gameName.setFill(C.GAME_MAIN_COLOR)
    gameName.setSize(25)
    GAME_VISUAL.append(gameName)

    newGameSquare = Rectangle(Point(50, 75), Point(170, 115))
    newGameSquare.setWidth(0)
    newGameSquare.setFill(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(newGameSquare)

    newName = Text(Point(110, 95), "NEW GAME")
    newName.setStyle("bold")
    newName.setFill(C.CELL_COLOR_DICT[2])
    newName.setSize(11)
    GAME_VISUAL.append(newName)

    squareHigh = Rectangle(Point(230, 10), Point(410, 60))
    squareHigh.setWidth(2)
    squareHigh.setOutline(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(squareHigh)

    squareScore = Rectangle(Point(230, 70), Point(410, 120))
    squareScore.setWidth(2)
    squareScore.setOutline(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(squareScore)

    highWord = Text(Point(320, 20), "HIGH SCORE")
    highWord.setStyle("bold")
    highWord.setFill(C.GAME_MAIN_COLOR)
    highWord.setSize(11)
    GAME_VISUAL.append(highWord)

    scoreWord = Text(Point(320, 80), "SCORE")
    scoreWord.setStyle("bold")
    scoreWord.setFill(C.GAME_MAIN_COLOR)
    scoreWord.setSize(11)
    GAME_VISUAL.append(scoreWord)

    return GAME_VISUAL

def game_over_screen():
    GAME_OVER = []

    gameOverWindow = Rectangle(Point(100, 295), Point(325, 420))
    gameOverWindow.setFill("white")
    gameOverWindow.setWidth(3)
    gameOverWindow.setOutline(C.GAME_MAIN_COLOR)
    GAME_OVER.append(gameOverWindow)


    gameOverMessage = Text(Point(212.5, 357.5), 'Game over, press the\n"NEW GAME" button\nto restart game!')
    gameOverMessage.setStyle("bold")
    gameOverMessage.setFill(C.GAME_MAIN_COLOR)
    gameOverMessage.setSize(11)
    GAME_OVER.append(gameOverMessage)

    return GAME_OVER