class Myclass:
    def fun1(self):
        n = int(input("enter a number:"))
        for i in range (1,n+1):
            if(n%2==0):
                print("Even")
            else:
                print("Odd")

class Myclass2:
    def fun2(self):
     marks = int(input("Enter your marks (0 to 100): "))

     if marks >= 90 and marks <= 100:
      print("Grade: A")
     elif marks >= 80:
       print("Grade: B")
     elif marks >= 70:
       print("Grade: C")
     elif marks >= 60:
       print("Grade: D")
     elif marks >= 0:
      print("Grade: Fail")
     else:
      print("Invalid input! Marks should be between 0 and 100.")


class Myclass3(Myclass,Myclass2):
    def fun3(self):
      n = int(input("Enter a Number:"))
      if n<0:
       print("Enter Positive Number")
      else:
       if n==1 or n==3 :
        print("Prime")
       else:
        prime=0
        for i in range (1,n+1):
            if(n%i==0):
                prime+=1
        if prime==2:
                print(n,"Is Prime")
        else:
                print(n,"Is Not Prime")

obj = Myclass3()
obj.fun1()
obj.fun2()
obj.fun3()