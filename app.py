from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import  bcrypt


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Initialize the SQLite databases
def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    # Create a new table for sign-up data
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students_signup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            student_id INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            faculty TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    print("Signup table created successfully")

    conn.commit()
    conn.close()

# Initialize the database
init_sqlite_db()

@app.route('/welcome/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email'].strip().lower()  # Normalize email
        password = request.form['password'].strip()

        print(f"Attempting to login with email: {email}")

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM students_signup WHERE email = ?", (email,))
            user = cur.fetchone()

            if user:
                print(f"User fetched from database: {user}")
                if check_password_hash(user[7], password):  # Check password
                    session['user'] = user[0]  # Store user ID in session
                    return redirect(url_for('dashboard'))
                else:
                    print("Password does not match")
            else:
                print("No user found with that email")
                
            return "Invalid email or password"
    return render_template('login.html')
# Initialize your SQLite database and other routes...


@app.route('/welcome/signup.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        email = request.form['email']
        age = request.form['age']
        faculty = request.form['faculty']
        phone_number = request.form['phone_number']
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password)

        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            try:
                cur.execute('''
                    INSERT INTO students_signup (name, student_id, email, age, faculty, phone_number, password)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, student_id, email, age, faculty, phone_number, hashed_password))
                con.commit()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return "Email already exists."
            except Exception as e:
                return f"An error occurred: {e}"
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear the session
    return redirect(url_for('welcome'))  # Redirect to welcome pag


# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('jobs.db')

# Create a cursor object
cursor = conn.cursor()

# Create the jobs table
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT NOT NULL,
    department TEXT NOT NULL,
    interview_details TEXT NOT NULL,
    news TEXT
)
''')

# Insert job data into the table

job_data = [
    ("Software Developer", "Computing and Informatics", 
     "Interviews will be conducted online via video call.", 
     "Demand for software developers is increasing due to the rise of technology companies."),
     
    ("Data Scientist", "Computing and Informatics", 
     "Candidates should be prepared for a technical assessment during the interview process.", 
     "Data science skills are highly sought after in various industries."),
     
    ("Information Security Analyst", "Computing and Informatics", 
     "Interviews will include discussions on cybersecurity best practices.", 
     "With the increase in cyber threats, there is a growing demand for information security professionals."),
     
    ("Database Administrator", "Computing and Informatics", 
     "Be prepared to discuss your experience with database management systems (e.g., MySQL, PostgreSQL, Oracle).",
     "DBAs are managing increasingly large datasets as organizations accumulate more data from various sources."),
     
    ("Cybersecurity Engineer", "Computing and Informatics", 
     "Be prepared to discuss your experience in cybersecurity operations and threat intelligence analysis.", 
     "Cybersecurity engineers are combating sophisticated cyber threats through proactive threat hunting."),
     
    ("Systems Administrator", "Computing and Informatics", 
     "Be prepared to discuss your experience in managing computer systems, networks, and servers.", 
     "Systems administrators are embracing automation, cloud technologies, and containerization."),
     
    ("Mechanical Engineer", "Engineering", 
     "Candidates will undergo a technical interview focusing on engineering principles.", 
     "Mechanical engineering jobs are in demand, especially in manufacturing and renewable energy sectors."),
     
    ("Electrical Engineer", "Engineering", 
     "Expect questions about your experience with circuit design, troubleshooting skills, and relevant software.", 
     "Renewable energy projects continue to grow, providing opportunities for electrical engineers."),
     
    ("Chemical Engineer", "Engineering", 
     "Prepare to discuss your experience with process optimization, safety protocols, and chemical reactions.", 
     "Chemical engineers are increasingly involved in eco-friendly production processes and materials."),
     
    ("Software Engineer", "Engineering", 
     "Be ready to demonstrate your coding skills, problem-solving abilities, and knowledge of development methodologies.", 
     "Software engineers are developing AI, machine learning applications, and cybersecurity solutions."),
     
    ("Environmental Engineer", "Engineering", 
     "Be ready to discuss your expertise in environmental regulations, pollution control technologies, and risk assessment.", 
     "Environmental engineers are addressing pressing challenges like climate change and waste management."),
     
    ("Biomedical Engineer", "Engineering", 
     "Prepare to discuss your experience in medical device design, biomaterials, and biomechanics.", 
     "Biomedical engineers are at the forefront of healthcare innovation, developing medical devices and diagnostic tools."),
     
    ("Marketing Assistant", "Management", 
     "Interviews will assess candidates' knowledge of marketing strategies and trends.", 
     "Marketing roles are crucial for companies looking to expand their customer base."),
     
    ("Sales Manager", "Management", 
     "Be ready to demonstrate your leadership skills, ability to strategize sales campaigns, and track record of meeting targets.", 
     "Sales managers are adapting to the rise of e-commerce by incorporating digital marketing strategies."),
     
    ("Human Resources Manager", "Management", 
     "Expect questions about employee relations, recruitment strategies, and handling conflicts in the workplace.", 
     "HR professionals are focusing more on employee well-being and mental health support."),
     
    ("Product Manager", "Management", 
     "Expect to be asked about your experience with product lifecycle management and prioritizing product features.", 
     "Product managers are leveraging agile methodologies and cross-functional teams for rapid development cycles."),
     
    ("Project Manager", "Management", 
     "Expect to be asked about your experience with project planning, budgeting, and risk management.", 
     "Project managers are embracing agile methodologies and digital tools to increase flexibility and efficiency."),
     
    ("Financial Manager", "Management", 
     "Be prepared to discuss your experience in financial planning, analysis, and reporting.", 
     "Financial managers are focusing on navigating economic uncertainties and adapting strategies to volatile markets."),
     
    ("Graphic Designer", "Creative Multimedia", 
     "Candidates should prepare a portfolio to showcase their design skills.", 
     "The demand for graphic designers is increasing with the growth of digital media."),
     
    ("Film Editor", "Creative Multimedia", 
     "Prepare to discuss your editing software proficiency and storytelling abilities.", 
     "Streaming platforms are driving demand for film editors, as they produce original content."),
     
    ("Web Developer", "Creative Multimedia", 
     "Be ready to showcase your coding skills and experience with responsive design.", 
     "Mobile-first design and web accessibility features are shaping the priorities of web developers."),
     
    ("Animator", "Creative Multimedia", 
     "Prepare to present your animation reel and discuss your animation techniques.", 
     "Animators are exploring immersive technologies like virtual reality and augmented reality."),
     
    ("Video Editor", "Creative Multimedia", 
     "Be ready to showcase your video editing portfolio and proficiency with editing software.", 
     "Video editors are adapting to the growing demand for short-form video content on social media platforms."),
     
    ("Content Creator", "Creative Multimedia", 
     "Prepare to discuss your content creation portfolio and your ability to engage with a target audience.", 
     "Social media content creators are diversifying their formats to include short-form videos and live streams."),

]

cursor.executemany('''
INSERT INTO jobs (job_title, department, interview_details, news)
VALUES (?, ?, ?, ?)
''', job_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and jobs inserted successfully.")

# Connect to the SQLite database
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Query the jobs
cursor.execute("SELECT * FROM jobs")

# Fetch all rows from the query
jobs = cursor.fetchall()

# Display the jobs
for job in jobs:
    print(f"Job Title: {job[1]}")
    print(f"Department: {job[2]}")
    print(f"Interview Details: {job[3]}")
    print(f"News: {job[4]}")
    print("="*40)

# Close the connection
conn.close()

# Connect to the existing jobs database
conn = sqlite3.connect('jobs.db')

# Create a cursor object
cursor = conn.cursor()

# Create the new 'posted_jobs' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS posted_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT NOT NULL,
    job_category TEXT NOT NULL,
    job_description TEXT NOT NULL,
    interview_details TEXT NOT NULL,
    news TEXT,
    posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit changes and close the connection to the database
conn.commit()
conn.close()

print("New 'posted_jobs' table created successfully.")

@app.route('/dashboard/jobs.html')
def available_jobs():
    with sqlite3.connect('jobs.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
    return render_template('jobs.html', jobs=jobs)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS user_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_question TEXT NOT NULL,
            admin_reply TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/dashboard/faq.html')
def faq():
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM user_questions').fetchall()
    conn.close()
    return render_template('faq.html', questions=questions)

@app.route('/submit_question', methods=['POST'])
def submit_question():
    user_question = request.form['user_question']
    conn = get_db_connection()
    conn.execute('INSERT INTO user_questions (user_question) VALUES (?)', (user_question,))
    conn.commit()
    conn.close()
    flash('Your question has been submitted successfully!')
    return redirect('/dashboard/faq.html')

@app.route('/reply_question/<int:question_id>', methods=['POST'])
def reply_question(question_id):
    admin_reply = request.form['admin_reply']
    conn = get_db_connection()
    conn.execute('UPDATE user_questions SET admin_reply = ? WHERE id = ?', (admin_reply, question_id))
    conn.commit()
    conn.close()
    flash('Reply submitted successfully!')
    return redirect('/dashboard/faq.html')



def get_db_connection():
    conn = sqlite3.connect('database.db')  
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS resume (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            age TEXT NOT NULL,
            bio TEXT,
            status TEXT,
            faculty TEXT,
            job_roles TEXT
        )''')
        conn.commit()
        print("Database initialized and table created.")



@app.route('/dashboard/profile.html', methods=['GET', 'POST'])
def profile():
    user_email = session.get('user_email')  # Check if the user email exists in the session

    if request.method == 'POST':
        # Fetch form data
        user_email = request.form.get('user_email')
        user_name = request.form.get('user_name')
        user_password = request.form.get('user_password')
        user_age = request.form.get('user_age')
        user_bio = request.form.get('user_bio', '')
        user_status = request.form.get('user_Status')
        user_faculty = request.form.get('user_faculty')
        job_roles = request.form.get('user_job_roles')

        # Hash the password
        hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode('utf-8')

        try:
            with get_db_connection() as con:
                cur = con.cursor()
                # Check if profile exists in the 'resume' table
                cur.execute("SELECT * FROM resume WHERE email = ?", (user_email,))
                existing_profile = cur.fetchone()

                if existing_profile:
                    # Update existing profile in the 'resume' table
                    cur.execute('''UPDATE resume 
                                   SET name = ?, password = ?, age = ?, bio = ?, status = ?, faculty = ?, job_roles = ?
                                   WHERE email = ?''', 
                               (user_name, hashed_password, user_age, user_bio, user_status, user_faculty, job_roles, user_email))
                else:
                    # Insert new profile into the 'resume' table
                    cur.execute('''INSERT INTO resume (name, email, password, age, bio, status, faculty, job_roles)
                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                                (user_name, user_email, hashed_password, user_age, user_bio, user_status, user_faculty, job_roles))

                con.commit()
                flash('Profile saved successfully!', 'success')
                return redirect(url_for('profile'))
        except Exception as e:
            app.logger.error(f"Error while saving profile: {e}")
            flash('An error occurred while saving your profile.', 'danger')

    # If GET request, fetch existing profile data
    with get_db_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM resume WHERE email = ?", (user_email,))
        profile_data = cur.fetchone()

    return render_template('profile.html', profile=profile_data)







@app.route('/dashboard/contactus.html')
def contactus():
    return render_template('contactus.html')

@app.route('/dashboard/term_condition.html')
def term_condition():
    return render_template('term_condition.html')

@app.route('/dashboard/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/dashboard/post_jobs.html')
def post_jobs():
    return render_template('post_jobs.html')

@app.route('/dashboard/user_home.html')
def user_home():
    return render_template('user_home.html')
@app.route('/welcome/')
def welcome():
    return render_template('welcome.html')
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    init_db() 
    app.run(debug=True) 
