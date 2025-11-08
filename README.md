# Program Description:
A Simple command line interface application that allows a user to manage a students table in PostgreSQL. The porgram will connect to the database on the PostgreSQL server with the user credentials, create the table, insert intial data, and allow the user to display the tuples, add a student, change a student's email, or delete a student

# Steps to Run
1. Clone the directory
2. In the app/database/db.py file, enter your PostgreSQL credentails to connect to your database. Ensure the database named in the db.py file exists in your server
3. Install the dependency: pip install psycopg2-binary
4. In the terminal, in the /app/ directory, type python app.py to run the program
5. Type 0 to end the program.