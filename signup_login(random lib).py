import random

otp=random.randint(1001,9999)

d = {}
while True:
    menu = """
    press 1 for signup
    press 2 for login
    press 3 for forget password
    press 4 for exit

"""
    print(menu)
    choice = int(input("Enter Choice:"))

    if choice==1:
        print("*******Welcome to signup!*******")
        name=input("Enter name:")
        email=input("Enter email:")
        mobile=int(input("Enter Mobile:"))
        password=int(input("Enter Password:"))
        cpassword=int(input("Enter cpasssword:"))

        if password==cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("Sign Up successfully!!")

        else:
            print("Password & confirm password does not match!")

    elif choice ==2:
        print("*********Welcome to Log in!!*********")
        email=input("Enter Email:")
        password=int(input("Enter Password:"))

        if d['email']==email:
            if d['password']==password:
                print("Log in Successfully!!")

            else:
                print("Password does not match")

        else:
            print("Email dose not match!!")

    elif choice==3:
        print("********Welcome to forget password*******")
        mobile=int(input("Enter Mobile:"))

        if d['mobile']==mobile:
            print("Your otp is:",otp)

            uotp=int(input("Enter otp:"))

            if otp==uotp:
                password=int(input("Enter a Password:"))
                d['password']=password
                print("Password Update Succesfully") 

            else:
                print("Invalid OTP:")
        else:
            print("Mobile Number does not match")

    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice") 
        break     