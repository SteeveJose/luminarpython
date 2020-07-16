def prime(num):
        flag=0
        for i in range(2,num):
            if (num%i==0):
                flag=1
                break
            else:
                pass
        if(flag>0):
            print("the",num,"is not a prime")
        else:
            print("the", num, "is a prime")
prime(6)