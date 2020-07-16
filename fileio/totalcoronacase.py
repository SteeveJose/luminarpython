f=open("C:/Users/MyPc/PycharmProjects/luminar/fileio/complete.csv")
dict={}
i=0
for lines in f:
    report=lines.rstrip("\n").split(",")
    print(report)
    state=report[1]
    state1=report[1]
    cases=int(report[4])
    curedcases=int(report[5])
    if(state not in dict):
        dict[state]=cases
        dict[state1]=curedcases
    else:
        dict[state]=cases
        dict[state1]=curedcases
print(dict)
statelist=[]
for k,v in dict.items():
    statelist.append((v,k))
print(statelist)
sorteddata=sorted(statelist,reverse=True)
print(sorteddata[:3])