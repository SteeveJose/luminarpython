num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
if (num1>num2 and num1>num3):
    if(num2>num3):
        print(num2,"is the second largest number")
    else:
        print(num3,"is the second largest number")
elif (num2>num1 and num2>num3):
    if(num1>num3):
        print(num2,"is the second largest number")
    else:
        print(num3, "is the second largest number")
elif (num3>num1 and num3>num2):
    if(num1>num2):
        print(num1, "is the second largest number")
    else:
        print(num2, "is the second largest number")
else:
    pass