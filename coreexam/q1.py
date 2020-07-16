f=open("C:/Users/MyPc/PycharmProjects/luminar/coreexam/data.txt","r")
dict={}
for data in f:
    values=data.rstrip("\n").split(",")
    print (values)
    dist=values[0]
    temp=int(values[1])
    if dist not in dict:
        dict[dist]=temp
    else:
        if (temp>dict[dist]):
            dict[dist]=temp
        else:
            pass

print(dict)
