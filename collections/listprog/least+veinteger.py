list=[]
len=int(input("enter the length of list:"))
for i in range(0,len):
    num=int(input())
    list.append(num)
list.sort()
low=0
upp=len
while(low<upp):
    if(list[low]>0):
        print(list[low],"is the least positive integer in the list")
        break
    else:
        low=low+1
