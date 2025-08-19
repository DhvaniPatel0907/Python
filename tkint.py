from tkinter import *
from tkcalendar import DateEntry
from tkintlogin import *



root = Tk()

root.geometry("1000x1000")
root.title("Signup Form")

name = Label(root,text="Enter Name",font=("Arial",12,"bold"))
name.place(x=50,y=50)

email = Label(root,text="Enter Email",font=("Arial",12,"bold"))
email.place(x=50,y=100)

mobile = Label(root,text="Enter Mobile",font=("Arial",12,"bold"))
mobile.place(x=50,y=150)

password = Label(root,text="Enter Password",font=("Arial",12,"bold"))
password.place(x=50,y=200)

cpassword = Label(root,text="Confirm Password",font=("Arial",12,"bold"))
cpassword.place(x=50,y=250)

gender=Label(root,text="Gender",font=("Arial",12,"bold"))
gender.place(x=50,y=300)

gender_var = StringVar(value="Male")
male_radio=Radiobutton(root,text="Male", variable=gender_var,value="Male",font=("Arial",12,"bold"))
male_radio.place(x=240,y=300)

female_radio=Radiobutton(root,text="Female", variable=gender_var,value="Female",font=("Arial",12,"bold"))
female_radio.place(x=310,y=300)

other_radio=Radiobutton(root,text="Other", variable=gender_var,value="Other",font=("Arial",12,"bold"))
other_radio.place(x=400,y=300)

hobby=Label(root,text="Hobbies",font=("Arial",12,"bold"))
hobby.place(x=50,y=350)

hobby_badminton = Checkbutton(root,text="Cricket",font=("Arial",10,"bold"))
hobby_badminton.place(x=240,y=350)

hobby_music = Checkbutton(root,text="Music",font=("Arial",10,"bold"))
hobby_music.place(x=310,y=350)

hobby_travelling = Checkbutton(root,text="Travelling",font=("Arial",10,"bold"))
hobby_travelling.place(x=380,y=350)

Dob = Label(root,text="DOB",font=("Arial",12,"bold"))
Dob.place(x=50,y=400)

dob = DateEntry(root, width=18, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
dob.place(x=240, y=400)

Time = Label(root,text="Time",font=("Arial",12,"bold"))
Time.place(x=50,y=240)

hour = Spinbox(root, from_=0, to=23, width=5, font=("Arial", 12))
hour.place(x=240, y=450)

minute = Spinbox(root, from_=0, to=59, width=5, font=("Arial", 12))
minute.place(x=300, y=450)

second = Spinbox(root, from_=0, to=59, width=5, font=("Arial", 12))
second.place(x=360, y=450)

ename=Entry(root,bg="yellow")
ename.place(x=240,y=60)

eemail=Entry(root,bg="yellow")
eemail.place(x=240,y=110)

emobile=Entry(root,bg="yellow")
emobile.place(x=240,y=160)

epassword=Entry(root,bg="yellow")
epassword.place(x=240,y=210)

ecpassword=Entry(root,bg ="yellow")
ecpassword.place(x=240,y=260)


insert = Button(root,text="Insert",font=("Arial",16,"italic"),fg="red")
insert.place(x=50,y=550)

update = Button(root,text="Update",font=("Arial",16,"italic"),fg="red")
update.place(x=140,y=550)

delete = Button(root,text="Delete",font=("Arial",16,"italic"),fg="red")
delete.place(x=240,y=550)

login = Button(root,text="Login",font=("Arial",16,"italic"),fg="red",command=login_screen)
login.place(x=330,y=550)

root.mainloop()
