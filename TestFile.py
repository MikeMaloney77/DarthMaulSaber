from DisplayCase import *
from graphics import *


def main():
    """Runs the main code"""

    DisplayCase(win)
    handle1 = Handle(100, win, 160)
    handle1.drawBlade(win)
    time.sleep(.25)
    handle1.drawButton(win, 415, 175)
    handle1.changeBladeColor(win)
    handle2 = Handle(100, win)
    handle2.drawBlade(win)
    handle2.drawButton(win, 415, 325)
    handle2.changeBladeColor(win)
    handle3 = Handle(100, win, 460)
    handle3.drawBlade(win)
    handle3.drawButton(win, 415, 475)
    handle3.changeBladeColor(win)


    win.getMouse()
    win.close()

win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")

main()
