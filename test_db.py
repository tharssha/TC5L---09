import sqlite3

try:
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS students 
                    (email TEXT, password TEXT)''')
        cur.execute("INSERT INTO students (email, password) VALUES (?, ?)", ('test@example.com', 'password123'))
        con.commit()
        print("Data inserted successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")