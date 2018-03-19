from Blade import *

class Handle(Blade):
    def __init__(self, x, win, y = 310, color2 = "gray"):
        super(Handle, self).__init__(x, y)
        self.color2 = color2
        #self.drawHandle(win)
        #self.drawLine(win)



    def drawHandle(self, win):
        """Draws the lightsaber handle"""
        hand = Rectangle(Point(self.x + 298, self.y), Point(self.x + 502, self.y + 30))
        hand.setFill(self.color2)
        hand.draw(win)
        self.drawLine(win)


    def drawLine(self, win, newX = 432):
        """Draws lines on the handle"""
        for line in range(6):
            line = Line(Point(newX, self.y), Point(newX, self.y + self.height))
            line.setWidth(2)
            line.draw(win)
            newX += 34


    def drawButton(self, win, x, y, addedX = 34):
        """Draws buttons on the lightsaber"""
        for button in range(4):
            button = Circle(Point(x + addedX, y), 6)
            button.setFill("white")
            button.draw(win)
            addedX += 34
            time.sleep(.2)
            button.setFill(self.color)
            button.setActiveFill("white")


