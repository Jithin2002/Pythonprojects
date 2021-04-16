#single inheritance
class Parent:
    parent_name='arun'
    my_name='jit'
    def m1(self,age):
        self.age=age
        print("my name is",Parent.my_name)
        print("my age",self.age)
class Child(Parent):
    def m2(self,cage):
        self.cage=cage
        print("parent name is",Parent.parent_name)
        print("my age",self.age)
        print("parent age",self.cage)
c=Child()
c.m1(25)
c.m2(81)


