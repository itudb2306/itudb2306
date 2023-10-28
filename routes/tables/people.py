from flask import Blueprint, render_template, request
from database import db, Query

from config import RECORDS_PER_PAGE

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_people_blueprint = Blueprint('people', __name__)

@table_people_blueprint.route('/people')
def view_table():
    """
    URL: /tables/people?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Query building for table
    query = Query().SELECT('*').FROM('people').LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('people').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

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
        
    return render_template('table_people.html', data_list=data_recordings, current_page = page, total_pages = total_pages)