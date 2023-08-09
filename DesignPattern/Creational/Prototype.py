"""
Prototype is a creational design pattern that lets you copy existing objects without making your code
 dependent on their classes. When you need an object like the one you’ve configured, you just clone a prototype
  instead of constructing a new object from scratch.

  Suppose you have a complex class that requires a laborious configuration before it can be used.
  There are several common ways to configure this class, and this code is scattered through your app.
  To reduce the duplication, you create several subclasses and put every common configuration code into
  their constructors. You solved the duplication problem, but now you have lots of dummy subclasses.

The Prototype pattern lets you use a set of pre-built objects configured in various ways as prototypes.
Instead of instantiating a subclass that matches some configuration, the client can simply look for an
appropriate prototype and clone it.
"""


from abc import ABC, abstractmethod
import copy


class FactoryClass(ABC):

    @abstractmethod
    def clone(self):
        pass


class ConcreteShallow(FactoryClass):

    def __init__(self, num=0, name="", numlist=[], namedict={}):
        self.a = num
        self.b = name
        self.c = numlist
        self.d = namedict

    def clone(self):
        newobj = self.__class__(
            self.a,
            self.b,
            copy.copy(self.c),
            copy.copy(self.d)
        )
        return newobj

    def __str__(self):
        return f'a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}'


class ConcreteDeep(FactoryClass):

    def __init__(self, num=0, name="", numlist=[], namedict={}):
        self.a = num
        self.b = name
        self.c = numlist
        self.d = namedict

    def clone(self):
        newobj = type(self)(
            self.a,
            self.b,
            copy.deepcopy(self.c),
            copy.deepcopy(self.d)
        )
        return newobj

    def __str__(self):
        return f'a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}'


if __name__ == "__main__":

    obj1 = ConcreteShallow(1, "Hi", [[1,2,3],2,3], {'a':1, 'b':2})
    print(f'obj1: {obj1}')
    obj2 = obj1.clone()
    obj2.c[0][0] = 9    # In this case, shallow copy will change the original object values
    print(f'obj2: {obj2}')
    print(f'obj1: {obj1}')

    """
    Try with Deep Copy
    """
    print(" Try with Deep Copy")
    obj1 = ConcreteDeep(1, "Hi", [[1, 2, 3], 2, 3], {"a": 1, "b": 2})
    print(f'obj1: {obj1}')
    obj2 = obj1.clone()
    obj2.c[0][0] = 9  # In this case, shallow copy will change the original object values
    print(f'obj2: {obj2}')
    print(f'obj1: {obj1}')
