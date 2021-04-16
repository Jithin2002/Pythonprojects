class Person:
    def setValue(self,name,age):
        self.age=age
        self.name=name
    def printValue(self,):
        print("name:",self.name)
        print("age:",self.age)

obj=Person()
obj.setValue('ram',23)
obj.printValue()