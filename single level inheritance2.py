class A:
    def fun1(self):
     n = int(input("Enter a Number:"))
     fac=1
     i=1

     for i in range (1,n+1):
      fac*=i

     print(fac)

    def fun2(self):
     d1 = {'p': 1100, 'q': 300, 'r': 600}
     d2 = {'p': 400, 'q': 200}
     ans = {}
     for i,j in d1.items():
      for k,l in d2.items():
        if i == k:
            ans[i]=j+l
      print(ans)

class B(A):
   def fun3(self):
    s = "Python is Programming Langugage"
    print(len(s))
    print(s[0:6:1])
    print(s[:18:3])
    print(s[5: :4])
    print(s[6:14:2])
    print(s[16:28:3])

obj=B()
obj.fun1()
obj.fun2()
obj.fun3()
