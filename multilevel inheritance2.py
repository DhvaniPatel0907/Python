class A:
    def fun1(self):
        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))

class B(A):
    def fun2(self):
        a = int(input("Enter a marks for Maths:"))
        b = int(input("Enter a marks for English:"))
        c = int(input("Enter a marks for Science:"))
        self.a=a
        self.b=b
        self.c=c

class C(B):
    def fun3(self):
        total = self.a + self.b + self.c
        percent = total // 3
        print("Percentage:", percent, "%")
        if percent > 75:
            print("First Class")
        elif percent > 60:
            print("Second Class")
        elif percent >= 35:
            print("Pass")
        else:
            print("Fail")


obj = C()
obj.fun1()
obj.fun2()
obj.fun3()
