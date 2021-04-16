class Employee:
    def __init__(self,name,age,sal,id):
        self.name=name
        self.age=age
        self.sal=sal
        self.id=id
    def printValue(self):
        print("name is",self.name)
        print("age is",self.age)
        print("id is", self.sal)
        print("salary is",self.id)
emp =Employee("abc", 26,50000,15)
emp.printValue()
