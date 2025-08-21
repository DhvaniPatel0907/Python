from tkintdatabase import *
from tkinter import *
from tkintlogin import *
from tkcalendar import DateEntry

def insert():
    
    name1 = ename.get()
    email1 = eemail.get()
    mobile1 = emobile.get()
    passw = epassword.get()
    cpassword1 = ecpassword.get()
    gender1 = gender_var.get()
    hobbies = []
    if hobby_var.get(): hobbies.append("Reading")
    if hobby_var1.get(): hobbies.append("Writing")
    if hobby_var2.get(): hobbies.append("Drawing")
    if hobby_var3.get(): hobbies.append("Music")
    hobby1 = ", ".join(hobbies)
    DOB1 = edob.get()
 
 
    sql = "INSERT INTO signup_page (name, email, mobile, password, cpassword, gender, hobby, BOD) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name1, email1, mobile1, passw, cpassword1, gender1, hobby1, DOB1)
    mycursor.execute(sql, val)
    mydb.commit()
    print(" insert data successfully!")

def delete():
    emaildel = eemail.get().strip()

    if not emaildel:
        print("Please enter an email to delete.")
        return
    
    mycursor.execute("SELECT * FROM signup_page WHERE email = %s", (emaildel,))
    result = mycursor.fetchone()

    if result:
            mycursor.execute("DELETE FROM signup_page WHERE email = %s", (emaildel,))
            mydb.commit()
            print(f"delete data successfully!")
    else:
            print(f"No record found with email is does not exit...")

def update():
    name1 = ename.get()
    email1 = eemail.get().strip()  
    mobile1 = emobile.get()
    passw = epassword.get()
    cpassword1 = ecpassword.get()
    gender1 = gender_var.get()

    hobbies = []
    if hobby_var.get(): hobbies.append("Reading")
    if hobby_var1.get(): hobbies.append("Writing")
    if hobby_var2.get(): hobbies.append("Drawing")
    if hobby_var3.get(): hobbies.append("Music")
    hobby1 = ", ".join(hobbies)

    DOB1 = edob.get()

    sql = "UPDATE signup_page SET name=%s, mobile=%s, password=%s, cpassword=%s, gender=%s, hobby=%s, BOD=%s WHERE email=%s"
    val = (name1, mobile1, passw, cpassword1, gender1, hobby1, DOB1, email1)

    
    mycursor.execute(sql, val)
    mydb.commit()

    if mycursor.rowcount == 0:
        print("No record found with that email. Update failed.")
    else:
        print("Update data successfully!")

    
root = Tk()

root.geometry("1000x1000")
root.title("Signup From")


name = Label(root,text="Enter Name: ",font=("Arial",12,"bold"))
name.place(x=50,y=50)

email = Label(root,text="Enter email: ",font=("Arial",12,"bold"))
email.place(x=50,y=100)

mobile = Label(root,text="Enter mobile: ",font=("Arial",12,"bold"))
mobile.place(x=50,y=150)

password = Label(root,text="Enter password: ",font=("Arial",12,"bold"))
password.place(x=50,y=200)

cpassword = Label(root,text="Enter cpassword: ",font=("Arial",12,"bold"))
cpassword.place(x=50,y=250)

gender = Label(root,text="Enter a gender: ",font=("Arial",12,"bold"))
gender.place(x=50,y=300)

hobby = Label(root,text="Enter hobby: ",font=("Arial",12,"bold"))
hobby.place(x=50,y=350)

DOB = Label(root,text="Enter DOB: ",font=("Arial",12,"bold"))
DOB.place(x=50,y=400)




ename = Entry(root,bg="yellow")
ename.place(x=240,y=60)

eemail = Entry(root,bg="yellow")
eemail.place(x=240,y=110)

emobile = Entry(root,bg="yellow")
emobile.place(x=240,y=160)

epassword = Entry(root,bg="yellow")
epassword.place(x=240,y=210)

ecpassword = Entry(root,bg="yellow")
ecpassword.place(x=240,y=260)

gender_var=StringVar(value="female")
egender = Radiobutton(root, text='Male', variable=gender_var, value="male" ,font=("Arial",12,"bold"))
egender.place(x=240,y=300)

egender1 = Radiobutton(root, text='Female', variable=gender_var, value="female" ,font=("Arial",12,"bold"))
egender1.place(x=340,y=300)

hobby_var = IntVar()
ehobby = Checkbutton(root, text='Reading',variable=hobby_var,font=("Arial",12,"bold"))
ehobby.place(x=240,y=350)

hobby_var1 = IntVar()
ehobby1 = Checkbutton(root, text='Writing',variable=hobby_var1,font=("Arial",12,"bold"))
ehobby1.place(x=340,y=350)

hobby_var2 = IntVar()
ehobby2 = Checkbutton(root, text='Drawing',variable=hobby_var2,font=("Arial",12,"bold"))
ehobby2.place(x=440,y=350)

hobby_var3 = IntVar()
ehobby3 = Checkbutton(root, text='Music',variable=hobby_var3,font=("Arial",12,"bold"))
ehobby3.place(x=550,y=350)

edob = DateEntry(root, width=12, background='pink', foreground='white', borderwidth=2)
edob.place(x=240,y=400)





insert = Button(root,text="Insert",font=("Arial",16,"italic"),fg="red",command = insert)
insert.place(x=50,y=500)

update = Button(root,text="update",font=("Arial",16,"italic"),fg="red",command = update)
update.place(x=140,y=500)

delete = Button(root,text="Delete",font=("Arial",16,"italic"),fg="red",command=delete)
delete.place(x=240,y=500)

login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red",command=login_screen)
login.place(x=330,y=500)

root.mainloop()
