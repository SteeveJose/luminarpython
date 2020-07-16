import re
f=open("C:/Users/MyPc/PycharmProjects/luminar/regularexp/phonenumbers")
validlist=[]
invalidlist=[]
for data in f:
    phnum=data.rstrip("\n").split(",")
for data in phnum:
 x='\d{10}'
 match=re.fullmatch(x,data)
 if(match!=None):
    #print(data,"is a valid phone num")
    validlist.append(data)
 else:
     #print(data,"is a invalid phone num")
    invalidlist.append(data)
print("The valid phone numbers are",validlist)
print("The invalid phone numbers are",invalidlist)

