## libraries used to connect ot POSTGRES database
from psycopg2 import Error
from database.db import create_table, getAllStudents, addStudent, updateStudentEmail, deleteStudent, closeDB

if __name__ == "__main__":

    ## connect to the database
    try:
        create_table()

        end = False
        while not end:
            print("\nOptions:")
            print("1: Get all Students")
            print("2: Insert a Student")
            print("3: Update a Student Email")
            print("4: Delete a Student")
            print("0: End Program")
            
            option = input("\nEnter your option: ")

            if option == "1":
                getAllStudents()

            elif option == "2":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

                addStudent(first_name, last_name, email, enrollment_date)

            elif option == "3":
                student_id = input("Enter student id: ")
                email = input("Enter new email: ")

                updateStudentEmail(student_id, email)

            elif option == "4":
                student_id = input("Enter student id: ")

                deleteStudent(student_id)

            elif option == "0":
                end = True
            
            else:
                print("Invalid option. Please try again.")

    ## if error occurs during connection, then print error
    except Error as e:
        print(f"Error: ", e)


    ## once the program is done, close the connection to the database
    finally:
        closeDB()
        print("\nDatabase connection closed.")