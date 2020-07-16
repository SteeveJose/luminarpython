class Student():
    def __init__(self,name,rol,course):
        self.name=name
        self.rol=rol
        self.course=course
    def printValues(self):
        print(self.name,",",self.rol,",",self.course)

b=Student("steeve",23,"btech")
b.printValues()