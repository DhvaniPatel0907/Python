import pymysql

mydb = pymysql.connect(host="localhost" ,user="root" ,password="")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS think_singup")
mydb.commit()

mydb = pymysql.connect(host="localhost" ,user="root" ,password="" ,database="think_singup")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists signup_page(id INT PRIMARY KEY AUTO_INCREMENT ,name varchar(100),email varchar(100),mobile bigint,password varchar(30),cpassword varchar(30),gender varchar(20),hobby varchar(20),BOD DATE )")
mydb.commit()

