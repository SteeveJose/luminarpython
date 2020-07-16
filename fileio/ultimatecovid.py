f=open("C:/Users/MyPc/PycharmProjects/luminar/fileio/complete.csv","r")
covidlist={}
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[1]
    name=values[1]
    totalconf=values[4]
    totalcured=values[6]
    death=values[5]
    if (id not in covidlist):
        covidlist[id]={"id":id,"name":name,"confirmedcases":totalconf,"curedcases":totalcured,"death":death}
    else:
        covidlist[id] = {"id":id,"name":name,"confirmedcases": totalconf, "curedcases": totalcured, "death": death}
for k,v in covidlist.items():
    print(k,"\t\t",v)


def covidData(**kwargs):
    if "id" in kwargs:
        id = kwargs["id"]
        if id in covidlist:
            print("state name:",(covidlist[id]["name"]))
        else:
            print("state nt found")
    if "property" in kwargs:
        prop=kwargs["property"]
        print(covidlist[id][prop])

covidData(id="Kerala",property="death")