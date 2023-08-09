"""
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they’re observing.

The object that has some interesting state is often called subject, but since it’s also going to notify other
objects about the changes to its state, we’ll call it publisher. All other objects that want to track changes
to the publisher’s state are called subscribers.

The Observer pattern suggests that you add a subscription mechanism to the publisher class so individual objects
 can subscribe to or unsubscribe from a stream of events coming from that publisher.

 Use the Observer pattern when changes to the state of one object may require changing other objects, and the
 actual set of objects is unknown beforehand or changes dynamically.

"""

from abc import ABC, abstractmethod
from typing import List


#Subject's interface from where multiple subjects can be implement these methods.
class EventInterface(ABC):

    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Object's interface which all objects will implement to get notifed by subject. (e.g - signup by email or buy ticket)
class ObserverInterface(ABC):

    @abstractmethod
    def update(self):
        pass


# create object class, which will take Subject to which it will subscribe
class Observer(ObserverInterface):

    def __init__(self, Name, Event):
        self.name = Name
        Event.subscribe(self)

    def update(self):
        print(f'observer {self.name} is notified')


# create subject class and implement subscription mechanism and store all subscribers
class ConcreteEventA(EventInterface):

    observerList: List[Observer]

    def __init__(self):
        self.observerList = []

    def subscribe(self, observer):
        if observer in self.observerList:
            print(f'observer {observer.name} has already Subscribed')
        else:
            self.observerList.append(observer)
            print(f'observer {observer.name} has Subscribed')

    def unsubscribe(self, observer):
        self.observerList.remove(observer)
        print(f'observer {observer.name} has Unsubscribed')

    def notify(self):
        for obs in self.observerList:
            obs.update()


if __name__ == "__main__":

    eventA = ConcreteEventA()
    obj1 = Observer("A", eventA)
    obj2 = Observer("B", eventA)
    obj3 = Observer("C", eventA)
    obj4 = Observer("D", eventA)
    obj5 = Observer("E", eventA)

    eventA.subscribe(obj3)

    eventA.unsubscribe(obj4)
    eventA.unsubscribe(obj2)

    eventA.notify()

    eventB = ConcreteEventA()
    oobj1 = Observer("X", eventB)
    oobj2 = Observer("Y", eventB)
    oobj3 = Observer("Z", eventB)
    oobj4 = Observer("M", eventB)
    oobj5 = Observer("N", eventB)

    eventB.subscribe(obj4)


    eventB.notify()
