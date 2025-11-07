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

    ## set the cursor to do datatbase operations
    cursor = connection.cursor()

## if error occurs during the database connection, we would print the error
except Error as e:
    connection = None
    cursor = None
    print("Error connecting to the database", e)

## this function would create the students table in the database if it doesnt already exist, and then
## insert the intial data into the table using our addStudent function
def create_table():
    if connection:
        create_table_query = "CREATE TABLE IF NOT EXISTS students " \
            "(student_id SERIAL PRIMARY KEY, " \
            "first_name VARCHAR(255) NOT NULL, " \
            "last_name VARCHAR(255) NOT NULL, " \
            "email VARCHAR(255) UNIQUE NOT NULL, " \
            "enrollment_date DATE);"
        cursor.execute(create_table_query)

        ## insert inital data to the database using our addStudent function that we created
        addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
        addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
        addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

        connection.commit()

def getAllStudents():
    if connection:
        cursor.execute("SELECT * FROM students")
        tuples = cursor.fetchall()
        print(*tuples, sep="\n")

def addStudent(first_name, last_name, email, enrollment_date):
    if connection:
        add_student_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        student_data = (first_name, last_name, email, enrollment_date)
        cursor.execute(add_student_query, student_data)
        connection.commit()

def updateStudentEmail(student_id, new_email):
    if connection:
        update_student_email_query = "UPDATE students SET email = %s WHERE students.student_id = %s;"
        cursor.execute(update_student_email_query, (new_email, student_id))
        connection.commit()

def deleteStudent(student_id):
    if connection:
        delete_student_query = "DELETE FROM students WHERE students.student_id = %s;"
        cursor.execute(delete_student_query, (student_id,))
        connection.commit()

def closeDB():
    if connection:
        drop_students_table_query = "DROP TABLE IF EXISTS students;"
        cursor.execute(drop_students_table_query)
        connection.commit()

        cursor.close()
        connection.close()