uplim=int(input("enter the upper limit:"))
i=0
totaleven=0
totalodd=0
while (i<uplim):
    if(i%2==0):
        totaleven=totaleven+i
    else:
        totalodd=totalodd+i
    i+=1

print("sum of even:",totaleven)
print("sum of odd",totalodd)