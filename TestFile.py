from DisplayCase import *
from graphics import *

def main():
    """Runs the main code"""

    DisplayCase(win)

    win.getMouse()
    win.close()

win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

main()


