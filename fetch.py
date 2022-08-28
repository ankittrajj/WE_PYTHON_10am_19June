import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'kuchbhi')

cursor = con.cursor()

# user input -----> name & age
#
# name = input("Enter your name")
# age = int(input("Enter your age"))


query = "select * from user"

cursor.execute(query)

# data = cursor.fetchone()
# data1 = cursor.fetchmany(3)
data2 = cursor.fetchall()
print(data2)

# print("Data insert successfully!!")






