from flask import Flask
from config import (HOST, PORT, DEBUG, TABLES_PREFIX)
from database import db
from routes.index import index_blueprint
from routes.tables.people import table_people_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(table_people_blueprint, url_prefix=TABLES_PREFIX)

"""
@app.route("/")
def index_page():
    return "<h1>Database Project's Homepage</h1>"
"""

@app.route("/test")
def test_page():
    return "<h1>Test Page</h1>"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG) # Run the app server on localhost:5000