from flask import Flask
from flask_login import LoginManager
from models.users.auth.user import get_user
from config import (HOST, PORT, DEBUG, TABLES_PREFIX,
                    AUTH_PREFIX, SECRET_KEY, WTF_CSRF_SECRET_KEY)
from database import db
from routes.index import index_blueprint
from routes.tables.people import table_people_blueprint
from routes.tables.fielding import table_fielding_blueprint
from routes.tables.batting import table_batting_blueprint
from routes.tables.divisions import table_divisions_blueprint
from routes.tables.parks import table_parks_blueprint
from routes.tables.teams import table_teams_blueprint
from routes.tables.leagues import table_leagues_blueprint
from routes.tables.pitching import table_pitching_blueprint
from routes.users.auth import auth_blueprint
from routes.tables.homegames import table_homegames_blueprint
from routes.forum.forum import forum_blueprint
from routes.tables.halloffame import table_halloffame_blueprint
from routes.tables.managers import table_managers_blueprint
from routes.tables.appearances import table_appearances_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['WTF_CSRF_SECRET_KEY'] = WTF_CSRF_SECRET_KEY

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(index_blueprint, url_prefix='/')
app.register_blueprint(table_people_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_fielding_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_divisions_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_parks_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_batting_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_teams_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_leagues_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_pitching_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(auth_blueprint, url_prefix=AUTH_PREFIX)
app.register_blueprint(table_homegames_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(forum_blueprint, url_prefix='/forum')
app.register_blueprint(table_halloffame_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_managers_blueprint, url_prefix=TABLES_PREFIX)
app.register_blueprint(table_appearances_blueprint, url_prefix=TABLES_PREFIX)

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
