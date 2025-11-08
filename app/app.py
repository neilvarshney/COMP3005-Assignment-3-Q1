## libraries used to show database errors
from psycopg2 import Error

## import the database functions from db.py (which is a package inside the database folder)
from database.db import create_table, getAllStudents, addStudent, updateStudentEmail, deleteStudent, closeDB

## this is the main function of the app. this will run the main functionality of the program
if __name__ == "__main__":

    try:
        ## connect to the database and create the table
        create_table()

        ## main loop to show options to the user, the U.I
        end = False
        while not end:
            print("\nOptions:")
            print("1: Get all Students")
            print("2: Insert a Student")
            print("3: Update a Student Email")
            print("4: Delete a Student")
            print("0: End Program")
            
            option = input("\nEnter your option: ")

            ## option 1, to get all students
            if option == "1":
                getAllStudents()

            
            ## option 2, to add a student
            elif option == "2":
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

                addStudent(first_name, last_name, email, enrollment_date)

            ## option 3, change email of a student
            elif option == "3":
                student_id = input("Enter student id: ")
                email = input("Enter new email: ")

                updateStudentEmail(student_id, email)

            ## option 4, delete a student
            elif option == "4":
                student_id = input("Enter student id: ")

                deleteStudent(student_id)

            ## option 0, to end the program
            elif option == "0":
                end = True
            
            ## invalid option chosen, print error message
            else:
                print("Invalid option. Please try again.")

    ## if error occurs during connection, then print error
    except Error as e:
        print(f"Error: {e}")


    ## once the program is done, close the connection to the database
    finally:
        closeDB()
        print("\nDatabase connection closed.")