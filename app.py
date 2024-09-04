from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    
    conn.execute('CREATE TABLE IF NOT EXISTS students (email TEXT, password TEXT)')
    print("Table created successfully")
    conn.close()

init_sqlite_db()

# Home route
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Save to database
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (email, password) VALUES (?, ?)", (email, password))
            con.commit()
            return "Login successful"
    return render_template('login.html')

@app.route('/register/')
def register():
    return "Registration Page"

if __name__ == '__main__':
    app.run(debug=True)