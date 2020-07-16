f=open("C:/Users/MyPc/PycharmProjects/luminar/fileio/complete.csv")
dict={}
i=0
for lines in f:
    report=lines.rstrip("\n").split(",")
    print(report)
    state=report[1]
    cases=int(report[4])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)

