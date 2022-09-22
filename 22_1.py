class building():
    def __init__(self, floors):
        self.FLOORS = floors
#        print("I have ", self.FLOORS," floors")

    def area(self):
        self.AREA = "INDIA"

    @staticmethod
    def meth():
        building.size = 500

    @classmethod
    def meth2(cls):
        print(building.size)
        building.balcony = "yes"
        print(building.balcony)

    def deleting(self):
        del building.size

    def setFloor(self,floor):
        self.FLOORS = floor

    def getFloor(self):
        print(self.FLOORS)

obj = building(7)
obj.getFloor()