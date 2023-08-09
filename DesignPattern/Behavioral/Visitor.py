"""
Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

Use the Visitor when you need to perform an operation on all elements of a complex object structure
(for example, an object tree).

The Visitor pattern lets you execute an operation over a set of objects with different classes by having a
visitor object implement several variants of the same operation, which correspond to all target classes.

"""

from __future__ import annotations
from abc import ABC, abstractmethod


class ComponentI(ABC):
    """
        The Component interface declares an `accept` method that should take the
        base visitor interface as an argument.
        """
    @abstractmethod
    def accept(self, visitor:Visitor):
        pass


class ComponentA(ComponentI):
    """
        Each Concrete Component must implement the `accept` method in such a way
        that it calls the visitor's method corresponding to the component's class.
        """
    def accept(self, visitor:Visitor):
        visitor.doWorkA()


class ComponentB(ComponentI):

    def accept(self, visitor:Visitor):
        visitor.doWorkB()


class Visitor(object):
    """
        The Visitor method declares a set of visiting methods that correspond to
        component classes. The signature of a visiting method allows the visitor to
        identify the exact class of the component that it's dealing with.
        """
    def doWorkA(self):
        print("Work A done")

#The Visitor pattern lets you execute an operation over a set of objects with different classes by having a
    # visitor object implement several variants of the same operation, which correspond to all target classes.
    def doWorkB(self):
        print("Work B done")


if __name__ == "__main__":

    visitor = Visitor()
    cmp1 = ComponentA()
    cmp2 = ComponentB()
    cmp1.accept(visitor)
    cmp2.accept(visitor)
