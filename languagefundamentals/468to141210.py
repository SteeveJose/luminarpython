lst=[]
len=int(input("enter the length of list:"))
for i in range(0,len):
    num=int(input())
    lst.append(num)
#print(lst)
lst2=[]
for i in range(0,len):
    num2=sum(lst)-lst[i]
    lst2.append(num2)
#print(lst2)
print("the ouput of",lst, "is",lst2)
