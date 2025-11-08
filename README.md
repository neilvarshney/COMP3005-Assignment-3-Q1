# Program Description:
A simple command line interface application that allows a user to manage a students table in PostgreSQL. The program will connect to the database on the PostgreSQL server with the user credentials, create the table, and insert initial data. This program will allow the user to display all records in the table, add a student, change a student's email, or delete a student record.

# Functions:
- `getAllStudents()`: Retrieves and displays all student records from the database
- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the database
- `updateStudentEmail(student_id, new_email)`: Updates the email address of an existing student
- `deleteStudent(student_id)`: Removes a student record from the database

# Steps to Run
1. Clone the directory
2. In the app/database/db.py file, enter your PostgreSQL credentials to connect to your database. Ensure the database named in the db.py file exists in your server
3. Install the dependency: 
`pip install psycopg2-binary`
4. In the terminal, in the /app/ directory, type the following to run the program: `python app.py`
5. Type 0 to end the program.

# Video Demonstration
Here is the link to watch a video demonstration on this program: [Demo Video](https://www.youtube.com/watch?v=TRJx8k6izJ8)