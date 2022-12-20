import pytest
from queue import Queue

def test_is_empty():
    ex1 = Queue()
    assert ex1.is_empty() is True

    ex2 = Queue()
    ex2.put(2)
    assert ex2.is_empty() is False

def test_is_full():
    ex1 = Queue()
    for i in range(0, 5):
        ex1.put(i)
    assert ex1.is_full() is True

    ex2 = Queue()
    assert ex2.is_full() is False


def test_put():
    ex2 = Queue()
    ex2.put(0)
    ex2.put(1)
    ex2.put(2)

    for i in range(0, 3):
        assert ex2.items[i] == i

def test_get():
    ex1 = Queue()
    ex1.put(0)
    ex1.put(1)
    ex1.put(2)
    ex1.put(3)

    for i in range(0, 4):
        assert ex1.get() == i

if __name__ == '__main__':
     pytest.main()     # uruchamia wszystkie testy
