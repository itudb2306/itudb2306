from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from database import db, Query
from models.users.auth.forms import LoginForm, SignUpForm
from models.users.auth.user import User
from passlib.hash import pbkdf2_sha256 as hasher

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    URL: /users/login
    """
    print("Login:")
    if current_user.is_authenticated:
        print("User already logged in")
        return redirect(url_for('index.index'))
    
    form = LoginForm()
    remember = request.form.get('remember')

    if form.validate_on_submit():
        # Query building for table
        query = Query().SELECT('*').FROM('users').WHERE("username = %s").BUILD()
        print("Query:", query)
        result = db.fetchone(query, params=(form.username.data, ))
        if result:
            if not hasher.verify(form.password.data, result[3]):
                print("Invalid username or password")
                flash('Invalid username or password')
                return redirect(url_for('auth.login'))
            
            user = User(result[0], result[1], result[2], result[3], result[4])
            print("User logged in:", user)
            login_user(user, remember=remember)
            print(current_user)

            flash('Welcome back, %s!' % result[1])
            return redirect(url_for('index.index'))
        else:
            print("Invalid username or password")
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        
    print("Form is not validated")
    return render_template('users/auth/login.html', form=form)

@auth_blueprint.route('/logout')
@login_required
def logout():
    """
    URL: /users/logout
    """
    logout_user()
    return redirect(url_for('index.index'))

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    URL: /users/signup
    """
    print("Signup:")
    if current_user.is_authenticated:
        print("User already logged in")
        return redirect(url_for('index.index'))
    
    form = SignUpForm()
    print("Form:", form)
    if form.validate_on_submit():
        print("Form is validated")
        form.hash_password()

        # Query building for table
        query = Query().INSERT_INTO('users', ['username', 'email', 'password', 'is_admin']).VALUES('%s', '%s', '%s', '%s').BUILD()
        print("Query:", query)
        db.execute(query, params=(form.username.data, form.email.data, form.password.data, 0))
        flash('Account created for %s!' % form.username.data)
        return redirect(url_for('auth.login'))
    print("Form is not validated")
    return render_template('users/auth/signup.html', form=form)
