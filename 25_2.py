class AddSub():
    def __init__(self, num1, num2):
        self.NUM1 = num1
        self.NUM2 = num2

    def addsub(self, num1, num2):
        print(self.NUM1 + self.NUM2, " is the addition result")
        print(self.NUM1 - self.NUM2, " is the subtraction result")


class MultDiv():
    def __init__(self, num1, num2):
        self.NUM1 = num1
        self.NUM2 = num2

    def multdiv(self, num1, num2):
        print(self.NUM1 * self.NUM2, " is the multiplication result")
        print(self.NUM1 // self.NUM2, " is the division result")


class Calc(AddSub, MultDiv):
    def __init__(self, num1, num2):
        self.NUM1 = num1
        self.NUM2 = num2
        """self.obj1 = AddSub(num1, num2)
        self.obj2 = MultDiv(num1, num2)"""
        self.calculate(self.NUM1, self.NUM2)

    def calculate(self, a, b):
        self.addsub(a,b)
        self.multdiv(a, b)
        """AddSub.addsub(self, self.NUM1, self.NUM2)
        MultDiv.multdiv(self, self.NUM1, self.NUM2)"""

    def multdiv(self, num1, num2):
        print( "Calc Method" , self.NUM1 * self.NUM2 )


A, B = map(int, input().split())
obj = Calc(A, B)
