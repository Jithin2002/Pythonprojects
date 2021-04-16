class Employee:
    cmpny_name="luminar technologies"
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
        print("company name is",Employee.cmpny_name)
emp = Employee()
emp.setValue("abc", 26,50000,15)
emp.printValue()
ab=Employee()
ab.setValue("bv",25,535555,45)
ab.printValue()
