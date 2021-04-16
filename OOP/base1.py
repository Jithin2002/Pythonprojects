class Person: #name of class starts with capital letter
    def walk(self): #to create method use function object name starts with small letter
        print("person is walking")
    def run(self):
        print("person is running")
    def jumping(self):
        print("person is jumping")



obj= Person() #to create object of that class obj is the reference name using thisreference we create the object
obj.walk()  #method call
obj.run()

