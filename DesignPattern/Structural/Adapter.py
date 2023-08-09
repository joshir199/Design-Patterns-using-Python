"""
How does class be used that does not have interface that the client requires?
how can classes that have incompatible interface work together

Thus, We need Adapter class which will link incompatible classes together so that One can use other.

We can add multiple adapter without breaking the code.
"""

from abc import ABC, abstractmethod


class FactoryA(ABC):

    @abstractmethod
    def method_a(self):
        pass


class FactoryB(ABC):

    @abstractmethod
    def method_b(self):
        pass


class ConcreteA(FactoryA):

    def method_a(self):
        print("method A")


class ConcreteB(FactoryB):

    def method_b(self):
        print("method B")


# FactoryA is the service used by class B. So, In order to use Service method by class B, It will create a Adapter
class AdapterB(FactoryA):

    def __init__(self):
        self.clsB = ConcreteB()

    def method_a(self):
        self.clsB.method_b()


if __name__ == "__main__":
    objB = AdapterB()
    objB.clsB.method_b()
    objB.method_a()
