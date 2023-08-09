"""
Decorator is a structural design pattern that lets you attach new behaviors to objects
by placing these objects inside special wrapper objects that contain the behaviors.

A wrapper is an object that can be linked with some target object. The wrapper contains the same set of methods
as the target and delegates to it all requests it receives. However, the wrapper may alter the result by doing
something either before or after it passes the request to the target.

Use the Decorator pattern when you need to be able to assign extra behaviors to objects at
 runtime without breaking the code that uses these objects.

The Decorator lets you structure your business logic into layers, create a decorator for each layer and
compose objects with various combinations of this logic at runtime.

Decorator and Proxy have similar structures, but very different intents. Both patterns are built on the
composition principle, where one object is supposed to delegate some of the work to another.
The difference is that a Proxy usually manages the life cycle of its service object on its own,
whereas the composition of Decorators is always controlled by the client.
"""

from __future__ import annotations
import functools

class DecoratorClass():

    @staticmethod
    def decorator_normal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Started")
            func(*args, **kwargs)
            print("End")

        return wrapper

    def decorator_sum(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("sum started")
            val = func(*args, **kwargs)
            print(f'sum ended, and Its value is: {val}')
            return val

        return wrapper

class ObjectClass():

    @DecoratorClass.decorator_normal
    def someFunc(self, a):
        print(f'Value of {a}')

    @DecoratorClass.decorator_sum
    def sumFunc(self, a, b):
        return a+b


obj = ObjectClass()

obj.someFunc(9)
obj.sumFunc(5, 6)

