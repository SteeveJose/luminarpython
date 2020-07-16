lst=[]
len=int(input("enter the length of list:"))
for i in range(0,len):
    num=int(input())
    lst.append(num)
print(lst)
lst2=[]
count=1
for i in range(0,len):
        num2=lst[i]**count
        lst2.append(num2)
        count+=1
print(lst2)