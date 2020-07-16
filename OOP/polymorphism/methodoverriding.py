class Parent:
    def Phone(self):
        print("parent have nokia")


class Child(Parent):
    def Phone(self):
        print("i have iphone")


c=Child()
c.Phone()
