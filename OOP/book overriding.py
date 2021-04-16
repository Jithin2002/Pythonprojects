class Book:
    def book_name(self):
        print("The Secrets")
    def author(self):
        print("Rahul")
class Novel(Book):
    def book_name(self):
        print("The science in life")
c=Novel()
c.book_name()