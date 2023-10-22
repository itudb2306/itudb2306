import mysql.connector
from config import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.cursor = self.db.cursor()

db = Database()