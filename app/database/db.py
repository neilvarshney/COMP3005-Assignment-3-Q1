## libraries used to connect to POSTGRES database
import psycopg2
from psycopg2 import Error

## connect to the database with our database credentials
try:
    ## you would have to enter your own credentials here to connect to your own database
    connection = psycopg2.connect(
        user="postgres",
        password="SQL",
        host="localhost",
        port="5432",
        database="COMP3005_A3"
    )

    ## set the cursor to do database operations
    cursor = connection.cursor()

## if error occurs during the database connection, we would print the error
except Error as e:
    connection = None
    cursor = None
    print("Error connecting to the database", e)

## this function would create the students table in the database if it doesnt already exist, and then
## insert the initial data into the table using our addStudent function
def create_table():
    if connection:
        create_table_query = "CREATE TABLE IF NOT EXISTS students " \
            "(student_id SERIAL PRIMARY KEY, " \
            "first_name VARCHAR(255) NOT NULL, " \
            "last_name VARCHAR(255) NOT NULL, " \
            "email VARCHAR(255) UNIQUE NOT NULL, " \
            "enrollment_date DATE);"
        cursor.execute(create_table_query)

        ## insert initial data to the database using our addStudent function that we created
        addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
        addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
        addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

        connection.commit()

## this function will get all records/tuples from the students table and print them to the terminal
def getAllStudents():
    if connection:
        try:
            cursor.execute("SELECT * FROM students")

            ## fectchall() reads all the tuples from the SELECT query and returns as a list of tuples
            tuples = cursor.fetchall()

            ## this reads that list and prints each tuple seperately
            print(*tuples, sep="\n")

        except Error as e:
            ## connection.rollback() cancels all changes made in the current transaction and resets the connection to a clean state.
            connection.rollback()
            print(f"\nError getting all students: {e}")

## this function will add a new student to the students table with the given parameters
def addStudent(first_name, last_name, email, enrollment_date):
    if connection:
        try:
            add_student_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
            student_data = (first_name, last_name, email, enrollment_date)

            cursor.execute(add_student_query, student_data)
            connection.commit()

            print(f"\nStudent {first_name} {last_name} added successfully.")

        ## if error occurs, like invalid type of data or duplicate email, then print the error message
        except Error as e:
            connection.rollback()
            print(f"\nError adding student: {e}")

## this function will update the email of a student with the given student_id if the student exists.
def updateStudentEmail(student_id, new_email):
    if connection:
        try:
            # Check if student exists
            student_exists_query = "SELECT student_id FROM students WHERE student_id = %s"
            cursor.execute(student_exists_query, (student_id,))
            student = cursor.fetchone()

            ## if student exists, then update the email by executing the update query
            if student:
                update_student_email_query = "UPDATE students SET email = %s WHERE student_id = %s;"
                cursor.execute(update_student_email_query, (new_email, student_id))
                connection.commit()
                print(f"\nEmail updated successfully for student ID {student_id}")

            else:
                print(f"\nStudent with ID {student_id} not found.")

        except Error as e:
            connection.rollback()
            print(f"\nError updating email: {e}")

## this function will delete a student from the students table with the given student_id
def deleteStudent(student_id):
    if connection:
        try:
            # Check if student exists
            student_exists_query = "SELECT student_id FROM students WHERE student_id = %s"
            cursor.execute(student_exists_query, (student_id,))
            student = cursor.fetchone()

            ## if student exists, then execute the delete query to remove the student from the table
            if student:
                delete_student_query = "DELETE FROM students WHERE students.student_id = %s;"
                cursor.execute(delete_student_query, (student_id,))
                connection.commit()

                print(f"\nStudent with ID {student_id} deleted successfully.")
                
            else:
                print(f"\nStudent with ID {student_id} not found.")
        
        except Error as e:
            connection.rollback()
            print(f"\nError deleting student: {e}")

## this function will DROP the students table (so for the next run we have a "fresh" table) and close the database 
# connection and cursor
def closeDB():
    if connection:
        ## try to drop the students table if it exists
        try:
            drop_students_table_query = "DROP TABLE IF EXISTS students;"
            cursor.execute(drop_students_table_query)
            connection.commit()

        ## if error occurs then print the error message
        except Error as e:
            connection.rollback()
            print(f"\nError dropping table: {e}")
        
        ## close the cursor and connection to the database
        cursor.close()
        connection.close()