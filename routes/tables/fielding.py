from flask import Blueprint, render_template, request
from database import db, Query

from config import RECORDS_PER_PAGE

table_fielding_blueprint = Blueprint('fielding', __name__)

@table_fielding_blueprint.route('/fielding')
def view_fielding_table():
    """
    URL: /tables/fielding?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Query building for the "fielding" table
    query = Query().SELECT('*').FROM('fielding').LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('fielding').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data_recordings = []
    for row in result:
        data_recordings.append({
            'ID': row[0],
            'playerID': row[1],
            'yearID': row[2],
            'stint': row[3],
            'teamID': row[4],
            'team_ID': row[5],
            'lgID': row[6],
            'POS': row[7],
            'G': row[8],
            'GS': row[9],
            'InnOuts': row[10],
            'PO': row[11],
            'A': row[12],
            'E': row[13],
            'DP': row[14],
            'PB': row[15],
            'WP': row[16],
            'SB': row[17],
            'CS': row[18],
            'ZR': row[19],
        })

    return render_template('table_fielding.html', data_list=data_recordings, current_page=page, total_pages=total_pages)
