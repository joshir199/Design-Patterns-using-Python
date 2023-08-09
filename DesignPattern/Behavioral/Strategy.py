"""
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a
separate class, and make their objects interchangeable.

Use the Strategy pattern when you want to use different variants of an algorithm within an object and
 be able to switch from one algorithm to another during runtime.
 Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
 Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not
  be as important in the context of that logic.

  Use the pattern when your class has a massive conditional statement that switches between
  different variants of the same algorithm.
  You can swap algorithms used inside an object at runtime.
"""

from abc import ABC, abstractmethod


class StrategyInterface(ABC):
    """
        The Strategy interface declares operations common to all supported versions
        of some algorithm.

        The Context uses this interface to call the algorithm defined by Concrete
        Strategies.
        """
    @abstractmethod
    def runAlgorithm(self):
        pass


class StrategyA(StrategyInterface):

    def runAlgorithm(self):
        print("run strategy Algo A")


class StrategyB(StrategyInterface):

    def runAlgorithm(self):
        print("run Strategy Algo B")


class ContextObject(object):
    """
        The Context defines the interface of interest to clients.
        """
    def __init__(self, strategy: StrategyInterface):
        self._strategy = strategy

    """
           Usually, the Context accepts a strategy through the constructor, but
           also provides a setter to change it at runtime.
           """
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def do_operation(self):
        """
                The Context delegates some work to the Strategy object instead of
                implementing multiple versions of the algorithm on its own.
                """
        self._strategy.runAlgorithm()

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    stA = StrategyA()
    stB = StrategyB()
    context = ContextObject(stB)
    context.do_operation()

    context.strategy = stA
    context.do_operation()