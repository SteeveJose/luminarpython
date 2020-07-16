txt=input("enter the text:")
wrd=list(txt)
dict={}
flg=0
for i in wrd:
    if(i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
        print("the recursive character is:",i)
        flg=1
        break
if(flg==0):
    print("No recursive character")