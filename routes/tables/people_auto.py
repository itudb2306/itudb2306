from flask import Blueprint, render_template

from utils.constants.table import PEOPLE
from utils.decorators.table import table_view_decorator
from models.table import Table
from models.table_data import PeopleData



table_people_auto_blueprint = Blueprint('people_auto', __name__)
@table_people_auto_blueprint.route('/people_auto')
@table_view_decorator(PEOPLE, PeopleData)
def view_table(table: Table):
    """
    URL: /tables/people?p=
    """
    table = table.construct()
    return render_template('table.html', table=table)