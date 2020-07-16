lst=[10,9,11,8,12,7,13,6]
lst.sort()
low=0
upper=len(lst)-1
flg=0
element=int(input("enter the element to search:"))
while(low<upper):
    mid=(low+upper)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element==lst[mid]):
        flag=1
        break
    elif(element<lst[mid]):
        upper=mid-1
if(flg==1):
    print("element found")
else:
    print("element nt found")

