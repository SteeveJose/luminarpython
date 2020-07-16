class Parent():
    def phone(self):
        print("parent have nokia phone")

class Child(Parent):
    def phone2(self):
        print("child have iphone")



p=Parent()
p.phone()
# p.phone2()  form error

c=Child()
c.phone()
c.phone2()
