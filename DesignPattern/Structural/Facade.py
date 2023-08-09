"""
Facade is a structural design pattern that provides a simplified interface to a library, a framework, or
any other complex set of classes.

// There will be some of the classes of a complex 3rd-party video
// conversion framework. We don't control that code, therefore
// can't simplify it.

// We create a facade class to hide the framework's complexity
// behind a simple interface. It's a trade-off between
// functionality and simplicity.

Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.
facade interface makes the client code independent of many of the subsystem’s classes.
The subsystem itself is unaware of the facade.
"""


class taskA(object):

    def doWork(self):
        print("Finished taskA")
        return "taskA"


class taskB(object):

    def doWork(self):
        print("Finished taskB")
        return "taskB"


class taskC(object):

    def doWork(self, taskA, taskB):
        print(f'Finished taskC using product made from {taskA} and {taskB}')


# facade class acts as final interface to client who wants to make project using multiple 3rd party library
class Project(object):

    def __init__(self):
        self.t1 = taskA()
        self.t2 = taskB()
        self.t3 = taskC()

    def make_project(self):
        self.t3.doWork(self.t1.doWork(), self.t2.doWork())


def client_code(project: Project):

    project.make_project()


if __name__ == "__main__":

    obj = Project()
    client_code(obj)


