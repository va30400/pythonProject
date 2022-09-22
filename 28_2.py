from abc import *

class Parent(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class child1(Parent):
    def m1(self):
        print("i am m1")

class child2(child1):
    def m2(self):
        print("i am m2")

obj = child2()