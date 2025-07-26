from diffclass1 import *
obj1 = Prime()
obj2 = Pattern()
obj3 = Table()
obj4 = Mid()
while True:
    menu = """
     Press 1 for Prime Number
     Press 2 for Pattern
     Press 3 for Table
     Press 4 for Mid
     Press 5 for Exit
"""
    print(menu)

    choice = int(input("Enter a Choice:"))
    if choice == 1:
        obj1.prime()

    elif choice==2:
        obj2.pattern()

    elif choice==3:
        obj3.table()

    elif choice==4:
        s=input("Enter a Name:")
        print(obj4.mid(s))

    elif choice==5:
        print("Thank You")
        break

    else:
        print("Invalid Choice!")
        break