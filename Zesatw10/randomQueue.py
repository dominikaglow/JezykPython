import random

class RandomQueue:

    def __init__(self, mSize=15):
        self.items = [None] * mSize
        self.mSize = mSize
        self.size = 0

    def insert(self, item):    # wstawia element w czasie O(1)
        if self.size == self.mSize:
            raise ValueError('Cannot insert new element. The queue is full.')

        self.items[self.size] = item
        self.size += 1

    def remove(self):    # zwraca losowy element w czasie O(1)
        if self.size == 0:
            raise ValueError('Cannot romove element. The queue is empty.')

        num = self.size - 1 #index of last element in queue
        ind = random.randint(0, num)
        elem = self.items[ind]

        if ind == (self.size - 1):
            self.items[ind] = None
        else:
            replaceWith = self.items[num]
            self.items[ind] = replaceWith
            self.items[num] = None
        self.size -= 1

        return elem

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.mSize:
            return True
        else:
            return False

    def clear(self):    # czyszczenie listy
        self.items = [None] * self.mSize
        self.size = 0
