size = 0
color = None

class Point:
    def __init__(self, *args):
        self.setVals(args)
        self.size = size
        self.color = color

    def setVals(self, *args):
        args = args[0]
        if len(args) == 1 and len(args[0]) == 2:
            self.pos = tuple(args[0])
        elif len(args) == 2:
            self.pos = tuple(args)
        else: raise ValueError(len(args) + " arguments is too many for Point.moveTo")
        acceptableTypes = (int, float)
        if type(self.pos[0]) in acceptableTypes and type(self.pos[1]) in acceptableTypes:
            self.x = self.pos[0]
            self.y = self.pos[1]
        else: raise ValueError("Point.moveTo must take in numbers as arguments")

    def moveTo(self, *args):
        self.setVals(args)

    def __str__(self):
        return '(' + str(self.pos[0]) + ', ' + str(self.pos[1]) + ')'

class Line:
    def __init__(self, p1, p2):
        self.points = [p1, p2]
        self.size = size
        self.color = color

    def __str__(self):
        return str(self.points[0]) + ' -> ' + str(self.points[1])

    def movePoint(self, point, pos):
        self.points[point].moveTo(pos)

    def translate(self, translation): #takes the form [dX, dY]
        self.movePoint(0, [self.points[0].x + translation[0], self.points[0].y + translation[1]])
        self.movePoint(1, [self.points[1].x + translation[0], self.points[1].y + translation[1]])

    #def rotate(self, angle): #clockwise, in degrees
    #    center = Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    def connect(self, other, thisPoint, otherPoint):
        self.points[thisPoint] = other.points[otherPoint]
