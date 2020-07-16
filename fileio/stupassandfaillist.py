f=open("student","r")
fpass=open("stupass","r")
ffail=open("stufail","w")
st1=set()
st2=set()
def readDataFromFile(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
st1=readDataFromFile(f)
st2=readDataFromFile(fpass)
print(st1)
print(st2)
stufail=st1-st2
print(stufail)