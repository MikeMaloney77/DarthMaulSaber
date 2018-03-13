from LightSaberHandle import *

class DisplayCase(object):
    def __init__(self, win, length = 900, widthHeight = 10):
        self.length = length
        self.widthHeight = widthHeight
        self.buildCase(win, 50, 360)
        self.buildCase(win, 50, 510)
        self.buildCase(win, 50, 210)
        self.rect(win, 260, 370)
        self.rect(win, 710, 370)
        self.rect(win, 710, 220)
        self.rect(win, 710, 520)
        self.rect(win, 260, 220)
        self.rect(win, 260, 520)

    def buildCase(self, win, x1, y1):
        """Builds display case"""
        shelfFront = Rectangle(Point(x1, y1), Point(x1 + self.length, y1 + self.widthHeight))
        shelfFront.setFill(color_rgb(66, 134, 244))
        shelfFront.draw(win)
        shelfTop = Polygon(Point(x1, y1), Point(x1 + 25, y1 - 10), Point(x1 + self.length - 25, y1 - self.widthHeight), Point(x1 + self.length, y1))
        shelfTop.setFill("white")
        shelfTop.draw(win)

    def rect(self, win, x, y, height= 25, width = 30):
        """This builds the rectangle that holds up the shelf"""
        rect1 = Rectangle(Point(x, y), Point(x + width, y + height))
        rect1.setFill(color_rgb(66, 134, 244))
        rect1.draw(win)
