from flask import Blueprint, render_template, request
from database import db, Query

from config import RECORDS_PER_PAGE

TBLNM = 'divisions'

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_divisions_blueprint = Blueprint(TBLNM, __name__)


@table_divisions_blueprint.route('/%s' % TBLNM)
def view_table():
    """
    URL: /tables/divisions?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Query building for table
    """
    select 
        l.league,
        l.active as lgActive,
        d.division, 
        d.active as divActive 
    from divisions d, leagues l
    where
        d.lgID=l.lgID;
    """
    query = Query().SELECT('l.league, l.active as lgActive, d.division, d.active as divActive').FROM(
        'divisions d, leagues l').WHERE('d.lgID=l.lgID').LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    """
    select count(*) 
    from divisions d, leagues l
    where d.lgID=l.lgID;
    """
    total_pages_query = Query().SELECT('COUNT(*)').FROM(
        'divisions d, leagues l').WHERE('d.lgID=l.lgID').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data_recordings = []
    for row in result:
        data_recordings.append({'league': row[0],
                                'lgActive': row[1],
                                'division': row[2],
                                'divActive': row[3]})

    return render_template('table_divisions.html', data_list=data_recordings, current_page=page, total_pages=total_pages)
