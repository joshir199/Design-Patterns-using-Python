# It separates the process of creating an object from the code that depends on the interface of the object.
# The first step when you see complex conditional code in an application is to identify the common goal
# of each of the execution paths (or logical paths).

# The central idea in Factory Method is to provide a separate component with the responsibility to decide
# which concrete implementation should be used based on some specified parameter.

# An Object Factory gives additional flexibility to the design when requirements change.
# ABC = Abstract Base Class
from abc import abstractmethod, ABC

class FactoryObject(ABC):
    """
        The Creator class declares the factory method that is supposed to return an
        object of a Product class. The Creator's subclasses usually provide the
        implementation of this method.

        Note: It has only one product type
    """
    @abstractmethod
    def createFactory(self):
        pass


    def defaultImplementation(self):
        product = self.createFactory()
        print(product.createProduct())




"""
    The Product interface declares the operations that all concrete products
    must implement. Interface class will always all abstract method.
    We can have multiple interface for building different common functionality of products 
    """
class Product(ABC):

    @abstractmethod
    def createProduct(self):
        pass

"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""
class ConcreteCreatorA(FactoryObject):

    def createFactory(self)->Product:
        return ConcreteProductA()


class ConcreteCreatorB(FactoryObject):

    def createFactory(self)->Product:
        return ConcreteProductB()


"""
Concrete Products provide various implementations of the Product interface.
"""
class ConcreteProductA(Product):

    def createProduct(self):
        return "Create Product A"


class ConcreteProductB(Product):

    def createProduct(self):
        return "Concrete Product B"



def clientCode(factory_object: FactoryObject):

    print(f' do something')
    obj = factory_object.createFactory()
    print(obj)
    print(factory_object.defaultImplementation())


if __name__== "__main__":
    print("start code")
    clientCode(ConcreteCreatorA())

    print("another")
    clientCode(ConcreteCreatorB())

    print("end code")

