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
        self.logo(win)
        self.explanation(win)
        self.darthMaul(win)
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

    def logo(self, win):
        """This imports the starwars logo"""
        sW = Image(Point(1250, 585), "StarWarsLogo.png")
        sW.draw(win)
        for i in range(75):
            sW.move(-10,0)
            time.sleep(.032)
        # for i in range(100):
            # sW.draw(win)
            # time.sleep(.01)
            # sW.undraw()
            # time.sleep(.01)

    def explanation(self, win):
        """Shows instructions"""
        ex = Text(Point(-250,80), "HOVER THE MOUSE OVER THE BLADES AND BUTTONS")
        ex.setFill("red")
        ex.setFace("helvetica")
        ex.setStyle("bold italic")
        ex.setSize(18)
        ex.draw(win)
        for i in range(75):
            ex.move(10,0)
            time.sleep(.032)

    def darthMaul(self, win):
        """This will place an image of darth maul in the code"""

        dM = Image(Point(150, 585), "DarthMaul.png")
        dM.draw(win)
        for i in range(65):
            dM.move(10,0)
            time.sleep(.012)
