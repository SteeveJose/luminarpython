#******list comprehention********


#lst=[1,2,3,4,5,6]
#sq=[(i**2) for i in lst]
#print(sq)

#print paIRS

"""normal method

for i in lst:
    for j in lst:
        print(i,j)"""

#lst=[1,2,3,4]
#lst1=[5,6,7,8,]
#pairs=[(i,j) for i in lst for j in lst1]
#print(pairs)

#print powerpair


"""lst=[1,2,3,4,]
lst2=[5,6,7,8,]
pairs=[(i,i**j) for i in lst for j in lst2]
print (pairs)"""

#even number in lst

lst=[1,2,3,4,]
even=[i for i in lst if i%2==0]
print(even)