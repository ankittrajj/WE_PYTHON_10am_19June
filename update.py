import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'kuchbhi')

cursor = con.cursor()

# user input -----> name & age

name = input("Enter your name")
age = int(input("Enter your age"))


query = "update user set age = {} where name = '{}'".format(age,name)

cursor.execute(query)
con.commit()

print("Data update successfully!!")






