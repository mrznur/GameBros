from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user_model import create_user, get_user_by_username

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_page():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = get_user_by_username(username)
    
    if user and user['password'] == password:
        session['user'] = username
        return 'Login Successful'
    else:
        flash('Invalid credentials')
        return redirect(url_for('auth.login_page'))

@auth_bp.route('/register/buyer')
def register_buyer():
    return render_template('newacc.html')

@auth_bp.route('/register/developer')
def register_developer():
    return render_template('devacc.html')

@auth_bp.route('/register/submit', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']  # 'buyer' or 'developer'

    if get_user_by_username(username):
        flash('Username already exists.')
        return redirect(url_for('auth.login_page'))

    create_user(username, password, role)
    flash('Account created successfully.')
    return redirect(url_for('auth.login_page'))
