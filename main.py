from Game import *
from graphics import *
import visual as vis
import consts as C

##############################################
#                                            #
#                                            #
#               GAME INTERFACE               #
#                                            #
#                                            #
############################################## 

def main():
    win = GraphWin("2048",425,570,autoflush=False)
    win.setBackground(C.BACKGROUND_COLOR_GAME)

    staticVisual = vis.staticVisual()
    for item in staticVisual:
        item.draw(win)

    Game(win)
        
if __name__ == "__main__":
    main()
