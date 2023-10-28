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