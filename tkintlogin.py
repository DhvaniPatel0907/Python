from tkinter import *
def login_screen():
    root = Tk()
    root.geometry("500x500")
    root.title("Login Form")

    email = Label(root,text="Enter Email",font=("Arial",12,"bold"))
    email.place(x=100,y=80)

    eemail = Entry(root,bg="yellow")
    eemail.place(x=240,y=90)

    password = Label(root,text="Enter Password",font=("Arial",12,"bold"))
    password.place(x=100,y=130)

    epassword=Entry(root,bg="yellow")
    epassword.place(x=240,y=140)

    login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red")
    login.place(x=250,y=200)

    root.mainloop()