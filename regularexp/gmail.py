import re
x="[a-zA-Z]\w*@gmail[.]com"# we can use/d
vname=input("enter a gmail:")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid gmail")
else:
    print("invalid gmail name")


