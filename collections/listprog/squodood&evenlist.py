lst=[]
for i in range(200,300):
    lst.append(i)
even=[]
odd=[]
even=[i for i in lst if i%2==0]
print(even)
for item in lst:
    if(item%2==0):
        even.append(item)
    else:
        odd.append(item)
print("the even list is:",even)      #can use (i**2) in print statement easily.but with using prime the program changes
print("the odd list is:",odd)

def seq(lst):
    squares=[]
    for item in lst:
         squares.append(item**2)
    return squares

evensquare= seq(even)
print("even square:",evensquare)
oddsquare= seq(odd)
print("odd square:",oddsquare)