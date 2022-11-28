import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        ret = f'({self.x}, {self.y})'
        return ret

    def __repr__(self):        # zwraca string "Point(x, y)"
        ret = f'Point({self.x}, {self.y})'
        return ret

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):  # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Point(3, 5)), '(3, 5)')
        self.assertEqual(str(Point(4, 82)), '(4, 82)')
        self.assertEqual(str(Point(-2, -68)), '(-2, -68)')

    def test_repr(self):
        self.assertEqual(repr(Point(3, 5)), 'Point(3, 5)')
        self.assertEqual(repr(Point(4, 82)), 'Point(4, 82)')
        self.assertEqual(repr(Point(-2, -68)), 'Point(-2, -68)')

    def test_eq(self):
        self.assertEqual(Point(3, 5), Point(3, 5))
        self.assertEqual(Point(4, 82), Point(4, 82))
        self.assertEqual(Point(15, -5), Point(15, -5))

    def test_neq(self):
        self.assertNotEqual(Point(3, 5), Point(4, 7))
        self.assertNotEqual(Point(4, 82), Point(7, 12))
        self.assertNotEqual(Point(15, -5), Point(-1, -2))

    def test_add(self):
        self.assertEqual(Point(3, 5) + Point(4, 7), Point(7, 12))
        self.assertEqual(Point(2, 14) + Point(4, 82), Point(6, 96))

    def test_sub(self):
        self.assertEqual(Point(3, 5) - Point(4, 7), Point(-1, -2))
        self.assertEqual(Point(2, 14) - Point(4, 82), Point(-2, -68))
        self.assertEqual(Point(15, 5) - Point(10, 2), Point(5, 3))

    def test_sub(self):
        self.assertEqual(Point(3, 5) - Point(4, 7), Point(-1, -2))
        self.assertEqual(Point(2, 14) - Point(4, 82), Point(-2, -68))
        self.assertEqual(Point(15, 5) - Point(10, 2), Point(5, 3))

    def test_mul(self):
        self.assertEqual(Point(3, 5) * Point(4, 7), 47)
        self.assertEqual(Point(2, 14) * Point(4, 82), 1156)
        self.assertEqual(Point(15, -5) * Point(10, 2), 140)

    def test_cross(self):
        self.assertEqual(Point(3, 5).cross(Point(4, 7)), 1)
        self.assertEqual(Point(2, 14).cross(Point(4, 82)), 108)
        self.assertEqual(Point(15, -5).cross(Point(10, 2)), 80)

    def test_length(self):
        self.assertEqual(Point(-2, 0).length(), 2)
        self.assertEqual(Point(15, 0).length(), 15)
        self.assertEqual(Point(0, 3).length(), 3)

    def test_hash(self):
        self.assertEqual(hash(Point(3, 5)), hash((3, 5)))
        self.assertEqual(hash(Point(4, 82)), hash((4, 82)))
        self.assertEqual(hash(Point(-2, -68)), hash((-2, -68)))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
