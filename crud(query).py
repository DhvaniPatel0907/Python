from crud import *

mydb = connect(host="localhost",user="root",password="",database="signup")
mycursor = mydb.cursor()

while True:
    menu = """

     press 1 for Insert Data
     press 2 for Update Data
     press 3 for Delete Data
     press 4 for Fetch Data
     press 5 for Exit
"""

    print(menu)

    choice = int(input("Enter a Choice:"))
    if choice == 1:
        name = input("Enter a Name:")
        subject = input("Enter a Subject:")

        query = "insert into data (name,subject) value('%s','%s')"
        args = (name,subject)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted Successfully!!")


    elif choice == 2:
        id = int(input("Enter a ID:"))
        name = input("Enter a Name:")
        subject = input("Enter a Subject:")

        query = "update data set name='%s' , subject='%s' where id = '%s'"
        args = (name,subject,id)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Updated Successfully!!")


    elif choice == 3:
        id = int(input("Enter ID:"))
        query = "delete from data where id = '%s'"
        args = (id)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted Successfully!!")

    elif choice == 4:
        query = "select * from data"
        mycursor.execute(query)
        mydata = mycursor.fetchall()
        print(mydata)


    elif choice == 5:
        print("Thank You so much!!")
        break
    elif choice == 6:
        print("Invalid choice")
        break
    
