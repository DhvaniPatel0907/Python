class Myclass:
    def fun1(self):
        print("1 Class")

class Myclass2(Myclass):
    def fun2(self):
        print("2 Class")

class Myclass3(Myclass):
    def fun3(self):
        print("3 Class")

obj = Myclass2()
obj1 = Myclass3()

obj.fun1()
obj.fun2()
obj1.fun3()