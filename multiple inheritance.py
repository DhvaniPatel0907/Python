class Myclass:
    def fun1(self):
        print("1 Class")

class Myclass2:
    def fun2(self):
        print("2 Class")

class Myclass3(Myclass,Myclass2):
    def fun3(self):
        print("3 Class")

obj = Myclass3()
obj.fun1()
obj.fun2()
obj.fun3()