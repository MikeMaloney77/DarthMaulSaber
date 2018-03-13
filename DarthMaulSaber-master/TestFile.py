from LightSaberHandle import *
from DisplayCase import *
from Blade import *
from graphics import *


def main():
    """Runs the main code"""

    handle1 = Handle(100, win)
    handle2 = Handle(100, win, 160)
    handle3 = Handle(100, win, 460)
    case = DisplayCase(win)

    while checkMouse == None:

        Blade.blade.color.setFill("blue")
        Blade.blade2.color.setFill("blue")


    win.getMouse()
    win.close()

win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

main()
