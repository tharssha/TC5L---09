from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    

# Initialize the database
init_sqlite_db()

# Home route (login)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (email, password) VALUES (?, ?)", (email, password))
            con.commit()
            return "Login successful"
    return render_template('login.html')

# Registration route (sign-up)
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        student_id = request.form['student_id']
        email = request.form['email']
        age = request.form['age']
        faculty = request.form['faculty']
        phone_number = request.form['phone_number']
        password = request.form['password']

        # Save sign-up data to database
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('''
                INSERT INTO students_signup (name, student_id, email, age, faculty, phone_number, password)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, student_id, email, age, faculty, phone_number, password))
            con.commit()
            return "Registration successful!"
    return render_template('signup.html')
# Connect to the existing SQLite database
def create_connection():
    conn = sqlite3.connect('database.db')  # Connect to your existing database
    return conn

# Function to create the jobs table
def create_jobs_table(conn):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        interview_details TEXT NOT NULL,
        news TEXT NOT NULL
    );
    """
    try:
        conn.execute(create_table_sql)
        conn.commit()
        print("Table 'jobs' added to the existing database successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Main function to create the table
def main():
    # Create connection
    conn = create_connection()

    # Create jobs table
    create_jobs_table(conn)

    # Close the connection
    conn.close()

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/forgot_password/')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset_password')
def request_reset_password():
    return render_template('request_reset_password.html')

@app.route('/reset2')
def reset2():
    return render_template('reset2.html')


if __name__ == '__main__':
    app.run(debug=True)    