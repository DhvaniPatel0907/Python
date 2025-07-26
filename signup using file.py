import random

otp = random.randint(1001, 9999)

while True:
    menu = """
    Press 1 for Signup
    Press 2 for Exit
    """
    print(menu)
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("******* Welcome to Signup! *******")
        name = input("Enter name: ")
        email = input("Enter email: ")
        mobile = input("Enter mobile: ")
        password = input("Enter password: ")
        cpassword = input("Enter confirm password: ")

        if password == cpassword:
            # Save data to file
            file = open("signup.txt", "a")  # 'a' for append mode
            file.write(f"{name},{email},{mobile},{password}\n")
            file.close()
            print("Sign Up successfully!!")
        else:
            print("Password & confirm password do not match!")

    elif choice == 2:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
        break
