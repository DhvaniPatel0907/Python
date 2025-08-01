class Myname:
    def myname(self):
        print("Method 1!!")

class Myname2(Myname):
    def myname(self):
        super().myname()
        print("Method 2!!")

obj=Myname2()
obj.myname()