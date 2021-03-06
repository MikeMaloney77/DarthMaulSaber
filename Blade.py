from graphics import *

class Blade(object):
    """creates a blade for the lightsaber"""

    def __init__(self, x, y = 310, color = "red", width = 298, height = 30):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.blade = None
        self.blade2 = None


    def drawBlade(self, win):
        """This will draw the blades"""
        blade = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        blade2 = Rectangle(Point(self.x + 500, self.y), Point(self.x + 500 + self.width, self.y + self.height))

        blade.setFill("white")
        blade.setOutline("white")
        blade.draw(win)

        blade2.setFill("white")
        blade2.setOutline("white")
        blade2.draw(win)
        time.sleep(.1)



    def changeBladeColor(self, win):
        """This will change the color of the blade"""
        blade = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        blade2 = Rectangle(Point(self.x + 500, self.y), Point(self.x + 500 + self.width, self.y + self.height))

        blade.setFill(self.color)
        blade.undraw()

        blade2.setFill(self.color)
        blade2.undraw()
        blade.setActiveFill("blue")
        time.sleep(.1)
        blade2.setActiveFill("blue")
        blade2.draw(win)
        blade.draw(win)
