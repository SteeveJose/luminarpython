lst=[10,11,12,13,14,15,16,17,18]
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("the even list is:",even)
print("the odd list is:",odd)    #can reduce all statements into ( even=[i for i in lst if i%2==0])
                                                                #print(even)