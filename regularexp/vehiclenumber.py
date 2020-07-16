import re
x="KL[0-9]{2}[A-Z]{2}[1-9]{4}"# we can use/d
vname=input("enter a variable name:")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")


