<<<<<<< HEAD
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    
 # Create a new table for sign-up data
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students_signup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            faculty TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    print("Signup table created successfully")
    conn.close()

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

if __name__ == '__main__':
=======
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    
 # Create a new table for sign-up data
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students_signup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            faculty TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    print("Signup table created successfully")
    conn.close()

# Initialize the database
init_sqlite_db()

# Home route (login)
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Save login to database (already implemented)
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

if __name__ == '__main__':
>>>>>>> fc5cf75 (Register page)
    app.run(debug=True)    