import math

while True:
    menu = """
    press 1 for function without parameter and without return type
    press 2 for function with parameter and without return type
    press 3 for function without parameter and with return type
    press 4 for function with parameter and with return type
    press 5 for exit
    """
    print(menu)
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # 1. Without parameter, without return type
    if choice == 1:
        def fac():
            n = int(input("Enter a number: "))
            print(math.factorial(n))
        fac()

    # 2. With parameter, without return type
    elif choice == 2:
        def fac(n):
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print(fact)
        try:
            num = int(input("Enter a number: "))
            fac(num)
        except ValueError:
            print("Invalid number.")

    # 3. Without parameter, with return type
    elif choice == 3:
        def fun1():
            n = int(input("Enter a number: "))
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact
        print(fun1())

    # 4. With parameter, with return type
    elif choice == 4:
        def factorial(n):
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            return fact
        try:
            num = int(input("Enter a number: "))
            print(factorial(num))
        except ValueError:
            print("Invalid number.")

    # 5. Exit
    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid choice!! Please try again.")
