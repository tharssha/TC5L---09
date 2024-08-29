from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user store (replace with database in production)
users = {
    'admin': {'password': 'adminpass', 'is_admin': True}
}

class User(UserMixin):
    def __init__(self, username, is_admin):
        self.id = username
        self.is_admin = is_admin

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id, users[user_id]['is_admin'])
    return None

@app.route('/')
def home():
    return 'Welcome to the Job Portal!'

@app.route('/login')
def login():
    # Simulate login (replace with actual login form logic)
    user = User('admin', users['admin']['is_admin'])
    login_user(user)
    return redirect(url_for('admin_dashboard'))

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return 'Access Denied', 403
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
