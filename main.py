# SCHOOL MANAGEMENT SYSTEM (COMMAND LINE)

# Import needed packages
import time # INBULIT
import sqlite3 # INBULIT

# dependencies
import admin

# CREATING DATABASE AND TABLES
def DB():
    global conn
    global c
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()

    # Create table
    # c.execute('''CREATE TABLE users
    #             (name text, password text, priveledge text, id integer)''')


def teachers_session():
    while True:
        print("\nTeacher Menu")
        print("1. Create a classroom")
        print("2. Register a new student")
        print("3. End a classroom")
        print("4. Logout\n")
        user_option4 = input("OPTION :")

        if user_option4 == "1":
            print("\nCreate a classroom")
        elif user_option4 == "2":
            username = input("\nEnter Username For New Student :")
            password = input("Enter Password For New Student :")
            query_vals = (username, password)
            c.execute("INSERT INTO users (name,password,priveledge) VALUES (?,?,'student')",query_vals)
            conn.commit()
        elif user_option4 == "3":
            print("\nEND A CLASSROOM")
        elif user_option4 == "4":
            print("\nLOGOUT")
            break
        else:
            print("\nINVALID OPTION")


def teachers_auth():
    print("\nTeachers Login")
    username = input("\nUSERNAME :")
    password = input("PASSWORD :")
    t = (username,'teacher')
    c.execute('SELECT password FROM users WHERE name=? AND priveledge=?',t)
    passcode = str(c.fetchone())
    # passw = "('" password + "',)"
    passw = password
    # print(passw)
    # print(passcode[2:-3])
    if passcode[2:-3] == passw:
        print("\nLogin to teachers account successfull")
        teachers_session()
    else:

        print(username,"ACCOUNT NOT FOUND\n")
        time.sleep(3)
    

def students_session():
    while True:
        print("\nStudent Menu")
        print("1. Create a classroom")
        print("2. Leave Classroom")
        print("3. End a club")
        print("4. Logout\n")
        user_option3 = input("OPTION :")

        if user_option3 == "1":
            print("\nCreate a Club")
        elif user_option3 == "2":
            print("\nLeave Classroom")
        elif user_option3 == "3":
            print("\nEnd a club")
        elif user_option3 == "4":
            break
        else:
            print("\nINVALID OPTION")



def students_auth():
    print("\nStudents Login")
    username = input("\nUSERNAME :")
    password = input("PASSWORD :")
    t = (username,'student')
    c.execute('SELECT password FROM users WHERE name=? AND priveledge=?',t)
    passcode = str(c.fetchone())
    # passw = "('" password + "',)"
    passw = password
    # print(passw)
    # print(passcode[2:-3])
    if passcode[2:-3] == passw:
        print("\nLogin to students account successfull")
        students_session()
    else:

        print(username,"ACCOUNT NOT FOUND\n")
        time.sleep(3)



def main():
    while True:
        print("Welcome to School management system\n")
        print("1. Login as admin ")
        print("2. Login as teacher ")
        print("3. Login as student ")
        print("4. Exit")

        user_option = input("\nOPTION :")
        if user_option == "1":
            print("\nAdmin Login")
            admin.admin_auth()
        elif user_option == "2":
            teachers_auth()
        elif user_option == "3":
            students_auth()
        elif user_option == "4":
            print("Shutting Down...")
            time.sleep(3)
            exit()
        else:
            print("Invalid option")

DB()
main()
