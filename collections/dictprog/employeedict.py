employee={"name":"arun","id":18,"salary":15000,"des":"manager"}
print(employee["name"])
for k,v in employee.items():
    print(k,",",v)
employee["exp"]=2
print(employee)
employee["salary"]+=5000
print(employee)