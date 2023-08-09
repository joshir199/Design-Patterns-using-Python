"""
// The abstract factory interface declares a set of methods that
// return different abstract products. These products are called
// a family and are related by a high-level theme or concept.
// Products of one family are usually able to collaborate among
// themselves. A family of products may have several variants,
// but the products of one variant are incompatible with the
// products of another variant.

Note: It has only multiple product type as compared to Factory Method. So, It is more general

"""
from __future__ import annotations
from abc import ABC, abstractmethod

# Abstract class for creating different families of Product Combined with A & B
class FactoryInterface(ABC):

    @abstractmethod
    def create_productA(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_productB(self) -> AbstractProductB:
        pass


class AbstractProductA(ABC):
    """
        Each distinct product of a product family A should have a base interface. All
        variants of the product A must implement this interface.
    """
    @abstractmethod
    def function_first(self):
        pass


class AbstractProductB(ABC):
    """
            Each distinct product of a product family B should have a base interface. All
            variants of the product B must implement this interface.
    """

    @abstractmethod
    def fucntion_firstB(self):
        pass

    @abstractmethod
    def function_collab(self, collaborator: AbstractProductA):
        pass


# first family of products e.g: Italian Product A and B
class ConcreteFirst(FactoryInterface):


    def create_productA(self):
        return ConcreteProductA1()


    def create_productB(self):
        return ConcreteProductB1()


# first family of products e.g: Spanish Product A and B
class ConcreteSecond(FactoryInterface):


    def create_productA(self):
        return ConcreteProductA2()


    def create_productB(self):
        return ConcreteProductB2()


# make product A1
class ConcreteProductA1(AbstractProductA):

    def function_first(self):
        return "Concrete Product A1"


# make product A2
class ConcreteProductA2(AbstractProductA):

    def function_first(self):
        return "Concrete Product A2"


# make product B1
class ConcreteProductB1(AbstractProductB):

    def fucntion_firstB(self):
        return "Concrete Product B1"

    def function_collab(self, collaborator: AbstractProductA):
        print(collaborator.function_first())
        return "Concrete Product B1 Collaborator with Product A"


# make product B2
class ConcreteProductB2(AbstractProductB):

    def fucntion_firstB(self):
        return "Concrete Product B2"

    def function_collab(self, collaborator: AbstractProductA):
        print(collaborator.function_first())
        return "Concrete Product B2 Collaborator with Product A"


def client_code(factory: FactoryInterface):

    product_a = factory.create_productA()
    product_b = factory.create_productB()

    print(product_a.function_first())
    print("next")
    print(product_b.function_collab(product_a))


if __name__ == "__main__":

    print("start code")
    client_code(ConcreteFirst())  # create Italian Family Products
    client_code(ConcreteSecond())  # create Spanish Family Products
    print("end code")