class P1:#can access only P1
    def m1(self):
        print("inside parent1")
class P2(P1):#can access p2 and p1
    def m1(self):
        print("inside parent 2")
    def m2(self):
        print("inside parent1")
class P3(P2,P1):#can access p3 and p2, and p1 through p2
    def m3(self):
        print("inside parent3")

ob=P3()
ob.m1()#access m in parent 2 cuz of firstcum basis in p3 paranthesis
