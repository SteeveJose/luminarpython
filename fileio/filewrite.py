f=open("abc.txt","r")
fw=open("out.txt","w")
for data in f:
    num=int(data)
    if((num%2)==0):
        fw.write(str(num)+"\n")