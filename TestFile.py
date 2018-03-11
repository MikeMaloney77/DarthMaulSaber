from LightSaberHandle import *

def main():
    """Runs the main code"""

    handle = Handle(100, win)


    win.getMouse()
    win.close()

win = GraphWin("Lightsaber", 1000, 650)
win.setBackground("black")


main()