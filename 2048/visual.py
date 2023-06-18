from graphics import *
import consts as CONS

def squares():
    SQUARES = []
    SQUARES.append(Rectangle(Point(5, 150), Point(105, 250)))
    SQUARES.append(Rectangle(Point(110, 150), Point(210, 250)))
    SQUARES.append(Rectangle(Point(215, 150), Point(315, 250)))
    SQUARES.append(Rectangle(Point(320, 150), Point(420, 250)))

    SQUARES.append(Rectangle(Point(5, 255), Point(105, 355)))
    SQUARES.append(Rectangle(Point(110, 255), Point(210, 355)))
    SQUARES.append(Rectangle(Point(215, 255), Point(315, 355)))
    SQUARES.append(Rectangle(Point(320, 255), Point(420, 355)))

    SQUARES.append(Rectangle(Point(5, 360), Point(105, 460)))
    SQUARES.append(Rectangle(Point(110, 360), Point(210, 460)))
    SQUARES.append(Rectangle(Point(215, 360), Point(315, 460)))
    SQUARES.append(Rectangle(Point(320, 360), Point(420, 460)))

    SQUARES.append(Rectangle(Point(5, 465), Point(105, 565)))
    SQUARES.append(Rectangle(Point(110, 465), Point(210, 565)))
    SQUARES.append(Rectangle(Point(215, 465), Point(315, 565)))
    SQUARES.append(Rectangle(Point(320, 465), Point(420, 565)))

    for item in SQUARES:
        item.setWidth(5)
        item.setOutline(CONS.CELL_BORDER_COLOR)
        item.setFill(CONS.BACKGROUND_COLOR_CELL_EMPTY)

    return SQUARES