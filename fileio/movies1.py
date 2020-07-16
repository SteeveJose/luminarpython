f=open("C:/Users/MyPc/PycharmProjects/luminar/fileio/movies.csv")
dict={}
i=0
for lines in f:
    words=lines.rstrip("\n").split(",")
    print(words)
    year=words[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

    i+=1
    if(i==50):
        break
print(dict)