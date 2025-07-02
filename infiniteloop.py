while True:
    menu = """
    press 1 for prime number
    press 2 for Pyramid
    press 3 for factorial
    press 4 for exit
"""
    print(menu)
    choice = int(input("Enter Your choice:"))

    if choice==1:
        n = int(input("Enter a Number:"))
        if n<0:
          print("Enter Positive Number")
        else:
             if n==1 or n==3 or n==2 :
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
    elif choice==2:
       for i in range (1,6):
         print(" "*(6-i)," *"*i)


    elif choice==3:
       n=int(input("Enter a Number:"))
       fac=1
       i=1

       while(i<=n):
        fac*=i
        i=i+1
       print(fac)

    elif choice==4:
      print("Thank You")
      break

    else:
      print("Invalid choice!!")
      break

    
       

        
