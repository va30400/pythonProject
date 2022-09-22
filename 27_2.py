class parent():
    def __init__(self):
        print("parent constructor")

    def m1(self, a , b):
        print(a+b)

class child(parent):
    def __init__(self):
        print("child constructor")

    def m1(self, a,b):
        print("sum of numbers is", a+b)
        super().m1(a,b)

obj = child()
obj.m1(4,6)