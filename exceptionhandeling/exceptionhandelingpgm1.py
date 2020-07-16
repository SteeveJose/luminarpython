#exception
# it is an abnormal situation that terminates the program execution

# multiple exception cases treated multiple try s and except

#exception handeling

#try:
 #   doubtful code
#except:
 #   code to handle exception

num1=int(input("enter the number"))
num2=int(input("enter the number"))
try:
    res = num1 / num2
    print("result=",res),
except:

finally:#final operation even exception occured
    print("i have one database operation")
    print("i have file operation")