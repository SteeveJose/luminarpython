#first one ,starting with a.......k
#2nd one ,should be a digit divisibe by 3
#3rd one ,any number character
import re
x="[a-k][369][a-z]+"
vname=input("enter a variable name:")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")


