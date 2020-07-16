class Bank():
    def accountCreate(self,accno,acctype,holdername):
        self.bname="SBI"
        self.accno=accno
        self.acctype=acctype
        self.holdername=holdername
        self.balance=3000
    def deposit(self,depoamount):
        self.balance=self.balance+depoamount
        print("account credited:",depoamount)
    def withdraw(self,withdrawamount):
        if(self.balance<withdrawamount):
            print("account has insufficient balance")
        else:
            self.balance-=withdrawamount
            print("the acoount debited",withdrawamount)
    def balenq(self):
        print("ur available balance:",self.balance)

b=Bank()
b.accountCreate(1020,"savings","ajay")
b.deposit(2000)
b.balenq()
b.withdraw(400)
b.balenq()

