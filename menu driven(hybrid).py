class Myclass1:
    def fun1(self):
        n = int(input("Enter a number: "))
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        print("Factorial:", fac)


class Myclass2(Myclass1):
    def fun2(self):
        n = int(input("Enter a number: "))
        if n < 2:
            print(n, "is Not Prime")
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    print(n, "is Not Prime")
                    break
            else:
                print(n, "is Prime")


class Myclass3:
    def fun3(self):
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")


class Myclass4(Myclass2, Myclass3):
    def fun4(self):
        n = int(input("Enter a number: "))
        if n > 0:
            print("The number is Positive.")
        elif n < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")


obj = Myclass4()

while True:
    menu = """
    
    press 1 for Factorial
    press 2 for Prime 
    press 3 for Even/Odd
    press 4 for Positive/Negative/Zero
    press 5 for Exit
    
    """
    print(menu)

    choice = int(input("Enter your choice: "))
    

    if choice == 1:
        obj.fun1()
    elif choice == 2:
        obj.fun2()
    elif choice == 3:
        obj.fun3()
    elif choice == 4:
        obj.fun4()
    elif choice == 5:
        print("Thank you! Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
