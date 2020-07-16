class Student():
    def __init__(self,rollno,name,course,mark):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.mark=mark
    def printValues(self):
        print("rollno:",self.rollno,"name:",self.name,"course:",self.course,"mark:",self.mark)
f=open("C:/Users/MyPc/PycharmProjects/luminar/OOP/studentdata")
stu=[]
for data in f:
        student=data.rstrip("\n").split(",")
        print(student)
        rollno=student[0]
        name=student[1]
        course=student[2]
        mark=int(student[3])
        ob=Student(rollno,name,course,mark)
        stu.append(ob)
for student in stu:
    if(student.mark>150):
        print(student.name,"got more than 150 marks")
for student in stu:
    s=student.name
    print (s.upper())
def courseList(course_name):
    print("*******The",course_name, "students*****")
    for student in stu:
        course=student.course
        if (course==course_name):
            print(student.name)

courseList("btech")