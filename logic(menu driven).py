

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
       print("******* Welcome to merge  dictionary****")
       d1 = {'p': 1100, 'q': 300, 'r': 600}
       d2 = {'p': 400, 'q': 200}
       ans = {}
       for i,j in d1.items():
              for k,l in d2.items():
                    if i == k:
                      ans[i]=j+l
       print(ans)


    elif choice == 3:
        print("******* Merge Lists into Dictionary *******")
        l = [16, 62, 24]
        l1 = [32, 89, 62]
        ans = {}
        for i in range(len(l)):
             ans[l[i]] = l1[i]

        print(ans)


    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
