"""
Composite is a structural design pattern that lets you compose objects into tree structures and then work
with these structures as if they were individual objects.

when the application have directory like structure for classes and its interactions

A Decorator is like a Composite but only has one child component. There’s another significant difference:
 Decorator adds additional responsibilities to the wrapped object, while Composite just “sums up” its
 children’s results. However, the patterns can also cooperate: you can use Decorator to extend the behavior of a
 specific object in the Composite tree.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def isComposite(self, comp1, comp2):
        return False

    @abstractmethod
    def do_method(self):
        pass


class Composite(Component):

# create a list for storing children of this node
    def __init__(self):
        self.children : List[Component] = []

    def add(self, component):
        if component not in self.children:
            self.children.append(component)
            component.parent = self

    def remove(self, component):
        if component in self.children:
            self.children.remove(component)
            component.parent = None

    def isComposite(self, comp1, comp2):
        return True

    def do_method(self):
        for child in self.children:
            print(child)

# last element in the tree branches. Each node is a leaf until it gets its own children
class Leaf(Component):

    def do_method(self):
        print("Leaf")


if __name__ == "__main__":

    tree = Composite()

    bnch1 = Composite()
    bnch1.add(Leaf())
    bnch1.add(Leaf())

    bnch2 = Composite()
    bnch2.add(Leaf())

    tree.add(bnch1)
    tree.add(bnch2)

    tree.do_method()



