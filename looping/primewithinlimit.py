lowlim=int(input("enter a lower limit:"))
uplim=int(input("enter a upper limit:"))
for num in range(lowlim,(uplim+1)):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
        else:
            pass
    if(flag==1):
        pass
    else:
        print(num,"is prime")
