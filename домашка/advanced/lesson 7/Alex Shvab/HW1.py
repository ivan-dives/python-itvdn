import sqlite3
import smtplib


# conn = sqlite3.connect("usersdb.sqlite3")
#
# conn.execute('CREATE TABLE "users"(id INTEGER PRIMARY KEY, surname VARCHAR(20) , his_name VARCHAR(20) , second_name VARCHAR(20), birthday )')
# conn.execute(
#     """INSERT INTO users(surname, his_name, second_name, birthday)
#        VALUES ('Petrov', 'Ihor', 'Serheevich', '10/02/1956'),
#               ('Vodkin', 'Stepan', 'Ihorevich', '22/09/1973'),
#               ('Krysin', 'Dmitriy', 'Alexseevich', '16/11/1995')
#     """
# )
#
# conn.commit()
# conn.close()

class User():
    def get_full_name(self):
        conn = sqlite3.connect("usersdb.sqlite3")
        cur = conn.execute('SELECT surname, his_name, second_name FROM "users"')
        while True:
            row = cur.fetchone()

            if row == None:
                break
            print(f"{row[0]} {row[1]} {row[2]}")


    def get_age(self):
        conn = sqlite3.connect("usersdb.sqlite3")
        cur = conn.execute('SELECT birthday FROM "users"')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print(f"{row}")


    def __str__(self):
        conn = sqlite3.connect("usersdb.sqlite3")
        cur = conn.execute('SELECT * FROM "users"')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print(f"{row}")

    def new_user(self):
        conn = sqlite3.connect("usersdb.sqlite3")
        surname = input("Enter surname: ")
        name = input("Enter name: ")
        second_name = input("Enter second_name: ")
        birthday = input("Enter birthday: ")
        conn.execute(
                 """INSERT INTO users(surname, his_name, second_name, birthday)
                    VALUES (?, ?, ?, ?)
                 """, (surname, name, second_name, birthday)
             )

            

u = User()
u.get_full_name()
u.__str__()
