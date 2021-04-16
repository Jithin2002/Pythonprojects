class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog(Animal):
    def __init__(self,breed,name,age):
        super().__init__(name,age)
        self.breed=breed
    def print(self):
        print("Name",self.name)
        print("Age:",self.age)
        print("Breed:",self.breed)

obj=Dog("Tison",3,"Lab")
obj.print()