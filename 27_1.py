class Parent():
    def __init__(self):
        pass

    def prin(self, * num):
        for i in num:
            print (i)

    def summ(self, a = 2, b = 5):
        print(a+b)

obj = Parent()
obj.summ(5)
obj.summ(3,8)