# app.py
# import helpers
# Flask is the main helper
from flask import Flask, render_template, request, redirect, url_for, session, flash

# connecting app to database
from flask_sqlalchemy import SQLAlchemy

# password handling
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__, instance_relative_config=True )
app.config['SECRET_KEY'] = 'a-super-secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(200), nullable=False) 


@app.route('/')
def index():
    return render_template('index.html')

#regiteration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            # If the user exists, show a message and send them back to the form
            flash('That username is already taken. Please choose a different one.', 'error')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('acc.html')


# login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
            
    return render_template('login.html')


# dashboard
@app.route('/dashboard')
def dashboard():
    #not logged in
    if 'user_id' not in session:
        #login page
        flash('You must be logged in to view this page.', 'warning')
        return redirect(url_for('login'))
        # else dashboard
    return render_template('dashboard.html')


# logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    with app.app_context():
        db.create_all()

    app.run(debug=True)