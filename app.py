from flask import Flask
from config import (HOST, PORT, DEBUG, TABLES_PREFIX)
from database import db
from routes.index import index_blueprint
from routes.tables.people import table_people_blueprint
from routes.tables.fielding import table_fielding_blueprint
from routes.tables.divisions import table_divisions_blueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(table_people_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_fielding_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_divisions_blueprint, url_prefix=TABLES_PREFIX)

"""
@app.route("/")
def index_page():
    return "<h1>Database Project's Homepage</h1>"
"""


@app.route("/test")
def test_page():
    return "<h1>Test Page</h1>"


if __name__ == "__main__":
    # Run the app server on localhost:5000
    app.run(host=HOST, port=PORT, debug=DEBUG)
