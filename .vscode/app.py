from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def admin_dashboard():
    return render_template('admin_dashboard.html')


import sqlite3

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

if __name__ == '__main__':
    app.run(debug=True)

