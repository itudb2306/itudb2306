from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""


table_teams_name_blueprint = Blueprint("teams_name", __name__)


@table_teams_name_blueprint.route('/teams')
def view_table():
    """
    URL: /tables/teams?p=
    """
    # asc/desc ascending descending mode
    order_by = request.args.get('orderby', 'team_name', type=str)
    order_type = request.args.get('ordertype', 'asc', type=str)

    # precaution for not breaking sql
    if order_by != 'team_name' or order_by != 'number_of_records':
        order_by = 'team_name'
    if order_type != 'asc' or order_type != 'desc':
        order_type = 'asc'

    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # select name, count(*) from teams group by name;

    # Query building for table
    query = "select name as team_name, count(*) as number_of_records from teams group by name order by %s %s limit %s, %s" % (
        order_by, order_type, first_record, RECORDS_PER_PAGE)
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = "select count(distinct name) from teams"
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data_recordings = []
    for row in result:
        data_recordings.append({'team_name': row[0],
                                'number_of_records': row[1]})

    return render_template('teams_name.html', data_list=data_recordings, current_page=page, total_pages=total_pages)
