import mysql.connector
import re
from os import system
from getpass import getpass  # For hidden password input
from datetime import date
import datetime

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="employee"
)

# Regular expressions for email and phone validation
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")

def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if(Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    # Instering Employee Details in
    # the Employee (empdata) Table
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()

# Function To Check if Employee With
# given Name Exist or not
def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Name=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function To Check if Employee With
# given Id Exist or not
def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Display_Employ
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    # query to select all rows from Employee (empdata) Table
    sql = 'select * from empdata'
    c = con.cursor()

    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

# Function to Update_Employ
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if(Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        # Updating Employee details in empdata Table
        sql = 'UPDATE empdata set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()

# Function to Promote_Employ
def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        #query to fetch salary of Employee with given data
        sql = 'select Salary from empdata where Id=%s'
        data = (Id,)
        c = con.cursor()
        
        #executing the sql query
        c.execute(sql, data)
        
        #fetching salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
        
        #query to update salary of Employee with given id
        sql = 'update empdata set Salary = %s where Id = %s'
        d = (t, Id)

        #executing the sql query
        c.execute(sql, d)

        #commit() method to make changes in the table 
        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        menu()

# Function to Remove_Employ
def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to delete Employee from empdata table
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)

        #commit() method to make changes in the empdata table
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()
        
# Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to search Employee from empdata table
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        
        #executing the sql query
        c.execute(sql, data)

        #fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()



# ---------------- Sign In and Register Section ----------------

# Function to register a new user
def register():
    print("{:>60}".format("-->> Register New User <<--"))
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")  # Hidden input for security
    confirm_password = getpass("Confirm Password: ")

    # Check if passwords match
    if password != confirm_password:
        print("Passwords do not match! Try again.")
        register()

    # Check if the username already exists
    if check_user(username):
        print("Username already exists! Try again.")
        register()

    # Insert new user into the users table
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    data = (username, password)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Registration successful! Please login.")
    press = input("Press any key to continue..")
    login()

# Function to check if a username exists
def check_user(username):
    sql = "SELECT * FROM users WHERE username=%s"
    data = (username,)
    c = con.cursor(buffered=True)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to login an existing user
def login():
    print("{:>60}".format("-->> User Login <<--"))
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    # Check if the credentials are correct
    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    data = (username, password)
    c = con.cursor(buffered=True)
    c.execute(sql, data)
    r = c.rowcount
    if r == 1:
        print("Login successful!")
        press = input("Press any key to continue..")
        menu()  # Call the menu function to continue with the main application
    else:
        print("Invalid credentials! Try again.")
        press = input("Press any key to continue..")
        login()

# ---------------- Employee Management Section ----------------

# (Your existing employee management functions remain the same)
# Add_Employ, Display_Employ, Update_Employ, Promote_Employ, Remove_Employ, Search_Employ

# ---------------- Main Menu Section ----------------

def main_menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Register")
    print("2. Sign In")
    print("3. Exit")
    print("{:>60}".format("-->> Choice Options: [1/2/3] <<--"))

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        system("cls")
        register()
    elif choice == 2:
        system("cls")
        login()
    elif choice == 3:
        system("cls")
        print("{:>60}".format("Have A Nice Day :)"))
        exit(0)
    else:
        print("Invalid Choice! Try again.")
        press = input("Press Any key To Continue..")
        main_menu()

# ---------------- Employee Management Menu ----------------

def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Mark Attendance")                 # New option to mark attendance
    print("8. View Employee Attendance")        # New option to view individual employee's attendance
    print("9. View Attendance By Date")         # New option to view all attendance by a specific date
    print("10. Logout")
    print("11. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7/8/9/10/11] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        Mark_Attendance()                # Call to mark attendance
    elif ch == 8:
        system("cls")
        View_Attendance()                # Call to view an employee's attendance
    elif ch == 9:
        system("cls")
        View_Attendance_By_Date()        # Call to view attendance by a specific date
    elif ch == 10:
        system("cls")
        main_menu()                      # Log out and go back to the main menu
    elif ch == 11:
        system("cls")
        print("{:>60}".format("Have A Nice Day :)"))
        exit(0)
    else:
        print("Invalid Choice! Try again.")
        press = input("Press Any key To Continue..")
        menu()

def View_Attendance_By_Date():
    print("{:>60}".format("-->> View Attendance By Date <<--"))
    date = input("Enter the Date (YYYY-MM-DD): ")

    # Query to fetch attendance records by a specific date
    sql = 'SELECT * FROM attendance WHERE date = %s'
    data = (date,)
    c = con.cursor()

    # Executing the query
    c.execute(sql, data)
    records = c.fetchall()

    # Display the results
    if records:
        print("Employee ID | Date       | Status")
        print("-" * 30)
        for record in records:
            print(f"{record[0]}        | {record[1]} | {record[2]}")
    else:
        print("No attendance records found for this date.")

    press = input("Press Any key To Continue..")
    menu()
def Mark_Attendance():
    print("{:>60}".format("-->> Mark Employee Attendance <<--"))
    Id = input("Enter Employee Id: ")
    date = datetime.date.today()
    status = input("Enter Status (Present/Absent): ")
    
    # Adjust 'employee_id' to the actual column name in your attendance table
    sql = 'INSERT INTO attendance (employee_id, date, status) VALUES (%s, %s, %s)'
    data = (Id, date, status)
    c = con.cursor()

    # Executing the sql query
    c.execute(sql, data)

    # commit() method to make changes in the attendance table
    con.commit()
    print("Attendance Marked Successfully")
    press = input("Press Any key To Continue..")
    menu()


# Function to view attendance of a specific employee
def View_Attendance():
    print("{:>60}".format("-->> View Employee Attendance <<--"))
    emp_id = input("Enter Employee Id: ")

    # Check if employee exists
    if not check_employee(emp_id):
        print("Employee Record Not Exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
        return

    sql = "SELECT Date, Status FROM attendance WHERE Id = %s ORDER BY Date DESC"
    data = (emp_id,)
    c = con.cursor()
    c.execute(sql, data)
    records = c.fetchall()

    if records:
        for record in records:
            print("Date:", record[0], " | Status:", record[1])
    else:
        print("No attendance records found for this employee.")

    press = input("Press Any Key To Continue..")
    menu()

# Function to view attendance by a specific date
def View_Attendance():
    print("{:>60}".format("-->> View Employee Attendance <<--"))
    Id = input("Enter Employee Id: ")
    
    # Check if 'employee_id' matches the actual column name in the attendance table
    sql = 'SELECT * FROM attendance WHERE employee_id = %s'  # Adjust 'employee_id' to match your actual column name
    data = (Id,)
    c = con.cursor()

    # Executing the sql query
    c.execute(sql, data)

    # Fetching attendance records
    records = c.fetchall()
    if records:
        for record in records:
            print(f"Employee Id: {record[0]}")
            print(f"Date: {record[1]}")
            print(f"Status: {record[2]}")
            print("\n")
    else:
        print("No attendance records found for this employee.")
    
    press = input("Press Any key To Continue..")
    menu()

# Calling the main_menu function to start the program
main_menu()


# Function to mark attendance for an employee
