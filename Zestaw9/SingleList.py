class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("Given list is empty.")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):   # klasy O(n)
        if self.length == 0:
            raise ValueError('Cannot remove last element. Given list is empty.')
        if self.length == 1:
            temp = self.tail
            self.head = self.tail = None
            return temp
        helper = self.head
        while helper.next != self.tail:
            helper = helper.next
        temp = helper.next
        helper.next = None
        self.tail = helper
        return temp
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.

    def join(self, other):   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        other.clear()

    def clear(self):   # czyszczenie listy
        self.head = self.tail = None
        self.length = 0

    def find_min(self):  # klasy O(n)
        if self.length == 0:
            raise ValueError('Given list is empty.')
        minVal = self.head.data
        minNode = self.head

        helper = self.head
        while helper != None:
            if helper.data < minVal:
                minVal = helper.data
                minNode = helper
            helper = helper.next
        return minNode
    # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def find_max(self): # klasy O(n)
        if self.length == 0:
            raise ValueError('Given list is empty.')
        maxVal = self.head.data
        maxNode = self.head

        helper = self.head
        while helper != None:
            if helper.data > maxVal:
                maxVal = helper.data
                maxNode = helper
            helper = helper.next
        return maxNode
    # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
