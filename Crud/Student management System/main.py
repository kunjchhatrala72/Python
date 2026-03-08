from crud import *

while True:

    print("\nStudent Management System")
    print("1 Add Student")
    print("2 View Students")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")
    
    choice = input("Enter choice : ")
    
    
    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")

        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        id = int(input("Student ID: "))
        name = input("New Name: ")

        update_student(id, name)

    elif choice == "4":
        id = int(input("Student ID: "))
        delet_student(id)

    elif choice == "5":
        break