f=open("C:/Users/MyPc/PycharmProjects/luminar/fileio/complete.csv")
import matplotlib.pyplot as plt
dict={}
i=0
for lines in f:
    report=lines.rstrip("\n").split(",")
    print(report)
    state=report[1]
    cases=int(report[6])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
stateculist=[]
cnt=[]
for k,v in dict.items():
    stateculist.append((v,k))
print(stateculist)
sorteddata=sorted(stateculist,reverse=True)
print(sorteddata[:3])
for val in report:
    cnt.append(val[0])
    stateculist.append(val[1])
plt.bar(stateculist,cnt)
plt.show