class A:
    def sum(self,a,b):
        return a+b;

class B:
    def mul(self,a,b):
        return a*b;

class C(A,B):
    def divide(self,a,b):
        return a/b;

obj = C()
print(obj.sum(10,20))
print(obj.mul(10,7))
print(obj.divide(15,5))