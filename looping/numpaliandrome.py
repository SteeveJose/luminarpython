num=int(input("enter a number:"))
rev=0
while(num!=0):
    r=num%10
    rev=rev*10+r
    num=num//10
print("the reverse of the number is:",rev)