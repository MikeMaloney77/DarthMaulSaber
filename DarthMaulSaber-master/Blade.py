from graphics import *
import time

class Blade(object):
    """creates a blade for the lightsaber"""

    def __init__(self, x, win, y = 310, color = "red", width = 300, height = 30):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.blade = None
        self.blade2 = None
        self.drawBlade(win)
        #self.drawEndCap(win)

    def drawBlade(self, win):
        """This will draw the blade and add the animation to change color"""
        blade = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        blade2 = Rectangle(Point(self.x + 500, self.y), Point(self.x + 500 + self.width, self.y + self.height))
        blade.setFill(self.color)
        blade.setOutline("white")
        #blade.setActiveFill("blue")
        blade.draw(win)
        blade2.setFill(self.color)
        blade2.setOutline("white")
        #blade2.setActiveFill("blue")

        blade2.draw(win)





    # def drawEndCap(self, win):
    #      """Creates the ends of the lightsaber"""
    #
    #     endCap1 = Arc(Point(self.x + 500 + self.width, self.y), Point(self.x + 500, self.y + 60), 0, 90, "CHORD")
    #
    #     endCap1.draw(win)







