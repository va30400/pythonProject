class Parent1():
    def __init__(self):
        print("I am parent1")

    """def meth(self):
        print("I am meth in Parent1")"""

class Parent2():
    def __init__(self):
        print("I am parent2")

    def meth(self):
        print("I am meth1 in Parent2")

class Child1(Parent1, Parent2):
    def __init__(self):
        print("I am Child1")


obj1 = Child1()

obj1.meth()
obj1.meth()