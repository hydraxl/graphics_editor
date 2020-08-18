import math
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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.points = [self.p1, self.p2]
        self.size = size
        self.color = color

    def __str__(self):
        return str(self.points[0]) + ' -> ' + str(self.points[1])

    def movePoint(self, point, pos):
        if type(point) == Point:
            if point is self.p1: self.p1.moveTo(pos)
            elif point is self.p2: self.p2.moveTo(pos)
            else: raise ValueError("argument 'point' must refer to an endpoint on the line")
        elif type(point) == int: self.points[point].moveTo(pos)
        else: raise ValueError("argument 'point' must refer to an endpoint on the line")

    def translate(self, translation): #takes the form [dX, dY]
        self.movePoint(0, [self.points[0].x + translation[0], self.points[0].y + translation[1]])
        self.movePoint(1, [self.points[1].x + translation[0], self.points[1].y + translation[1]])

    def rotate(self, rotation, center=None): #counterclockwise, in radians
        def find_angle_dist(point, center):
            distance = ((point.x - center.x) ** 2 + (point.y - center.y) ** 2) ** 0.5
            angle = math.asin(abs(point.y - center.y) / distance)
            if point.y < center.y:
                print(deg(angle))
                angle += math.pi
                print("changing angle for " + str(point) + " to " + str(deg(angle)))
            return angle, distance

        if center is None: center = Point((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)
        if center != self.p1:
            a1, d1 = find_angle_dist(self.p1, center)
            a1 = (a1 + rotation) % (2 * math.pi)
            self.p1.moveTo((d1 * math.cos(a1)) + center.x, (d1 * math.sin(a1)) + center.y)
        if center != self.p2:
            a2, d2 = find_angle_dist(self.p2, center)
            a2 = (a2 + rotation) % (2 * math.pi)
            self.p2.moveTo((d2 * math.cos(a2)) + center.x, (d2 * math.sin(a2)) + center.y)




    def connect(self, other, thisPoint, otherPoint):
        self.points[thisPoint] = other.points[otherPoint]

def rad(deg):
    return (deg / 180) * math.pi

def deg(rad):
    return (rad / math.pi) * 180

test = Line(Point(0, -1), Point(0, 1))
test.rotate(rad(90), Point(5, 5))
print(test)
