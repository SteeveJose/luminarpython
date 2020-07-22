import functools
class Employee():
    def __init__(self,eid,ename,edesig,mailid,salary):
        self.eid=eid
        self.ename=ename
        self.edesig=edesig
        self.mailid=mailid
        self.salary=salary
    def printValues(self):
        print("eid:",self.eid,"ename:",self.ename,"edesig:",self.edesig,"mailid:",self.mailid,"salary:",self.salary)
f=open("C:/Users/MyPc/PycharmProjects/luminar/pythonexam/employeenew.txt")
emp=[]
for data in f:
        employee=data.rstrip("\n").split(",")
        print(employee)
        eid=employee[0]
        ename=employee[1]
        edesig=employee[2]
        mailid=employee[3]
        salary=int(employee[4])
        ob=Employee(eid,ename,edesig,mailid,salary)
        emp.append(ob)

maxsal=functools.reduce(lambda o1,o2 : o1 if o1>o2 else o2,list(map(lambda o1:o1.salary,emp)))
print("The max salary:",maxsal)

