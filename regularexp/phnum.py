import re
x='\d{10}'
vname=input("enter a phone num:")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid phone num")
else:
    print("invalid phone num")


