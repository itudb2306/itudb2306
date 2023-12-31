from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query
from utility import exceptionPage
from models.tables.pitching.records import Records
from models.tables.pitching.forms import FilterForm, SortForm
from config import RECORDS_PER_PAGE
import urllib.parse

table_pitching_blueprint = Blueprint('pitching', __name__)


def getPlayersList():
    player_list = []
    player_query = Query().SELECT('playerID, nameGiven').FROM('people').BUILD()
    player_result = db.fetchall(player_query)
    for row in player_result:
        player_list.append({'playerID': row[0],
                            'nameGiven': row[1], })
    return player_list


def getTeamsList():
    teams_list = []
    teams_query = Query().SELECT('id, name').FROM('teamnames').BUILD()
    teams_result = db.fetchall(teams_query)
    for row in teams_result:
        teams_list.append({'team_id': row[0],
                           'name': row[1], })
    return teams_list


def getLeaguesList():
    # Query for division league selection
    leagues_list = []
    leagues_query = Query().SELECT('lgID, league').FROM('leagues').BUILD()
    leagues_result = db.fetchall(leagues_query)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })
    return leagues_list


@table_pitching_blueprint.route('/pitching', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/pitching?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Query building for table
    leagues_list = getLeaguesList()
    teams_list = getTeamsList()
    players_list = getPlayersList()
    """
    SELECT
    p.nameFirst AS FirstName,
    p.nameLast AS LastName,
    t.name AS TeamName,
    pitching.yearID,
    pitching.stint,
    l.league AS LeagueName,
    pitching.W,
    pitching.L,
    pitching.G,
    pitching.GS,
    pitching.CG,
    pitching.SHO,
    pitching.SV,
    pitching.IPouts,
    pitching.ID
    FROM
        pitching
    JOIN
        people p ON pitching.playerID = p.playerID
    JOIN
        teamnames t ON pitching.team_id = t.id
    JOIN
        leagues l ON pitching.lgID = l.lgID;
    """

    request_form = request.form.to_dict()

    # Filtering arguments from the previous request:
    # filter=nameFirst=John&nameLast=Doe&...
    filter_request_from_prev = request.args.get('filter', None, type=str)
    # [('nameFirst', 'John'), ('nameLast', 'Doe'), ...]
    filter_dict = urllib.parse.parse_qsl(filter_request_from_prev)
    # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    filter_dict = dict(filter_dict)
    filter = FilterForm().from_dict(filter_dict)  # FilterForm object
    # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    filter_dict = filter.to_dict()
    print("Filter request from previous page: ", filter_dict)

    # Filtering arguments from the new request:
    filter_request_from_form = FilterForm().from_dict(request_form)
    if not filter_request_from_form.is_empty():
        filter = filter_request_from_form
        filter_dict = filter.to_dict()
        print("Filter request from form: ", filter_dict)

    filter_string = filter.to_and_string()

    # sort=nameFirst=ASC&nameLast=DESC&...
    sort = request.args.get('sort', None, type=str)
    # [('nameFirst', 'ASC'), ('nameLast', 'DESC'), ...]
    sort_dict = urllib.parse.parse_qsl(sort)
    # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    sort_dict = dict(sort_dict)
    sort = SortForm().from_dict(sort_dict)  # SortForm object
    sort_dict = sort.to_dict()  # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    print("Sort request from previous page: ", sort_dict)

    sort_request_from_form = SortForm().from_dict(request.form)
    if not sort_request_from_form.is_empty():
        sort = sort_request_from_form
        sort_dict = sort.to_dict()
        print("Sort request from form: ", sort_dict)

    sort_string = sort.to_and_string()

    query = Query().SELECT('p.nameFirst AS FirstName, p.nameLast AS LastName, t.name AS TeamName, pitching.yearID, pitching.stint, l.league AS LeagueName, pitching.W, pitching.L, pitching.G, pitching.GS, pitching.CG, pitching.SHO, pitching.SV, pitching.IPouts, pitching.ID'
                           ).FROM('pitching '
                                  ).JOIN('people p', 'pitching.playerID = p.playerID'
                                         ).JOIN('teamnames t', 'pitching.team_id = t.id'
                                                ).JOIN('leagues l', 'pitching.lgID = l.lgID'
                                                       ).WHERE(filter_string
                                                               ).ORDER_BY(sort_string
                                                                          ).LIMIT(first_record, RECORDS_PER_PAGE
                                                                                  ).BUILD()

    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('pitching '
                                                        ).JOIN('people p', 'pitching.playerID = p.playerID'
                                                               ).JOIN('teamnames t', 'pitching.team_id = t.id'
                                                                      ).JOIN('leagues l', 'pitching.lgID = l.lgID'
                                                                             ).WHERE(filter_string
                                                                                     ).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data = Records()
    data.from_list(result)
    print(f"Records length: {len(data.records)}")

    filter_encoded = urllib.parse.urlencode(filter_dict)
    sort_encoded = urllib.parse.urlencode(sort_dict)

    return render_template('table_pitching/table_pitching.html', data_list=data.records, current_page=page, total_pages=total_pages, leagues_list=leagues_list, teams_list=teams_list, players_list=players_list, filter=filter_encoded, sort=sort_encoded)


@table_pitching_blueprint.route('/pitching/details/<string:ID>', methods=['GET', 'POST'])
def view_details(ID):
    """
    URL: /tables/pitching/details/<string:ID>
    """
    # Query building for table
    query = Query().SELECT('p.nameFirst AS FirstName, p.nameLast AS LastName, t.name AS TeamName, pitching.yearID, pitching.stint, l.league AS LeagueName, pitching.W, pitching.L, pitching.G, pitching.GS, pitching.CG, pitching.SHO, pitching.SV, pitching.IPouts, pitching.ID'
                           ).FROM('pitching '
                                  ).JOIN('people p', 'pitching.playerID = p.playerID'
                                         ).JOIN('teamnames t', 'pitching.team_id = t.id'
                                                ).JOIN('leagues l', 'pitching.lgID = l.lgID'
                                                       ).WHERE('pitching.ID = %s' % ID
                                                               ).BUILD()

    print(query)
    result = db.fetchall(query)

    # Match column names with values
    result = result[0]
    result = dict(zip(['FirstName', 'LastName', 'TeamName', 'yearID', 'stint',
                  'LeagueName', 'W', 'L', 'G', 'GS', 'CG', 'SHO', 'SV', 'IPouts','ID'], result))

    return render_template('table_pitching/pitching_details.html', data=result)


@table_pitching_blueprint.route('/pitching/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID=None):
    """
    URL: /tables/pitching/delete/<string:ID>
    """

    if request.method == 'POST' and ID is not None:
        try:
            # Query building for table
            query = Query().DELETE().FROM('pitching').WHERE('ID = %s' % ID)
            queryString = query.BUILD()
            db.execute(queryString)
            print('Record deleted successfully')

        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('pitching.view_table'))


@table_pitching_blueprint.route('/pitching/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/pitching/update/<string:ID>
    """

    if request.method == 'POST' and ID is not None:
        try:
            # Get form data in parametrized format
            print("Entered update_record")
            print(request.form)
            col_val_pairs = {
                # 'playerID': request.form['playerID'],
                'yearID': request.form['yearID'],
                'stint': request.form['stint'],
                'team_id': request.form['team_id'],
                'lgID': request.form['lgID'],
                'W': request.form['W'],
                'L': request.form['L'],
                'G': request.form['G'],
                'GS': request.form['GS'],
                'CG': request.form['CG'],
                'SHO': request.form['SHO'],
                'SV': request.form['SV'],
                'IPouts': request.form['IPouts']
            }

            print(col_val_pairs)

            # Query building for table
            # BE CAREFUL: TEAM NAME'S ARE NOT UNIQUE IT CAUSES WRONG UPDATES
            query = Query().UPDATE('pitching').SET(col_val_pairs).WHERE('ID = %s' % ID)
            queryString = query.BUILD()
            print(query._PARAMS)
            print(queryString)
            db.execute(queryString, tuple(query._PARAMS))
            print('Record updated successfully')

        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('pitching.view_table'))


@table_pitching_blueprint.route('/pitching/add', methods=['GET', 'POST'])
def add_record():
    """
    URL: /tables/pitching/insert
    """
    if request.method == 'POST':
        try:
                # Get form data in parametrized format
            print("Entered insert_record")
            print(request.form)
            col_val_pairs = {
                # ID is auto-incremented but we need to add it column name to the query
                'ID': None,
                'playerID': request.form['playerID'],
                'yearID': request.form['yearID'],
                'stint': request.form['stint'],
                'team_id': request.form['team_id'],
                'lgID': request.form['lgID'],
                'W': request.form['W'],
                'L': request.form['L'],
                'G': request.form['G'],
                'GS': request.form['GS'],
                'CG': request.form['CG'],
                'SHO': request.form['SHO'],
                'SV': request.form['SV'],
                'IPouts': request.form['IPouts']
            }

            print(col_val_pairs)

            # Query building for table
            query = Query().INSERT_INTO('pitching').VALUES(col_val_pairs)
            queryString = query.BUILD()
            print(query._PARAMS)
            print(queryString)
            db.execute(queryString, tuple(query._PARAMS))
            print('Record added successfully')
        
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('pitching.view_table'))
