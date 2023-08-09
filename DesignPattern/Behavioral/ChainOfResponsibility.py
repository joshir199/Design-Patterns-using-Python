"""
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
 Upon receiving a request, each handler decides either to process the request or to pass it to the next handler
  in the chain.

  the Chain of Responsibility relies on transforming particular behaviors into stand-alone objects called handlers.
  The request, along with its data, is passed to this method as an argument.
  The pattern suggests that you link these handlers into a chain. Each linked handler has a field for storing a
  reference to the next handler in the chain. In addition to processing a request, handlers pass the request further
   along the chain.
   Here’s the best part: a handler can decide not to pass the request further down the chain and effectively
   stop any further processing.
It’s crucial that all handler classes implement the same interface. Each concrete handler should only care about
the following one having the execute method.
Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in various
 ways, but the exact types of requests and their sequences are unknown beforehand.
"""

from abc import ABC, abstractmethod


class HandlerInterface(ABC):
    """
        The Handler interface declares a method for building the chain of handlers.
        It also declares a method for executing a request.
        """
    @abstractmethod
    def setnext(self, handler):
        pass

    @abstractmethod
    def handle(self):
        pass


class Handler(HandlerInterface):
    """
       The default chaining behavior can be implemented inside a base handler
       class.
       """
    nexthandler = None

    def setnext(self, handler):
        self.nexthandler = handler
        return handler

    def handle(self, request):
        if self.nexthandler is not None:
            return self.nexthandler.handle(request)
        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""
class FirstHandler(Handler):

    def handle(self, request):
        if request == "First":
            return "Handled at First"
        else:
            return super().handle(request)


class SecondHandler(Handler):

    def handle(self, request):
        if request == "Second":
            return "Handled at Second"
        else:
            return super().handle(request)


class ThirdHandler(Handler):

    def handle(self, request):
        if request == "Third":
            return "Handled at Third"
        else:
            return super().handle(request)


class LastHandler(Handler):

    def handle(self, request):
        if request == "Last":
            return "Handled at Last"
        else:
            return super().handle(request)


if __name__ == "__main__":

    first = FirstHandler()
    second = SecondHandler()
    third = ThirdHandler()
    forth = LastHandler()

    first.setnext(second)
    second.setnext(third)
    third.setnext(forth)
    forth.setnext(first)  # cyclic dependency. Not a good thing

    ans = second.handle("First")
    print(ans)