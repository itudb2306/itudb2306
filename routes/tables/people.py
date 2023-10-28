from flask import Blueprint, render_template
from database import db, Query

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_people_blueprint = Blueprint('people', __name__)

@table_people_blueprint.route('/people')
def view_table():
    query = Query().SELECT('*').FROM('people').LIMIT(10, 10).BUILD()
    print(query)
    result = db.fetchall(query)

    data_recordings = []
    for row in result:
        data_recordings.append({'name_first': row[13],
                                'name_last': row[14],
                                'name_given': row[15],
                                'birth_date': row[25],
                                'birth_country' : row[4],
                                'weight': row[16],
                                'height': row[17],
                                'bats': row[18],
                                'throws': row[19]})
        
    return render_template('table_people.html', data_list=data_recordings)