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

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(str(Rectangle(30, 50, 200, 200)), "[(30, 50), (200, 200)]")
        self.assertEqual(str(Rectangle(0, 20, 100, 150)), "[(0, 20), (100, 150)]")
        self.assertEqual(str(Rectangle(70, 40, 300, 100)), "[(70, 40), (300, 100)]")

    def test__repr__(self):
        self.assertEqual(repr(Rectangle(50, 50, 200, 200)), "Rectangle(50, 50, 200, 200)")
        self.assertEqual(repr(Rectangle(0, 20, 100, 150)), "Rectangle(0, 20, 100, 150)")
        self.assertEqual(repr(Rectangle(70, 70, 85, 80)), "Rectangle(70, 70, 85, 80)")

    def test__eq__(self):
        self.assertEqual(Rectangle(50, 50, 200, 200), Rectangle(50, 50, 200, 200))
        self.assertEqual(Rectangle(0, 20, 100, 150), Rectangle(0, 20, 100, 150))
        self.assertEqual(Rectangle(70, 40, 300, 210), Rectangle(70, 40, 300, 210))

    def test__ne__(self):
        self.assertNotEqual(Rectangle(50, 50, 200, 200), Rectangle(0, 20, 100, 150))
        self.assertNotEqual(Rectangle(0, 20, 100, 150), Rectangle(70, 40, 300, 210))
        self.assertNotEqual(Rectangle(70, 40, 300, 210), Rectangle(50, 50, 200, 200))

    def test_center(self):
        self.assertEqual(Rectangle(50, 50, 200, 200).center(), Point(125, 125))
        self.assertEqual(Rectangle(0, 20, 100, 150).center(), Point(50, 85))
        self.assertEqual(Rectangle(70, 40, 300, 210).center(), Point(185, 125))

    def test_area(self):
        self.assertEqual(Rectangle(50, 50, 200, 200).area(), 22500)
        self.assertEqual(Rectangle(0, 20, 100, 150).area(), 13000)
        self.assertEqual(Rectangle(70, 40, 300, 210).area(), 39100)

    def test_move(self):
        self.assertEqual(Rectangle(50, 50, 200, 200).move(100, 100), Rectangle(150, 150, 300, 300))
        self.assertEqual(Rectangle(0, 20, 100, 150).move(12, -5), Rectangle(12, 15, 112, 145))
        self.assertEqual(Rectangle(70, 40, 300, 210).move(30, -100), Rectangle(100, -60, 330, 110))

    def test_intersection(self):
        self.assertEqual(Rectangle(1, 1, 5, 5).intersection(Rectangle(2, 2, 7, 7)), Rectangle(2, 2, 5, 5))
        self.assertEqual(Rectangle(10, 10, 100, 100).intersection(Rectangle(0, 50, 300, 350)), Rectangle(10, 50, 100, 100))
        self.assertEqual(Rectangle(70, 40, 300, 210).intersection(Rectangle(0, 20, 100, 150)), Rectangle(70, 40, 100, 150))

    def test_cover(self):
        self.assertEqual(Rectangle(1, 1, 5, 5).cover(Rectangle(2, 2, 7, 7)), Rectangle(1, 1, 7, 7))
        self.assertEqual(Rectangle(10, 10, 100, 100).cover(Rectangle(0, 50, 300, 350)), Rectangle(0, 10, 300, 350))
        self.assertEqual(Rectangle(70, 40, 300, 210).cover(Rectangle(0, 20, 100, 150)), Rectangle(0, 20, 300, 210))

    def test_make4(self):
        self.assertEqual((Rectangle(0, 0, 200, 200).make4()), (Rectangle(0, 0, 100, 100), Rectangle(100, 0, 200, 100), Rectangle(0, 100, 100, 200), Rectangle(100, 100, 200, 200)))
        self.assertEqual((Rectangle(0, 20, 100, 150).make4()), (Rectangle(0, 20, 50, 85), Rectangle(50, 20, 100, 85), Rectangle(0, 85, 50, 150), Rectangle(50, 85, 100, 150)))
        self.assertEqual((Rectangle(70, 70, 170, 170).make4()), (Rectangle(70, 70, 120, 120), Rectangle(120, 70, 170, 120), Rectangle(70, 120, 120, 170), Rectangle(120, 120, 170, 170)))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy