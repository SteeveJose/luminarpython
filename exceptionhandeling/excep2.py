lst=[10,20,30]
num1=int(input("enter the number"))
num2=int(input("enter the number"))
indx=int(input("enter index position to fetch element"))
try:
    res=num1/num2
    print("result=",res)
    print(lst[indx])

except Exception as e:# print curresponding error
    print(e.args)
print("i have one database operation")
print("i have file operation")