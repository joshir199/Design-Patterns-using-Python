"""
Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by
 sharing common parts of state between multiple objects instead of keeping all the data in each object.

 Its main goal is to reduce RAM size of the App it takes.



Divide fields of a class that will become a flyweight into two parts:

    the intrinsic state: the fields that contain unchanging data duplicated across many objects
    the extrinsic state: the fields that contain contextual data unique to each object

Leave the fields that represent the intrinsic state in the class, but make sure they’re immutable.
They should take their initial values only inside the constructor.

Similar Concept of CDN or Cache
"""

from typing import Dict, List

class Flyweight(object):

    def __init__(self, properties):
        self.property = properties

    def sell(self):
        print(f"sell phone with properties: {self.property}")


"""
    The Flyweight Factory creates and manages the Flyweight objects. It ensures
    that flyweights are shared correctly. When the client requests a flyweight,
    the factory either returns an existing instance or creates a new one, if it
    doesn't exist yet.
    """
class FlyweightFactory:

    propertiesStore: Dict[str, Flyweight] = {}

    def getSmartPhone(self, properties: List):

        key = self.getKey(properties)
        print(key)
        if key in self.propertiesStore.keys():
            print("phone already exist")
        else:
            print("Create New SmartPhone")
            self.propertiesStore[key] = Flyweight(properties)
        return self.propertiesStore[key]

    def listSmartPhones(self):
        return self.propertiesStore.items()

    def getKey(self, properties) -> str:
        return '-'.join(properties)


if __name__=="__main__":

    factory = FlyweightFactory()
    obj = factory.getSmartPhone(["Samsung", "S20", "128GB", "Black"])
    obj2 = factory.getSmartPhone(["Samsung", "S21", "128GB", "Black"])
    obj3 = factory.getSmartPhone(["Samsung", "S20", "128GB", "Golden"])
    obj4 = factory.getSmartPhone(["Samsung", "S20", "128GB", "Black"])

    obj4.sell()
    print("all phone items")
    phonelist = factory.listSmartPhones()
    for item in phonelist:
        print(item)

