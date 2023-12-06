from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_fielding_blueprint = Blueprint('fielding', __name__)

def getLeaguesList():
    # Query for division league selection
    leagues_list = []
    leagues_query = Query().SELECT('lgID, league').FROM('leagues').BUILD()
    leagues_result = db.fetchall(leagues_query)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })
    return leagues_list

@table_fielding_blueprint.route('/fielding')
def view_table():
    """
    URL: /tables/fielding?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE
    
    # Query building for table
    leagues_list = getLeaguesList()

    """
    SELECT
    p.nameFirst AS FirstName,
    p.nameLast AS LastName,
    t.name AS TeamName,
    f.yearID,
    f.stint,
    l.league AS LeagueName,
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
    f.ID
    FROM
        fielding f
    JOIN
        people p ON f.playerID = p.playerID
    JOIN
        teams t ON f.team_id = t.id
    JOIN
        leagues l ON f.lgID = l.lgID;
    """

    # self._FROM += 'JOIN %s ON %s' % (table_name, condition)

    query = Query().SELECT('p.nameFirst AS FirstName, p.nameLast AS LastName, t.name AS TeamName, f.yearID, f.stint, l.league AS LeagueName, f.POS, f.G, f.GS, f.InnOuts, f.PO, f.A, f.E, f.DP, f.PB, f.WP, f.SB, f.CS, f.ZR, f.ID'
    ).FROM('fielding f ' 
    ).JOIN('people p', 'f.playerID = p.playerID'
    ).JOIN('teams t', 'f.team_id = t.id'
    ).JOIN('leagues l', 'f.lgID = l.lgID'
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
            'LeagueName': row[5],
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
            'ZR': row[18],
            'ID': row[19]
        })

    return render_template('table_fielding.html', data_list=data_recordings, current_page=page, total_pages=total_pages, leagues_list = leagues_list)


@table_fielding_blueprint.route('/fielding/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/fielding/update/<string:ID>
    """

    if request.method == 'POST' and ID is not None:
        try:
             # Get form data in parametrized format
            col_val_pairs = {
                #'playerID': request.form['playerID'],
                'yearID': request.form['yearID'],
                'stint': request.form['stint'],
                #'team_id': request.form['team_id'],
                'lgID': request.form['lgID'],
                'POS': request.form['POS'],
                'G': request.form['G'],
                'GS': request.form['GS'],
                'InnOuts': request.form['InnOuts'],
                'PO': request.form['PO'],
                'A': request.form['A'],
                'E': request.form['E'],
                'DP': request.form['DP'],
                'PB': request.form['PB'],
                'WP': request.form['WP'],
                'SB': request.form['SB'],
                'CS': request.form['CS'],
                'ZR': request.form['ZR']
            }
            
            # Query building for table
            query = Query().UPDATE('fielding').SET(col_val_pairs).WHERE('ID = %s' % ID)
            queryString = query.BUILD()
            print(query._PARAMS)
            print(queryString)
            db.execute(queryString, tuple(query._PARAMS))
            print('Record updated successfully')
        
        except:    
            print('Record update failed')
            
    return redirect(url_for('fielding.view_table'))
