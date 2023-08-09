"""
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without
revealing the details of its implementation.

Use the Memento pattern when you want to produce snapshots of the object’s state to be able to restore
 a previous state of the object.

You can use Command and Memento together when implementing “undo”. In this case, commands are responsible for
 performing various operations over a target object, while mementos save the state of that object just
  before a command gets executed.
"""
from __future__ import annotations


class Memento:
    """
        The Memento class provides a way to retrieve the memento's metadata,
        such as creation date or name. However, it doesn't expose the Originator's
        state.
        """

    def __init__(self, state):
        self._state = state


class Originator:
    """
        The Originator holds some important state that may change over time. It also
        defines a method for saving the state inside a memento and another method
        for restoring the state from it.
        """

    def __init__(self):
        self._state = ""

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        print(f"Originator: Setting state to `{state}`")
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento._state


class CareTaker:
    "Guardian. Provides a narrow interface to the mementos for staring mementos as a backup and "
    # undo the step aat any index"
    """
        The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
        doesn't have access to the originator's state, stored inside the memento. It
        works with all mementos via the base Memento interface.
        """

    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def backup(self):
        "Store a new Memento of the Originators current state"
        print("CareTaker: Getting a copy of Originators current state")
        memento = self._originator.save()
        self._mementos.append(memento)

    def undo(self, index):
        print("CareTaker: Restoring Originators state from Memento")
        sz = len(self._mementos)
        if 0 <= index < sz:
            memento = self._mementos[index]
            self._originator.restore(memento)


if __name__ == "__main__":
    originator = Originator()
    memento = Memento("First")
    caretaker = CareTaker(originator)

    originator.state = "state #1"
    caretaker.backup()
    originator.state = "state #2"
    caretaker.backup()
    originator.state = "state #3"
    caretaker.backup()
    print(originator.state)

    caretaker.undo(0)
    print(originator.state)
