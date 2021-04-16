class Student:
    def __init__(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark


    def printvalue(self):
        print("name",self.name)
        print("rollno",self.roll)
        print("course",self.course)
        print("mark",self.mark)

    def __str__(self):
        return self.name

f=open("stud", "r")
for lines in f:
    words=lines.rstrip("\n").split(",")
    name=words[0]
    roll=words[1]
    course=words[2]
    mark=int(words[-1])
    obj=Student(name,roll,course,mark)
    if(mark==200):
        print(obj)
        obj.printvalue()
