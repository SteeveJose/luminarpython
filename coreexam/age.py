currentday=30#int(input("enter the current day:"))
currentmonth=5#int(input("enter the current month:"))
currentyear=2020#int(input("enter the current year:"))
birthday=int(input("enter the birth day:"))
birthmonth=int(input("enter the birth month:"))
birthyear=int(input("enter the birth year:"))
age=currentyear-(birthyear)
if (birthmonth>currentmonth):
    age-=1
if (birthmonth > currentmonth):
    if(birthday>currentday):
        age=age-1
    else:
        pass
print ("the age of the person is",age)
