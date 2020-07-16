student=input("enter the name of te student:")
m1=float(input("mark for chemistry:"))
m2=float(input("mark of physics:"))
m3=float(input("mark of Maths:"))
to_mark= m1+m2+m3
if(to_mark<130):
    print(student,"failed")
elif(130<=to_mark<135):
    print(student,"got grade:B")
elif(135<=to_mark<140):
    print(student,"got grade:B+")
elif(140<=to_mark<145):
    print(student,"got grade:A")
else:
    print(student,"got grade:A+")