# SCHOOL MANAGEMENT SYSTEM (COMMAND LINE) - Admin

# Import needed packages
import time # INBULIT
import sqlite3 # INBULIT

# Import Dependencies

# CREATING DATABASE AND TABLES

conn = sqlite3.connect('Database.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE users
#             (name text, password text, priveledge text, id integer)''')



# Defining functions

# FOR TEACHERS
def delete_teacher(name):
    query_vals = (name,'teacher')
    c.execute("DELETE FROM users WHERE name = ? AND priveledge = ?",query_vals)
    conn.commit()
    if c.rowcount < 1:
        print("USER NOT FOUND")
    else:
        print(name," Deleted successfully\n")

def register_teacher(name, password):
    query_vals = (name, password)

    # Insert a row of data
    c.execute("INSERT INTO users (name,password,priveledge) VALUES (?,?,'teacher')",query_vals)

    # Save (commit) the changes
    conn.commit()

# FOR STUDENTS
def delete_student(name):
    query_vals = (name,'student')
    c.execute("DELETE FROM users WHERE name = ? AND priveledge = ?",query_vals)
    conn.commit()
    if c.rowcount < 1:
        print("USER NOT FOUND")
    else:
        print(name," Deleted successfully\n")

def register_student(name, password):
    query_vals = (name, password)

    # Insert a row of data
    c.execute("INSERT INTO users (name,password,priveledge) VALUES (?,?,'student')",query_vals)

    # Save (commit) the changes
    conn.commit()

def admin_session():
    print("\nAdmin Login was successfull")
    print("Welcome Admin!\n")
    while True:
        time.sleep(3)
        print("Admin Menu")
        print("1. Register New Student")
        print("2. Delete Existing Student Account")
        print("3. Register New Teacher")
        print("4. Delete Existing Teacher Account")
        print("5. Users")
        print("6. Logout\n")

        user_option2 = input("OPTION :")
        if user_option2 == "1":
            print("Register New Student")
            name = input("Students Name :")
            password = input("Password :")
            time.sleep(3)
            register_student(name,password)
            print(name," Registered successfully as Student\n")

        elif user_option2 == "2":
            print("Delete Existing Student Account")
            name = input("Students Name :")
            # password = input("Password :")
            priveledge = "student"
            time.sleep(3)
            delete_student(name)

        elif user_option2 == "3":
            print("Register New Teacher")
            name = input("Teachers Name :")
            password = input("Password :")
            time.sleep(3)
            register_teacher(name,password)
            print(name," Registered successfully as Teacher\n")

        elif user_option2 == "4":
            print("Delete Existing Teacher Account")
            name = input("Teachers Name :")
            # password = input("Password :")
            priveledge = "teacher"
            time.sleep(3)
            delete_teacher(name)
            

        elif user_option2 == "5":
            print("\nUsers\n")
            for row in c.execute('SELECT * FROM users ORDER BY name'):
                print(row)
                print("")

        elif user_option2 == "6":
            print("Logout")
            print("")
            print("Logged Out")
            break
        else:
            time.sleep(3)
            print("INVALID OPTION\n")


def admin_auth():
    username = input("\nUSERNAME :")
    password = input("PASSWORD :")

    if username == "Admin":
        if password  == "Administration":
            admin_session()     
        else:
            print("\nINCORRECT PASSWORD\n")
            time.sleep(2)
    else:
        print("\nINVALID USERNAME\n")
        time.sleep()