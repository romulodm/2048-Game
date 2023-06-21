from graphics import *
import consts as C

def staticVisual():
    GAME_VISUAL = []

    squaresWindow = Rectangle(Point(0, 145), Point(425, 570))
    squaresWindow.setFill(C.CELL_BORDER_COLOR)
    squaresWindow.setWidth(0)
    GAME_VISUAL.append(squaresWindow)

    gameName = Text(Point(55, 72.5), "2048")
    gameName.setStyle("bold")
    gameName.setFill(C.GAME_MAIN_COLOR)
    gameName.setSize(25)
    GAME_VISUAL.append(gameName)

    squareScore = Rectangle(Point(160, 10), Point(370, 60))
    squareScore.setWidth(2)
    squareScore.setOutline(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(squareScore)

    squareHigh = Rectangle(Point(160, 70), Point(370, 120))
    squareHigh.setWidth(2)
    squareHigh.setOutline(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(squareHigh)

    scoreWord = Text(Point(265, 20), "SCORE")
    scoreWord.setStyle("bold")
    scoreWord.setFill(C.GAME_MAIN_COLOR)
    scoreWord.setSize(11)
    GAME_VISUAL.append(scoreWord)

    highWord = Text(Point(265, 80), "HIGH SCORE")
    highWord.setStyle("bold")
    highWord.setFill(C.GAME_MAIN_COLOR)
    highWord.setSize(11)
    GAME_VISUAL.append(highWord)


    return GAME_VISUAL