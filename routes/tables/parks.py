from flask import Blueprint, render_template, request
from database import db, Query

from config import RECORDS_PER_PAGE

TBLNM = 'parks'

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_parks_blueprint = Blueprint(TBLNM, __name__)


@table_parks_blueprint.route('/%s' % TBLNM)
def view_table():
    """
    URL: /tables/parks?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Query building for table
    """
    select 
        parkname, 
        city, 
        case 
            when isnull(state) then "" 
            else state 
            end as state_m, 
        country, 
        case 
            when isnull(parkalias) then "" 
            else parkalias 
            end as aka 
    from parks 
    order by 
        country desc, 
        state, 
        city,
        parkname;
    """
    state_m = 'case when isnull(state) then \"\" else state end as state_m'
    aka = 'case when isnull(parkalias) then \"\" else parkalias end as aka'
    query = Query().SELECT('parkname, city, %s, country, %s' % (state_m, aka)).FROM(
        'parks').ORDER_BY('country desc, state, city, parkname').LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    """
    select count(*) 
    from parks;
    """
    total_pages_query = Query().SELECT('COUNT(*)').FROM('parks').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data_recordings = []
    for row in result:
        data_recordings.append({'parkname': row[0],
                                'city': row[1],
                                'state': row[2],
                                'country': row[3],
                                'alias': row[4]})

    return render_template('table_parks.html', data_list=data_recordings, current_page=page, total_pages=total_pages)
