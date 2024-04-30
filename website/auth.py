from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from .models import Job, Student,Employee,Application
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import hashlib

auth = Blueprint('auth', __name__)
@auth.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html",user =current_user)
@auth.route('/', methods=['GET', 'POST'])  # Import Student and Employee models

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email exists in either the Student or Employee table
        user = Student.query.filter_by(email=email).first() or Employee.query.filter_by(email=email).first()

        if user:
            # Check if the password is correct
            if check_password_hash(user.password, password):
                # Log the user in (you might want to use Flask-Login for this)
                # For now, let's assume you have a session-based authentication mechanism
                login_user(user)
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.ed'))
            else:
                flash('Incorrect password. Please try again.', category='error')
        else:
            flash('Email not found. Please register if you are a new user.', category='error')

    # If the request method is GET or if there's an error, render the login template
    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        email = request.form.get('email')
        user_type = request.form.get('type')
        password = request.form.get('password')
        CGPA = request.form.get('CGPA')

        # Check if the email already exists in either the Student or Employee table
        if Student.query.filter_by(email=email).first() or Employee.query.filter_by(email=email).first():
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Handle CGPA if it's not None and can be converted to a float
            if CGPA:
                try:
                    CGPA = float(CGPA)
                except ValueError:
                    flash('CGPA must be a valid number.', category='error')
                    return redirect(url_for('auth.sign_in'))

            # Check if the user is a student or employee and create the appropriate object
            if user_type == 'student':
                new_user = Student(
                    id=id,
                    name=name,
                    email=email,
                    type=user_type,
                    password=generate_password_hash(password, method='pbkdf2:sha256')
                )
                if CGPA:
                    new_user.cgpa = CGPA
            else:
                new_user = Employee(
                    id=id,
                    name=name,
                    email=email,
                    type=user_type,
                    password=generate_password_hash(password, method='pbkdf2:sha256')
                )

            try:
                # Add the new user to the database session and commit changes
                db.session.add(new_user)
                db.session.commit()
                flash('Account created!', category='success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                flash('An error occurred while creating your account.', category='error')
                print(e)  # Print the error for debugging purposes

    # If the request method is GET or if there's an error, render the sign-in template
    return render_template('sign_in.html', student=current_user) or render_template('sign_in.html',)

@auth.route('/')
def index():
    return render_template('login.html')

@auth.route('/1')
def link1():
    return render_template('1.html')
@auth.route('/review')
def reviews():
    return render_template('review.html')

@auth.route('/2')
def link2():
    return render_template('2.html')

@auth.route('/3')
def link3():
    return render_template('3.html')

@auth.route('/4')
def link4():
    return render_template('4.html')

@auth.route('/5')
def link5():
    return render_template('5.html')

@auth.route('/6')
def link6():
    return render_template('6.html')

@auth.route('/7')
def link7():
    return render_template('7.html')

@auth.route('/8')
def link8():
    return render_template('8.html')

@auth.route('/9')
def link9():
    return render_template('9.html')

@auth.route('/10')
def link10():
    return render_template('10.html')






