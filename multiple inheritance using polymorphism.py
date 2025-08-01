class A:
    def fun1(self):
        super().fun1()
        print("Method 1!!")

class B:
    def fun1(self):
        print("Method 2!!")

class C(A,B):
    def fun1(self):
        super().fun1()
        print("Method 3!!")

obj = C()
obj.fun1()