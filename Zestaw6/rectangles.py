import copy

from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):     # "[(x1, y1), (x2, y2)]"
        ret = f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'
        return ret

    def __repr__(self):     #"Rectangle(x1, y1, x2, y2)"
        ret = f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'
        return ret

    def __eq__(self, other):    # obsługa rect1 == rect2
        return (self.pt1.x == other.pt1.x) and (self.pt1.y == other.pt1.y) and (self.pt2.x == other.pt2.x) and (self.pt2.y == other.pt2.y)

    def __ne__(self, other):    # obsługa rect1 != rect2
        return not self == other

    def center(self):   # zwraca środek prostokąta
        w = self.pt2.x - self.pt1.x
        h = self.pt2.y - self.pt1.y
        x = self.pt1.x + w / 2.0
        y = self.pt1.y + h / 2.0
        return Point(x, y)

    def area(self):     # pole powierzchni
        w = self.pt2.x - self.pt1.x
        h = self.pt2.y - self.pt1.y
        ar = w * h
        return ar

    def move(self, x, y):   # przesunięcie o (x, y)
        movedRec = copy.deepcopy(self)
        movedRec.pt1.x += x
        movedRec.pt1.y += y
        movedRec.pt2.x += x
        movedRec.pt2.y += y
        return movedRec

import unittest

class TestRectangle(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(str(Rectangle(50, 50, 200, 200)), "[(50, 50), (200, 200)]")
        self.assertEqual(str(Rectangle(0, 20, 100, 150)), "[(0, 20), (100, 150)]")
        self.assertEqual(str(Rectangle(70, 40, 300, 210)), "[(70, 40), (300, 210)]")

    def test__repr__(self):
        self.assertEqual(repr(Rectangle(50, 50, 200, 200)), "Rectangle(50, 50, 200, 200)")
        self.assertEqual(repr(Rectangle(0, 20, 100, 150)), "Rectangle(0, 20, 100, 150)")
        self.assertEqual(repr(Rectangle(70, 40, 300, 210)), "Rectangle(70, 40, 300, 210)")

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


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy