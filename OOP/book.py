class Book:
    def setValue(self,Library_name,book_name,author,pages):
        self.Library_name=Library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages

    def printValue(self):
        print("Library name:",self.Library_name)
        print("Book name:",self.book_name)
        print("Author:",self.author)
        print("Pages",self.pages)
obj= Book()
obj.setValue("Muncipal Library","Harry Potter and the Sorcerer's Stone","J.K. Rowling",350)
obj.printValue()