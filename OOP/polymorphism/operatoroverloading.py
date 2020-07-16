class Book:
    def __init__(self,pages):
        self.pages=pages


    def __add__(self,others):#add function
        return(self.pages+others.pages)

    def __sub__(self,others):#sub fuction
        return (self.pages - others.pages)

    def __mod__(self,others):#mod function
        return (self.pages % others.pages)

    def __str__(self):#when object calling default to user
        return str(self.pages)
b=Book(100)
b1=Book(200)
print(b+b1)
print(b-b1)
print(b%b1)