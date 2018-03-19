from DisplayCase import *
from graphics import *

def main():
    """Runs the main code"""

    d = DisplayCase(win)
    d.drawDisplayCase(win)

    win.getMouse()
    win.close()

win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

main()



