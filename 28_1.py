from abc import *

class Parent(ABC):

    def __init__(self):
        print("i am parent")

    @abstractmethod
    def m1(self):
        pass


class Child(Parent):

    def m1(self):
        print("i am implementation")

obj = Child()
obj.m1()

obj2 = Parent()





