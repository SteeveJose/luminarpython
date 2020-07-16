lst=[1,2,3,4,5,6,7,8,9,]
value=int(input("enter the element:"))
for i in lst:
    for j in lst:
        if(i+j==value):
            print([i,j],"=",value)
        else:
            pass
