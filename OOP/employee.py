class Employee:
    def setValue(self,name,age,sal,id):
        self.name=name
        self.age=age
        self.sal=sal
        self.id=id
    def printValue(self):
        print("name is",self.name)
        print("age is",self.age)
        print("id is", self.sal)
        print("salary is",self.id)
emp = Employee()
emp.setValue("abc", 26,50000,15)
emp.printValue()
