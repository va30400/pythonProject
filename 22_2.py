class machine():
    def __init__(self, price):
        self.PRICE = price  # instance variable

    # instance method
    def type(self):
        print("I am a machine")

    # class method
    @classmethod
    def speed(cls, speedo):
        cls.SPEEDO = speedo # class / static variable
        print("my speed is " , cls.SPEEDO)

    # static method
    @staticmethod
    def electricity():
        machine.electric = 5    # local variable
        print(" i use ", machine.electric , " power ")

obj = machine(5000)
obj.type()
obj.speed(300)
obj.electricity()
print(obj.electric)
print(obj.SPEEDO)
print(obj.PRICE)