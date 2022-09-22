class person:
    def __init__(self,name,age):
        self.NAME = name
        self.AGE = age
    def m1(self):
        print(self.NAME, self.AGE)
    def __init__(self,stringy):
        self.STRINGY = stringy
        print(self.STRINGY)
    def __init__(self,numb1,numb2):
        self.NUM1 = numb1
        self.NUM2 = numb2
        print(self.NUM1, self.NUM2)


obj = person("python","po")
