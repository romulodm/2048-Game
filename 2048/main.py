from Game import *
from graphics import *
import visual as vis
import consts as CONS

##############################################
#                                            #
#                                            #
#                GAME INTERFACE              #
#                                            #
#                                            # 
##############################################


def main():
    win = GraphWin("2048",425,570,autoflush=False)
    win.setBackground(CONS.BACKGROUND_COLOR_GAME)

    gameName = Text(Point(55, 72.5), "2048")
    gameName.setStyle("bold")
    gameName.setFill(CONS.GAME_MAIN_COLOR)
    gameName.setSize(25)
    gameName.draw(win)

    squareScore = Rectangle(Point(160, 40), Point(370, 100))
    squareScore.setWidth(2)
    squareScore.setOutline(CONS.GAME_MAIN_COLOR)
    squareScore.draw(win)

    scoreWord = Text(Point(265, 50), "SCORE")
    scoreWord.setStyle("bold")
    scoreWord.setFill(CONS.GAME_MAIN_COLOR)
    scoreWord.setSize(12)
    scoreWord.draw(win)

    currentScore = Text(Point(265, 80), "2048")
    currentScore.setStyle("bold")
    currentScore.setFill(CONS.GAME_MAIN_COLOR)
    currentScore.setSize(20)
    currentScore.draw(win)

    squareWindow = Rectangle(Point(0, 145), Point(425, 570))
    squareWindow.setFill(CONS.CELL_BORDER_COLOR)
    squareWindow.setWidth(0)
    squareWindow.draw(win)

    squares = vis.squares()
    for item in squares:
        item.draw(win)

    piece = Rectangle(Point(7, 257), Point(103, 353))
    piece.setFill(CONS.CELL_COLOR_DICT[2])
    piece.setWidth(0)
    piece.draw(win)

    while True:
        moveKey = win.getKey()

        if moveKey == "Right" or moveKey == "D" or moveKey == "d":
            piece.move(105,0)
        
        if moveKey == "Up" or moveKey == "W" or moveKey == "w":
            piece.move(0,-105)

        if moveKey == "Down" or moveKey == "S" or moveKey == "s":
            piece.move(0,105)

        if moveKey == "Left" or moveKey == "A" or moveKey == "a":
            piece.move(-105,0)


if __name__ == "__main__":
    main()
