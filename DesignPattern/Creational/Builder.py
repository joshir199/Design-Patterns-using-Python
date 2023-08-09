"""
The pattern allows you to produce different types and representations of an object using the same construction code.
Traditionally, It can be solved by making multiple number of constructor of the Object based on different features.
But it will make code very bad and not maintainable

Thus, We can separate object construction part from the object representations using builder class/interface.

Further Director class can assist in representing different object types and create object using common builder.

Builder focuses on constructing complex objects step by step. Abstract Factory specializes in creating families of
 related objects. Abstract Factory returns the product immediately, whereas Builder lets you run some additional
  construction steps before fetching the product.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

"""
    The Builder interface/class specifies methods for creating the different parts of
    the Product objects. It can also create in it
"""
class HomeBuilder():
    def __init__(self):
        self.pro1 = None
        self.pro2 = None
        self.pro3 = None



    def setpro1(self, val):
        self.pro1 = val
        return self


    def setpro2(self, val):
        self.pro2 = val
        return self


    def setpro3(self, val):
        self.pro3= val
        return self


# It builds the actual house object based on features added to it and return the House object
    def build(self):
        return House(self)


"""
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """
class House:
    def __init__(self, builder):
        self.pro1 = builder.pro1
        self.pro2 = builder.pro2
        self.pro3 = builder.pro3

    def display(self):
        print(f' pro1 : {self.pro1}')
        print(f' pro2 : {self.pro2}')
        print(f' pro3 : {self.pro3}')


"""
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
class Director():
    def __init__(self):
        self.builder = HomeBuilder()

    def OnePropertyHouse(self, p1):
        return self.builder.setpro1(p1).build()

    def TwoPropertyHouse(self, p1, p2):
        return self.builder.setpro1(p1).setpro2(p2).build()

    def FullPropertyHouse(self, p1, p2, p3):
        return self.builder.setpro1(p1).setpro2(p2).setpro3(p3).build()


director = Director()
onehouse = director.OnePropertyHouse(3)

onehouse.display()
