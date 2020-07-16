#ploymorphism many forms
#method overloading
#method overriding
#operator overloading


#method overloading
#   same method name different num of arguments
# value only recent callt

class mathsOp:
    def add(self):
        print("inside no arg method")
    def add(self,num1):
        print("inside one arg method")
    def add(self,num1,num2):
        print("inside two arg method")

ob=mathsOp()
ob.add(10,20)