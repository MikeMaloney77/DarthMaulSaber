from Blade import *

class Handle(Blade):
    def __init__(self, x, win):
        super(Handle, self).__init__(x, win, y = 310, color = "red", width = 298, height = 30)
        self.drawHandle("gray", win)
        self.drawButton(win, 415, 325)
        self.drawLine(win)

    def drawHandle(self, color, win):
        hand = Rectangle(Point(self.x + 298, self.y), Point(self.x + 502, self.y + 30))
        hand.setFill(color)
        hand.draw(win)


    def drawLine(self, win, newX = 432):
        """Draws stripes on the handle"""
        for line in range(6):
            line = Line(Point(newX, self.y), Point(newX, self.y + self.height))
            line.setWidth(2)
            line.draw(win)
            newX += 34


    def drawButton(self, win, x, y, addedX = 34):
        for button in range(4):
            button = Circle(Point(x + addedX, y), 6)
            button.setFill("red")
            button.draw(win)
            addedX += 34

