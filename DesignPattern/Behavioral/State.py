"""
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes.
 It appears as if the object changed its class.

 The main idea is that, at any given moment, there’s a finite number of states which a program can be in.
 Within any unique state, the program behaves differently, and the program can be switched from one state to another
  instantaneously. However, depending on a current state, the program may or may not switch to certain other states.
   These switching rules, called transitions, are also finite and predetermined.

State machines are usually implemented with lots of conditional statements (if or switch) that select the appropriate
 behavior depending on the current state of the object. this “state” is just a set of values of the object’s fields.

 Use the State pattern when you have an object that behaves differently depending on its current state,
 the number of states is enormous, and the state-specific code changes frequently.

 Use the pattern when you have a class polluted with massive conditionals that alter how the class
 behaves according to the current values of the class’s fields.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class StateInterface(ABC):
    """
        The base State class declares methods that all Concrete State should
        implement and also provides a backreference to the Context object,
        associated with the State. This backreference can be used by States to
        transition the Context to another State.
        each state will also have finite possible state to transition
        """
    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def handle_up(self):
        pass

    @abstractmethod
    def handle_down(self):
        pass


class StateGround(StateInterface):

    def handle_up(self):
        self.elevator.setElevatorState(StateFirst())
        print(" now go up to 1st floor")

    def handle_down(self):
        print(" Can't go down")


class StateFirst(StateInterface):

    def handle_up(self):
        self.elevator.setElevatorState(StateTop())
        print(" now go up to 2nd floor")

    def handle_down(self):
        self.elevator.setElevatorState(StateGround())
        print(" now go down to 1st floor")


class StateTop(StateInterface):

    def handle_up(self):
        print(" can't go up")

    def handle_down(self):
        self.elevator.setElevatorState(StateFirst())
        print(" now go down lower floor")


class Elevator(object):

    def __init__(self):
        self.setElevatorState(StateGround())

    def setElevatorState(self, state):      # transition the state to new one and store it as current state
        self._state = state
        self._state.elevator = self         # capturing current state of the elevator

    def press_up_btn(self):
        self._state.handle_up()

    def press_down_btn(self):
        self._state.handle_down()


if __name__ == "__main__":

    elevator = Elevator()
    elevator.press_up_btn()
    elevator.press_up_btn()
    elevator.press_down_btn()
    elevator.press_down_btn()
    elevator.press_down_btn()

