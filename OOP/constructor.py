#constructor : to initialise instance variables
# constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age):
         self.age=age
         self.name=name

    def printvalue(self):
          print("name is",self.name)
          print("age is",self.age)

obj=Person("anu",25)
obj.printvalue()