class Myclass:
    def fun1(self): #method
        l = [1,2,3,4,5,6,7,1,2]
        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)
        print(l1)

    def fun2(self):
        d={}
        for i in range(1,31):
            d[i]=i*i
        print(d)

    def fun3(self,a,b):
        print("Addition:",a+b)

obj = Myclass()    #creation of object
obj.fun1()
obj.fun2()
obj.fun3(10,20)