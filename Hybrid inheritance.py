class Myclass:
    def fun1(self):
        print("1 Class")

class Myclass2(Myclass):
    def fun2(self):
        print("2 Class")

class Myclass3:
    def fun3(self):
        print("3 Class")

class Myclass4(Myclass2,Myclass3):
    def fun4(self):
        print("4 Class")

obj = Myclass4()

obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()