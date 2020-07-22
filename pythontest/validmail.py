import re
f=open("C:/Users/MyPc/PycharmProjects/luminar/pythonexam/employeenew.txt","r")
f1=open("C:/Users/MyPc/PycharmProjects/luminar/pythonexam/validmails","w")
eid=[]
for lines in f:
    employee = lines.rstrip("\n").split(",")
    email=employee[3]
    eid.append(email)
print(eid)

for data in eid:
    pattern='[a-zA-z]\w.*[_]*\w*[.]*@[a-z]*[.][a-z]{3}'
    match=re.fullmatch(pattern,data)

    if(match!=None):
        f1.write(data+"\n")
    else:
        print("invalid")


