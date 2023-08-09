
from threading import RLock, Thread
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonMetaThreadSafe(type):

    _instances = {}
    _lock = RLock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonThreadSafe(metaclass=SingletonMetaThreadSafe):
    val = ""
    def __init__(self, value):
        self.val = value

    def business(self):
        self.val = "business"
        print("business")




class Singleton(metaclass=SingletonMeta):

    def business(self):
        print("business")


def testSngleton(val):
    singletn = SingletonThreadSafe(val)
    print(singletn.val)



s1 = Singleton()
s2 = Singleton()

print(id(s1))
print(id(s2))


t1 = Thread(target=testSngleton, args=("t1",))
t2 = Thread(target=testSngleton, args=("t2",))

t1.start()
t2.start()