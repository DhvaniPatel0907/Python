from pymysql import *

mydb = connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists Inventory")
mydb.commit()

mydb = connect(host="localhost",user="root",password="",database="Inventory")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists data(id int primary key auto_increment,name varchar(100),price decimal(10,2) not null,quantity int not null)")
mydb.commit()
