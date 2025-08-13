from pymysql import *

mydb = connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists signup")
mydb.commit()

mydb = connect(host="localhost",user="root",password="",database="signup")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists data(id int primary key auto_increment,name varchar(100),subject varchar(40))")
mydb.commit()
