f=open("person","r")
emp={}
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    age=values[2]
    desig=values[3]
    exp=values[4]
    salary=values[5]
    if (id not in emp):
        emp[id]={"id":id,"name":name,"age":age,"desig":desig,"exp":exp,"salary":salary}
    else:
        pass
for k,v in emp.items():
    print(k,"\t",v)


def printEmployee(**kwargs):
    if "id" in kwargs:
        id = kwargs["id"]
        if id in emp:
            print("employee name:",emp[id]["name"])
        else:
            print("employee nt found")
    if "property" in kwargs:
        prop=kwargs["property"]
        print(emp[id][prop])

printEmployee(id="105",property="desig")