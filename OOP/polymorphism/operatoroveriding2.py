class Book:
    def __init__(self,pages):
        self.pages=pages


    def __add__(self,others):#add function
        return Book(self.pages+others.pages)

    def __sub__(self,others):#sub fuction
        return Book(self.pages - others.pages)

    def __mod__(self,others):#mod function
        return Book(self.pages % others.pages)

    def __str__(self):#when object calling default to user
        return str(self.pages)
b=Book(100)
b1=Book(200)
b2=Book(300)
print(b+b2+b2)
print(b-b1-b2)
print(b%b1%b2)