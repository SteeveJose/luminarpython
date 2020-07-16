lst=[2,1,4,3]
lst.sort()
val=int(input("enter the value of pairs:"))
low=0
upp=len(lst)-1
while(low<upp):
    res=lst[low]+lst[upp]
    if(res==val):
        print("pairs",lst[low],lst[upp])
        break
    elif(res<val):
        low=low+1
    elif(res>val):
        upp=upp-1