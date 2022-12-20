import pytest
from randomQueue import RandomQueue

def test_insert():
    ex2 = RandomQueue()
    ex2.insert(0)
    ex2.insert(1)
    ex2.insert(2)

    for i in range(0, 3):
        assert ex2.items[i] == i

def test_remove():
    ex2 = RandomQueue()
    ex2.insert(2)

    assert ex2.remove() == 2

def test_is_empty():
    ex1 = RandomQueue()
    assert ex1.is_empty() is True

    ex2 = RandomQueue()
    ex2.insert(2)
    assert ex2.is_empty() is False

def test_is_full():
    ex1 = RandomQueue()

    for i in range(0, ex1.mSize):
        ex1.insert(i)

    assert ex1.is_full() is True

    ex2 = RandomQueue()
    assert ex2.is_full() is False

def test_clear():
    ex1 = RandomQueue()
    for i in range(0, 7):
        ex1.insert(i)
    ex1.clear()
    ex1.is_empty() is True


if __name__ == '__main__':
     pytest.main()     # uruchamia wszystkie testy
