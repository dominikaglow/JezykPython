from points import Point
import copy

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2:
            raise ValueError("Invalid value(x1 >= x2)")
        if y1 >= y2:
            raise ValueError("Invalid value (y1 >= y2)")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        ret = f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'
        return ret

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        ret = f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'
        return ret

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1.x == other.pt1.x) and (self.pt1.y == other.pt1.y) and (self.pt2.x == other.pt2.x) and (
                    self.pt2.y == other.pt2.y)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self):          # zwraca środek prostokąta
        w = self.pt2.x - self.pt1.x
        h = self.pt2.y - self.pt1.y
        x = self.pt1.x + w / 2.0
        y = self.pt1.y + h / 2.0
        return Point(x, y)

    def area(self):            # pole powierzchni
        w = self.pt2.x - self.pt1.x
        h = self.pt2.y - self.pt1.y
        ar = w * h
        return ar

    def move(self, x, y):      # przesunięcie o (x, y)
        movedRec = copy.deepcopy(self)
        movedRec.pt1.x += x
        movedRec.pt1.y += y
        movedRec.pt2.x += x
        movedRec.pt2.y += y
        return movedRec

    def intersection(self, other): # część wspólna prostokątów
        #nie przecinaja sie gdy jest spelniony jeden z warunkow:
        #1) jeden z nich jest ponad y2 drugiego
        #2) jeden z nich jest po lewej od lewej strony drugiego

        x2 = min(self.pt2.x, other.pt2.x)
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)

        if x1 >= x2 or y1 >= y2:
            raise ValueError("No intersection")

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):    # prostąkąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Given object is not a rectangle")

        minx1 = min(self.pt1.x, other.pt1.x)
        maxx2 = max(self.pt2.x, other.pt2.x)
        miny1 = min(self.pt1.y, other.pt1.y)
        maxy2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(minx1, miny1, maxx2, maxy2)

    def make4(self):           # zwraca krotkę czterech mniejszych
        x1 = self.pt1.x
        x2 = self.pt2.x
        xMiddle = x1 + ((x2 - x1) / 2)

        y1 = self.pt1.y
        y2 = self.pt2.y
        yMiddle = y1 + ((y2 - y1) / 2)

        rec1 = Rectangle(x1, y1, xMiddle, yMiddle)
        rec2 = Rectangle(xMiddle, y1, x2, yMiddle)
        rec3 = Rectangle(x1, yMiddle, xMiddle, y2)
        rec4 = Rectangle(xMiddle, yMiddle, x2, y2)
        tup = (rec1, rec2, rec3, rec4)

        return tup

# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

    @classmethod
    def from_points(cls, recPoints):
        point1 = recPoints[0]
        point2 = recPoints[1]

        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y

        rect = cls(x1, y1, x2, y2)

        return rect


    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        w = self.pt2.x - self.pt1.x
        return w

    @property
    def height(self):
        h = self.pt2.y - self.pt1.y
        return h

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)