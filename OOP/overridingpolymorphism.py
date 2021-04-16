class Parent:
    def properties(self):
        print("10lakh,2car")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")
c=Child()
c.marry()