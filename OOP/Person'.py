class Person:
    def setValue(self,name,age):
        self.name=name
        self.age=age
class Job:
    def set(self,jobname,salary):
        self.jobname=jobname
        self.salary=salary

class Child(Person,Job):
    def set1(self,cname,cage):
        self.cname=cname
        self.cage=cage
    def printValue(self):
        print(self.name,self.age,self.jobname,self.salary,self.cname,self.cage)
class Mark(Child):
    def set2(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def print2(self):
        print("child details:",self.cname,self.cage,"total marks:",self.m1+self.m2)

obj=Mark()
obj.setValue("Sachin",45)
obj.set("developer",40000)
obj.set1("arjun",18)
obj.set2(50,46)
obj.printValue()
obj.print2()