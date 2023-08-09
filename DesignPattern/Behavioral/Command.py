"""
Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information
about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s
execution, and support undoable operations.

The Command pattern can turn a specific method call into a stand-alone object. This change opens up a lot of
interesting uses: you can pass commands as method arguments, store them inside other objects, switch linked
 commands at runtime, etc.

Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.

Use the Command pattern when you want to implement reversible operations.
To be able to revert operations, you need to implement the history of performed operations. The command history
is a stack that contains all executed command objects along with related backups of the application’s state.

More UseCases: GUI buttons, Networking, Threading/Parallel processing, Multi-Level Redo/Undo, transactional behaviour
doing network calls like RESTApi calls
"""

from abc import ABC, abstractmethod
from typing import List

#receiver
class Light():
    """
        The Receiver classes contain some important business logic. They know how to
        perform all kinds of operations, associated with carrying out a request. In
        fact, any class may serve as a Receiver.
        This will execute on the action in the end.
        """
    def execute_ON(self):
        print("Light is ON")

    def execute_OFF(self):
        print("Light is Off")

#command
class CommandInterface(ABC):
    """
        The Command interface declares a method for executing a command.
        """
    @abstractmethod
    def execute(self):
        pass

class Command_ON(CommandInterface):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.execute_ON()


class Command_OFF(CommandInterface):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.execute_OFF()

#invoker
class CommandInvoker():
    """
        The Invoker is associated with one or several commands. It sends a request
        to the command.
        """
    def __init__(self):
        self.commandListStack = {}

    def register(self, commandName, command):
        self.commandListStack[commandName] = command

    def run(self, commandName):
        if commandName in self.commandListStack.keys():
            self.commandListStack[commandName].execute()
        else:
            print("Command not found")


if __name__ == "__main__":

    invoker = CommandInvoker()

    rec = Light()
    cmd1 = Command_ON(rec)
    cmd2 = Command_OFF(rec)

    invoker.register("ON", cmd1)
    invoker.register("OFF", cmd2)

    invoker.run("ON")
    invoker.run("POWER")

