"""
Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its
 underlying representation (list, stack, tree, etc.).
 Use the Iterator pattern when your collection has a complex data structure under the hood, but you want to
  hide its complexity from clients (either for convenience or security reasons).
  Use the Iterator when you want your code to be able to traverse different data structures or
  when types of these structures are unknown beforehand.
"""

from abc import ABC, abstractmethod


class IteratorInterface(ABC):

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class NumericIterator(IteratorInterface):

    def __init__(self, start, max):
        self._start = start
        self._max = max
        self._idx = 0

    def next(self):
        if self.has_next():
            self._idx += 1
            return self._start + self._idx - 1
        else:
            raise Exception("Index Out of bound")

    def has_next(self):
        return self._idx <= (self._max - self._start)


if __name__ == "__main__":

    obj = NumericIterator(5, 9)
    for i in range(10):
        try:
            print(obj.next())
        except Exception as e:
            print(e)

    obj2 = NumericIterator(5, 9)
    for i in range(10):
        if obj2.has_next():
            print(obj2.next())


