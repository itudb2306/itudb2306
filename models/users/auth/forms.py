from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from passlib.hash import pbkdf2_sha256 as hasher
from database import db, Query


class LoginForm(FlaskForm):
    """
    Login form
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Login')

    def __repr__(self):
        return f"LoginForm('{self.username.data}', '{self.password.data}')"
    

class SignUpForm(FlaskForm):
    """
    Sign up form
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=5, max=50), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=5, max=20), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        Validates username
        """
        # Query building for table
        query = Query().SELECT('*').FROM('users').WHERE("username = %s").BUILD()
        result = db.fetchone(query, params=(username.data, ))
        if result:
            raise ValidationError('Username already exists. Please choose a different one.')
        
    def validate_email(self, email):
        """
        Validates email
        """
        # Query building for table
        query = Query().SELECT('*').FROM('users').WHERE("email = %s").BUILD()
        result = db.fetchone(query, params=(email.data, ))
        if result:
            raise ValidationError('Email address already exists. Please choose a different one.')
        
    def hash_password(self):
        """
        Hashes password
        """
        self.password.data = hasher.hash(self.password.data)

    def __repr__(self):
        return f"SignUpForm('{self.username.data}', '{self.email.data}', '{self.password.data}, '{self.confirm_password.data}')"
