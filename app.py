from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Initialize the SQLite database
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    # Create a new table for sign-up data
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students_signup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_id INTEGER NOT NULL,
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

@app.route('/welcome/')
def welcome():
    return  render_template('welcome.html')
    
# Home route (login)
@app.route('/welcome/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM students_signup WHERE email = ?", (email,))
            user = cur.fetchone()

            if user:
                # user[7] is the hashed password in the DB
                if check_password_hash(user[7], password):
                    session['user'] = user[0]  # Store user ID in session
                    return redirect(url_for('dashboard'))  # Redirect to the dashboard
                else:
                    return "Invalid password"
            else:
                return "User not found"
    return render_template('login.html')

#route to dashboard after login
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
    

# Registration route (sign-up)
@app.route('/welcome/signup.html', methods=['GET', 'POST'])
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

        # Hash the password before saving it
        hashed_password = generate_password_hash(password)

        # Save sign-up data to database
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute('''
                INSERT INTO students_signup (name, student_id, email, age, faculty, phone_number, password)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, student_id, email, age, faculty, phone_number, hashed_password))
            con.commit()
            return "Registration successful!"
    return render_template('signup.html')

@app.route('/dashboard/jobs.html')
def available_jobs():
    return render_template('jobs.html')

@app.route('/dashboard/post_jobs.html')
def post_jobs():
    return render_template('post_jobs.html')

@app.route('/dashboard/contactus.html')
def contactus():
    return render_template('contactus.html')

@app.route('/dashboard/terms&conditions.html')
def terms_conditions():
    return render_template('/term&condition.html')

@app.route('/dashboard/settings.html')
def settings():
    return render_template('/settings.html')        

@app.route('/dashboard/profile.html')
def profile():
    return render_template('/profile.html')        
                

if __name__ == '__main__':
    app.run(debug=True)