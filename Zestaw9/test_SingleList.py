import pytest
from SingleList import Node, SingleList

def test_is_empty():
    ex1 = SingleList()
    ex1.insert_head(Node(11))
    ex1.insert_head(Node(22))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))
    assert ex1.is_empty() is False

    ex2 = SingleList()
    assert ex2.is_empty() is True

def test_count():
    ex1 = SingleList()
    ex1.insert_head(Node(11))
    ex1.insert_head(Node(22))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))
    assert ex1.count() == 4

    ex2 = SingleList()
    assert ex2.count() == 0

def test_remove_head():
    ex1 = SingleList()
    ex1.insert_head(Node(15))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))

    assert ex1.remove_head().data == 15

def test_remove_tail():
    ex1 = SingleList()
    ex1.insert_head(Node(15))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))
    ex1.insert_tail(Node(21))

    assert ex1.remove_tail().data == 21

def test_join():
    ex1 = SingleList()
    ex1.insert_head(Node(1))
    ex1.insert_head(Node(0))
    ex1.insert_tail(Node(2))
    ex1.insert_tail(Node(3))

    ex2 = SingleList()
    ex2.insert_head(Node(5))
    ex2.insert_head(Node(4))

    ex1.join(ex2)
    assert ex2.count() == 0

    for i in range(0, 6):
        assert ex1.remove_head().data == i

def test_clear():
    ex1 = SingleList()
    ex1.insert_head(Node(1))
    ex1.insert_head(Node(0))
    ex1.insert_tail(Node(2))
    ex1.insert_tail(Node(3))
    ex1.clear()
    assert ex1.count() == 0
    assert ex1.head == None
    assert ex1.tail == None

def test_find_min():
    ex1 = SingleList()
    ex1.insert_head(Node(11))
    ex1.insert_head(Node(22))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))

    assert ex1.find_min().data == 11

def test_find_max():
    ex1 = SingleList()
    ex1.insert_head(Node(11))
    ex1.insert_head(Node(22))
    ex1.insert_tail(Node(33))
    ex1.insert_tail(Node(50))

    assert ex1.find_max().data == 50

if __name__ == '__main__':
     pytest.main()     # uruchamia wszystkie testy
