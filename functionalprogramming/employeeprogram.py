#convert all employee name into uppercase
#print employee salary above 15000
#provide increment of 5000 abobe 2 or more exprience
#list all employee designamtion=developer

class Employee:
    def __init__(self,id,name,desig,salary,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
        self.exp=exp
    def __str__(self):
        return self.name
f=open("C:/Users/MyPc/PycharmProjects/luminar/functionalprogramming/employee")
emp=[]
for data in f:
    employee=data.rstrip("\n").split(",")
    print(employee)
    id=employee[0]
    name=employee[1]
    desig=employee[2]
    salary=int(employee[3])
    exp=int(employee[4])
    ob=emp.append(Employee(id,name,desig,salary,exp))
print("********employee name in upper cases***")
namelist=list(map(lambda Employee:Employee.name.upper(),emp))
print(namelist)
print("*******salary above 15000*****")
salarylist=list(filter(lambda Employee:Employee.salary>15000,emp))
for data in salarylist:
    print(data)
print("********increment salary list****")
incrementlist=list(filter(lambda Employee:Employee.exp>=2,emp))
for values in incrementlist:
    print(data,":",data.salary)
    salary=data.salary+5000
    print(data,"' updated salary:",salary)
print("********developer list*****")
designation=list(filter(lambda Employee:Employee.desig=="developer",emp))
for data in designation:
    print("developer:",data)
