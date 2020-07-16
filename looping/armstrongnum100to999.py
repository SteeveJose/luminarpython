num=int(input("enter the number:"))
num1=num
arm=0
while (num>0):
    r=num%10
    arm=arm+(r**3)
    num=num//10
if(arm==num1):
    print(arm,"is a armstrong number")
else:
    print(arm,"is nt a armstrong number")
