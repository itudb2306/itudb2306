import os
from dotenv import load_dotenv
load_dotenv()


HOST = "0.0.0.0"
PORT = 5000
DEBUG = True


# Database
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


# Tables
TABLES_PREFIX = "/tables"
RECORDS_PER_PAGE = 20

# Authentication
AUTH_PREFIX = "/user"

# Flask
SECRET_KEY = os.getenv("SECRET_KEY")
WTF_CSRF_SECRET_KEY = os.getenv("WTF_CSRF_SECRET_KEY")