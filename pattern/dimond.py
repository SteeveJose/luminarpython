num=int(input("enter the number:"))
def function(num):
    for i in range(1,num+1):
        print(" " * (num-i) + ("*" + " ") * i)
    for i in range(num-1,0,-1):
        print(" "*(num-i)+("*"+" ")*i)

function(num)