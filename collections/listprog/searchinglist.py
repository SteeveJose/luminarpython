lst=[10,11,12,13,14,15,16,17,18]
element=int(input("eneter the element for search:"))
flg=0
for item in lst:
    if(item==element):
        flg=1
        break
    else:
        pass
if(flg==1):
    print("element found")
else:
    print("elemnent nt found")

#print(element in list) easy method
