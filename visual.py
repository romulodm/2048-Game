from graphics import *
import consts as C

def staticVisual():
    GAME_VISUAL = []

    squareWindow = Rectangle(Point(0, 145), Point(425, 570))
    squareWindow.setFill(C.CELL_BORDER_COLOR)
    squareWindow.setWidth(0)
    GAME_VISUAL.append(squareWindow)

    #STATIC SQUARES
    GAME_VISUAL.append(Rectangle(Point(5, 150), Point(105, 250)))
    GAME_VISUAL.append(Rectangle(Point(110, 150), Point(210, 250)))
    GAME_VISUAL.append(Rectangle(Point(215, 150), Point(315, 250)))
    GAME_VISUAL.append(Rectangle(Point(320, 150), Point(420, 250)))

    GAME_VISUAL.append(Rectangle(Point(5, 255), Point(105, 355)))
    GAME_VISUAL.append(Rectangle(Point(110, 255), Point(210, 355)))
    GAME_VISUAL.append(Rectangle(Point(215, 255), Point(315, 355)))
    GAME_VISUAL.append(Rectangle(Point(320, 255), Point(420, 355)))

    GAME_VISUAL.append(Rectangle(Point(5, 360), Point(105, 460)))
    GAME_VISUAL.append(Rectangle(Point(110, 360), Point(210, 460)))
    GAME_VISUAL.append(Rectangle(Point(215, 360), Point(315, 460)))
    GAME_VISUAL.append(Rectangle(Point(320, 360), Point(420, 460)))

    GAME_VISUAL.append(Rectangle(Point(5, 465), Point(105, 565)))
    GAME_VISUAL.append(Rectangle(Point(110, 465), Point(210, 565)))
    GAME_VISUAL.append(Rectangle(Point(215, 465), Point(315, 565)))
    GAME_VISUAL.append(Rectangle(Point(320, 465), Point(420, 565)))

    for item in GAME_VISUAL:
        item.setWidth(5)
        item.setOutline(C.CELL_BORDER_COLOR)
        item.setFill(C.BACKGROUND_COLOR_CELL_EMPTY)

    gameName = Text(Point(55, 72.5), "2048")
    gameName.setStyle("bold")
    gameName.setFill(C.GAME_MAIN_COLOR)
    gameName.setSize(25)
    GAME_VISUAL.append(gameName)

    squareScore = Rectangle(Point(160, 40), Point(370, 100))
    squareScore.setWidth(2)
    squareScore.setOutline(C.GAME_MAIN_COLOR)
    GAME_VISUAL.append(squareScore)

    scoreWord = Text(Point(265, 50), "SCORE")
    scoreWord.setStyle("bold")
    scoreWord.setFill(C.GAME_MAIN_COLOR)
    scoreWord.setSize(12)
    GAME_VISUAL.append(scoreWord)


    return GAME_VISUAL