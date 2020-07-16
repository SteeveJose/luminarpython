class Employee():
    def __init__(self,id,empname,desig,salary,exp):
        self.id=id
        self.empname=empname
        self.desig=desig
        self.salary=salary
        self.exp=exp
    def printEmp(self):
        print(self.id,"name",self.empname,"desig",self.desig,"salary",self.salary,"exp",self.exp)
f=open("C:/Users/MyPc/PycharmProjects/luminar/OOP/emp")
emp=[]
for data in f:
    employee=data.rstrip("\n").split(",")
    print(employee)
    id=employee[0]
    empname=employee[1]
    desig=employee[2]
    salary=int(employee[3])
    exp=employee[4]
    ob=Employee(id,empname,desig,salary,exp)
    emp.append(ob)
    print(emp)
"""for employee in emp:
    if(employee.salary>17000):
        print(employee.empname)
for employee in emp:
    s=employee.empname
    print (s.upper())"""