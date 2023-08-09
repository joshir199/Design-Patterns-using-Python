"""
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes
into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

The Bridge pattern attempts to solve this problem by switching from inheritance to the object composition.
What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes
will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.

It is helpful in bridging 90 degree hierarchies with use of independent Single responsibility classes together
Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.

Generally, Bridge pattern is used to provide run-time Binding of the Implementation.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Communication(ABC):

    def __init__(self, cost): # Bridging Communication with CostLayer. It identifies the type of cost at run-time
        self._cost = cost

    def getCostDetail(self):
        self._cost.method_price() # run-time recognition of this method

    @abstractmethod
    def method_Com(self):
        pass


class Wireless(Communication):

    def method_Com(self):
        print("Wireless Communication")


class Wired(Communication):

    def method_Com(self):
        print("Wired Communication")


class CostLayer(ABC):

    @abstractmethod
    def method_price(self):
        pass


class Cheaper(CostLayer):

    def method_price(self):
        print("Cheaper Device")


class Costlier(CostLayer):

    def method_price(self):
        print("Costlier Device")


if __name__ == "__main__":

    cheapWireless = Wireless(Cheaper())
    costlierWired = Wired(Costlier())
    cheapWireless.method_Com()
    cheapWireless.getCostDetail()

    costlierWired.method_Com()
    costlierWired.getCostDetail()
