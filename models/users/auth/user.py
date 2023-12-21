from flask_login import UserMixin
from database import db, Query

class User(UserMixin):
    """
    User class
    """
    def __init__(self, user_id, username, email, password, is_admin):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def get_id(self):
        """
        Returns user user_id
        """
        return self.user_id

    def is_admin(self):
        """
        Returns True if user is admin
        """
        return self.is_admin
    
    def is_authenticated(self):
        """
        Returns True if user is authenticated
        """
        return True
    
    def is_active(self):
        """
        Returns True if user is active
        """
        return True
    
    def is_anonymous(self):
        """
        Returns True if user is anonymous
        """
        return False

    def __repr__(self):
        return '<User %r>' % self.username
    
def get_user(user_id):
    """
    Returns user object
    """

    # Query building for table
    query = Query().SELECT('*').FROM('users').WHERE('userID = %s').BUILD()
    result = db.fetchone(query, params=(user_id, ))
    if result:
        return User(result[0], result[1], result[2], result[3], result[4])
    else:
        return None