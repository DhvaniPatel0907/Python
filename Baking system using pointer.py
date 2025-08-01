import random
ac_no=random.randint(100000000001,999999999999)
password=random.randint(1001,9999)

class Bank:
    def ac_register(self):
        name=input("Enter Your Name:")
        email=input("Enter Your Email:")
        mobile=int(input("Enter your Mobile No.:"))
        balance = 5000

        self.balance=balance
        self.name=name
        print("Your Account Number is:",ac_no)
        print("Your Password is:",password)

    def deposit(self):
        damount = int(input("Enter Your Deposit:"))
        print("Your Deposit is",damount)
        self.balance+=damount
    def withdraw(self):
        wamount = int(input("Enter Withdraw Amount:"))
        print("Your Withdraw Amount is:",wamount)

        if wamount>self.balance:
            print("Invalid Amount!")

        else:
            self.balance=wamount

    def check_balance(self):
        print(f"{self.name}Your Account balance is{self.balance}")
obj = Bank()
print("Press 1 for Create Account")
print("Press 2 for Exit")

choice=int(input("Enter Your Choice:"))
if choice==1:
    obj.ac_register()

    while True:
        menu = """
        Press 1 for Deposit Amount
        Press 2 for withdraw Amount
        Press 3 for Checkbalance
        Press 4 for Exit


        """
        print(menu)
        choice1=int(input("Enter Choice:"))

        if choice1==1:
            obj.deposit()
        elif choice1==2:
            obj.withdraw()
        elif choice1==3:
            obj.check_balance()
        elif choice1==4:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")
            break