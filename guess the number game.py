import random
original = random.randint(1,51)
while True:
    print("***Enter Number between 1 to 50 range !!!*****")
    choice = int(input("Enter choice:"))

    if choice>50:
        print("Invalid choice!!")
        break
    elif choice==original:
        print("Win!!")
        break
    elif original>choice:
        print("Original number is greatest!!")
    else:
        print("Original number is smallest!!")