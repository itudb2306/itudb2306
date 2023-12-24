import random
import string
from flask import Blueprint, flash, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.appearances.records import Records
from models.tables.appearances.forms import UpdateForm, FilterForm, SortForm, AddForm
import urllib.parse

from utility import exceptionPage, getLeaguesList, getPlayersList, getTeamNamesList

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_appearances_blueprint = Blueprint('appearances', __name__)

@table_appearances_blueprint.route('/appearances', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/appearances?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE


    # Request from form
    request_form = request.form.to_dict()


    # Filtering
    filter_request_from_prev = request.args.get('filter', None, type=str) # filter=nameFirst=John&nameLast=Doe&...
    filter_dict = urllib.parse.parse_qsl(filter_request_from_prev) # [('nameFirst', 'John'), ('nameLast', 'Doe'), ...]
    filter_dict = dict(filter_dict) # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    filter = FilterForm().from_dict(filter_dict) # FilterForm object
    filter_dict = filter.to_dict() # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    print("Filter request from previous page: ", filter_dict)

    filter_request_from_form = FilterForm().from_dict(request_form) # FilterForm object
    if not filter_request_from_form.is_empty(): # if not empty
        filter = filter_request_from_form # update filter
        filter_dict = filter.to_dict() # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
        print("Filter request from form: ", filter_dict)

    filter_string = filter.to_and_string() # nameFirst = 'John' AND nameLast = 'Doe' AND ...


    # Sorting
    sort = request.args.get('sort', None, type=str) # sort=nameFirst=ASC&nameLast=DESC&...
    sort_dict = urllib.parse.parse_qsl(sort) # [('nameFirst', 'ASC'), ('nameLast', 'DESC'), ...]
    sort_dict = dict(sort_dict) # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    sort = SortForm().from_dict(sort_dict) # SortForm object
    sort_dict = sort.to_dict() # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    print("Sort request from previous page: ", sort_dict)

    sort_request_from_form = SortForm().from_dict(request_form) # SortForm object
    if not sort_request_from_form.is_empty(): # if not empty
        sort = sort_request_from_form # update sort
        sort_dict = sort.to_dict() # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
        print("Sort request from form: ", sort_dict)

    sort_string = sort.to_and_string() # nameFirst ASC, nameLast DESC, ...


    # Query building for table, join with playerID from people table
    # ID, playerID, yearID, team_ID, lgID, inseason, G, W, L, teamRank, plyrMgr
    # ID, nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
    query = Query().SELECT('appearances.ID AS ID, people.nameFirst AS nameFirst, people.nameLast AS nameLast, appearances.yearID AS yearID, teamnames.name AS team_ID, leagues.league AS league, appearances.G_all AS G_all, appearances.GS AS GS, appearances.G_batting AS G_batting, appearances.G_defense AS G_defense, appearances.G_p AS G_p, appearances.G_c AS G_c, appearances.G_1b AS G_1b, appearances.G_2b AS G_2b, appearances.G_3b AS G_3b, appearances.G_ss AS G_ss, appearances.G_lf AS G_lf, appearances.G_cf AS G_cf, appearances.G_rf AS G_rf, appearances.G_of AS G_of, appearances.G_dh AS G_dh, appearances.G_ph AS G_ph, appearances.G_pr AS G_pr').FROM('appearances ').JOIN('people', 'appearances.playerID = people.playerID ').JOIN('teamnames', 'appearances.team_ID = teamnames.ID ').JOIN('leagues', 'appearances.lgID = leagues.lgID').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    flash(query, 'admin') # display query on page
    result = db.fetchall(query)

    # Players list
    players_query = Query().SELECT('playerID, nameFirst, nameLast').FROM('people').BUILD()
    players = db.fetchall(players_query)
    print(players_query)
    flash(players_query, 'admin') # display query on page

    players_list = getPlayersList(players)

    # Teams list
    teams_list = getTeamNamesList()

    # Leagues list
    leagues_list = getLeaguesList()


    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('appearances ').JOIN('people', 'appearances.playerID = people.playerID ').JOIN('teamnames', 'appearances.team_ID = teamnames.ID').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)
    flash(total_pages_query, 'admin') # display query on page

    data = Records()
    data.from_list(result)
    print("Records length: ", len(data.records))

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict) # nameFirst=John&nameLast=Doe&...
    sort_encoded = urllib.parse.urlencode(sort_dict) # nameFirst=ASC&nameLast=DESC&...
        
    return render_template('table_appearances/table_appearances.html', data_list=data.records, current_page = page, total_pages = total_pages, filter = filter_encoded, sort = sort_encoded, players_list = players_list, teams_list = teams_list, leagues_list = leagues_list)


@table_appearances_blueprint.route('/appearances/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID = None):
    """
    URL: /tables/appearances/update/<string:ID>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and ID is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)
        print(form.to_dict())

        # Get column-value pairs to use in SET clause
        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('appearances').SET(col_val_pairs).WHERE('ID = \'%s\'' % ID).BUILD()
        # UPDATE appearances SET nameFirst = 'John', nameLast = 'Doe' ... WHERE playerID = 'johndoe01'
        print(query)
        flash(query, 'admin') # display query on page
        col_val_tuple = form.to_tuple()
        print(col_val_tuple)
        db.execute(query, col_val_tuple)

        print('Record updated: ', ID)

    return redirect(url_for('appearances.view_table', **other_args))


@table_appearances_blueprint.route('/appearances/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID=None):
    """
    URL: /tables/appearances/delete/<string:ID>
    """
    other_args = request.args.to_dict()

    # Query building
    query = Query().DELETE().FROM('appearances').WHERE("ID = %s").BUILD()

    # Execute query
    try:
        db.execute(query, (ID,))
    except Exception as e:
        return exceptionPage(e)

    print('Record updated: ', ID)

    return redirect(url_for('appearances.view_table', **other_args))


@table_appearances_blueprint.route('/appearances/add', methods=['GET', 'POST'])
def add_record():
    """
    URL: /tables/appearances/add
    """
    other_args = request.args.to_dict()
    request_form = request.form.to_dict()

   
    form = AddForm().from_dict(request.form)

    if request.method == 'POST':
        # Get form data in parametrized format
        col_val_pairs = form.to_dict()
        col_val_tuple = form.to_tuple()
        print(col_val_pairs)
        print(col_val_tuple)

        # Query building for table
        query = Query().INSERT_INTO('appearances (playerID, yearID, team_ID, lgID, inseason, G, W, L, plyrMgr)').VALUES(col_val_pairs).BUILD()

        query_string = query.BUILD()

        try:
            db.execute(query_string, col_val_tuple)
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('appearances.view_table', **other_args))
