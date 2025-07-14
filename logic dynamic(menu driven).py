while True:
    menu = """
    press 1 for Square
    press 2 for merge dictionary
    press 3 for merge list into dictionary
    press 4 for exit
    """
    print(menu)
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("******* Welcome to Square *******")
        n = int(input("Enter a number: "))
        d = {}
        for i in range(1, n + 1):
            d[i] = i * i
        print("Squares:", d)

    elif choice == 2:
        print("******* Welcome to Merge Dictionary *******")
        d1 = {}
        n1 = int(input("How many items in dictionary 1? "))
        for i in range(n1):
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            d1[key] = value

        d2 = {}
        n2 = int(input("How many items in dictionary 2? "))
        for i in range(n2):
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            d2[key] = value

        ans = {}
        for key in d1:
            if key in d2:
                ans[key] = d1[key] + d2[key]

        print("Merged dictionary with common keys added:", ans)

    elif choice == 3:
        print("******* Merge Lists into Dictionary *******")
        l = []
        l1 = []

        n = int(input("Enter number of elements in both lists: "))
        print("Enter elements for first list:")
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            l.append(val)

        print("Enter elements for second list:")
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            l1.append(val)

        ans = {}
        for i in range(n):
            ans[l[i]] = l1[i]

        print("Mapped Dictionary:", ans)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
