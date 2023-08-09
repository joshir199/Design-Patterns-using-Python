"""
Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but
 lets subclasses override specific steps of the algorithm without changing its structure.
 The Template Method pattern suggests that you break down an algorithm into a series of steps, turn these steps
  into methods, and put a series of calls to these methods inside a single template method.
  The steps may either be abstract, or have some default implementation. To use the algorithm, the client is
  supposed to provide its own subclass, implement all abstract steps, and override some of the optional ones if needed.

  As you can see, we’ve got two types of steps:

    abstract steps must be implemented by every subclass
    optional steps already have some default implementation, but still can be overridden if needed

Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm,
but not the whole algorithm or its structure.
"""

from abc import ABC, abstractmethod


class ProcessTemplate(ABC):
    """
        The Abstract Class defines a template method that contains a skeleton of
        some algorithm, composed of calls to (usually) abstract primitive
        operations.

        Concrete subclasses should implement these operations, but leave the
        template method itself intact.
        """
    @abstractmethod
    def openfile(self):
        pass

    def readFile(self):
        print("read file")

    @abstractmethod
    def modifyFile(self):
        pass

    # These are "hooks." Subclasses may override them, but it's not mandatory
    # since the hooks already have default (but empty) implementation. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.
    def saveFile(self):
        print("file saved")

    def doOrderedStep(self):
        """
                The template method defines the skeleton of an algorithm in ordered form.
                """
        self.openfile()
        self.readFile()
        self.modifyFile()
        self.saveFile()
        print("all steps done")


class PdfObject(ProcessTemplate):
    """
        Concrete classes have to implement all abstract operations of the base
        class. They can also override some operations with a default implementation.
        """
    def openfile(self):
        print("open pdf file")

    def modifyFile(self):
        print("pdf file has been modified")


class DocObject(ProcessTemplate):

    def openfile(self):
        print("open doc file")

    def modifyFile(self):
        print("doc file has been modified")

    def readFile(self):
        print("read only doc file")


if __name__ == "__main__":

    pdf = PdfObject()
    doc = DocObject()

    pdf.doOrderedStep()
    doc.doOrderedStep()
