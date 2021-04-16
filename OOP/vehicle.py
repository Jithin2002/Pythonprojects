class Vehicle:
    def setValue(self,name,mileage,capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity

    def printValue(self):
        print("name of vehicle",self.name)
        print("mileage",self.mileage)
        print("capacity",self.capacity)

class Bus(Vehicle):
    def fare(self):
        return self.capacity*100

obj= Bus()
obj.setValue("School Bus",10,60)
obj.printValue()
print("fare",obj.fare())