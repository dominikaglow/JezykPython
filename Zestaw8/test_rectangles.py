import pytest
from rectangles import Rectangle
from points import Point


def test_from_points():
    assert str(Rectangle.from_points((Point(30, 50), Point(200, 200)))) == '[(30, 50), (200, 200)]'
    assert str(Rectangle.from_points((Point(0, 20), Point(100, 150)))) == '[(0, 20), (100, 150)]'
    assert str(Rectangle.from_points((Point(70, 40), Point(300, 100)))) == '[(70, 40), (300, 100)]'

def test_prop_num():
    rect = Rectangle(30, 50, 200, 200)

    assert rect.top == 200
    assert rect.left == 30
    assert rect.bottom == 50
    assert rect.right == 200
    assert rect.width == 170
    assert rect.height == 150

def test_prop_point():
    rec_p = Rectangle.from_points((Point(0, 20), Point(100, 150)))

    assert rec_p.topleft == Point(0, 150)
    assert rec_p.bottomleft == Point(0, 20)
    assert rec_p.topright == Point(100, 150)
    assert rec_p.bottomright == Point(100, 20)

if __name__ == '__main__':
     pytest.main()     # uruchamia wszystkie testy
