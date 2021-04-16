class Employee:
    company_name="Luminar technolab"
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
        print("companyname",Employee.company_name)
    def __str__(self):
        return str(self.id)+self.name+str(self.age)+str(self.sal)+Employee.company_name
emp = Employee()
emp.setValue("arun", 26,50000,15)
print(emp)
