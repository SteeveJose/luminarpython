num=int(input("enter a number:"))
res=0
while(num!=0):
    r=num%10
    res=res+(r**3)
    num=num//10
print("the res is:",res)