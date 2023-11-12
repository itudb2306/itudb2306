from flask import Blueprint, render_template, request
from database import db, Query

from config import RECORDS_PER_PAGE

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_fielding_blueprint = Blueprint('fielding', __name__)

@table_fielding_blueprint.route('/fielding')
def view_table():
    """
    URL: /tables/fielding?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE
    
    # Query building for table

    """
    SELECT
    p.nameFirst AS FirstName,
    p.nameLast AS LastName,
    t.name AS TeamName,
    f.yearID,
    f.stint,
    f.lgID,
    f.POS,
    f.G,
    f.GS,
    f.InnOuts,
    f.PO,
    f.A,
    f.E,
    f.DP,
    f.PB,
    f.WP,
    f.SB,
    f.CS,
    f.ZR
    FROM
        fielding f
    JOIN
        people p ON f.playerID = p.playerID
    JOIN
        teams t ON f.team_id = t.id;
    """

    # self._FROM += 'JOIN %s ON %s' % (table_name, condition)

    query = Query().SELECT('p.nameFirst AS FirstName, p.nameLast AS LastName, t.name AS TeamName, f.playerID, f.yearID, f.stint, f.teamID, f.team_ID, f.lgID, f.POS, f.G, f.GS, f.InnOuts, f.PO, f.A, f.E, f.DP, f.PB, f.WP, f.SB, f.CS, f.ZR'
    ).FROM('fielding f ' 
    ).JOIN('people p', 'f.playerID = p.playerID'
    ).JOIN('teams t', 'f.team_id = t.id'
    ).LIMIT(first_record, RECORDS_PER_PAGE
    ).BUILD()
    
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
            'FirstName': row[0],
            'LastName': row[1],
            'TeamName': row[2],
            'yearID': row[3],
            'stint': row[4],
            'lgID': row[5],
            'POS': row[6],
            'G': row[7],
            'GS': row[8],
            'InnOuts': row[9],
            'PO': row[10],
            'A': row[11],
            'E': row[12],
            'DP': row[13],
            'PB': row[14],
            'WP': row[15],
            'SB': row[16],
            'CS': row[17],
            'ZR': row[18]
        })

    return render_template('table_fielding.html', data_list=data_recordings, current_page=page, total_pages=total_pages)
