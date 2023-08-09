"""
Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects.
The pattern restricts direct communications between the objects and forces them to collaborate only via mediator object.

The Mediator pattern suggests that you should cease all direct communication between the components which you
want to make independent of each other. Instead, these components must collaborate indirectly, by calling a special
mediator object that redirects the calls to appropriate components. As a result, the components depend only on a
 single mediator class instead of being coupled to dozens of their colleagues.

 The difference between Mediator and Observer is often elusive. In most cases, you can implement either of these
 patterns; but sometimes you can apply both simultaneously. Let’s see how we can do that.
"""

from abc import ABC, abstractmethod


class ComponentI(ABC):

    @abstractmethod
    def notify(self, event):
        pass

    @abstractmethod
    def receive(self):
        pass


class ComponentA(ComponentI):
    """
        The Base Component provides the basic functionality of storing a mediator's
        instance inside component objects.
        """
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, event):
        self._mediator.notifyOthers(event, self)

    def receive(self):
        print(f'Component {self._name} received message')


class Mediator(object):
    """
        The Mediator declares a method used by components to notify the
        mediator about various events. The Mediator may react to these events and
        pass the execution to other components.
        """
    def __init__(self):
        self._components = []

    def addComponents(self, component):
        self._components.append(component)

    def notifyOthers(self, event, component):
        for cmp in self._components:
            if event == "Only One":
                cmp.receive()
                break
            elif cmp is not component:
                cmp.receive()


if __name__ == "__main__":

    mediator = Mediator()
    cmp1 = ComponentA(mediator, "cmp1")
    cmp2 = ComponentA(mediator, "cmp2")
    cmp3 = ComponentA(mediator, "cmp3")
    cmp4 = ComponentA(mediator, "cmp4")

    mediator.addComponents(cmp1)
    mediator.addComponents(cmp2)
    mediator.addComponents(cmp3)
    mediator.addComponents(cmp4)

    cmp2.notify("Only One")
    print("next")
    cmp3.notify("None")

