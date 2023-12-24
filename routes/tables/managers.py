import random
import string
from flask import Blueprint, flash, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.managers.records import Records
from models.tables.managers.forms import UpdateForm, FilterForm, SortForm, AddForm
import urllib.parse

from utility import exceptionPage, getLeaguesList, getPlayersList, getTeamNamesList

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_managers_blueprint = Blueprint('managers', __name__)

@table_managers_blueprint.route('/managers', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/managers?p=
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
    query = Query().SELECT('managers.ID AS ID, people.nameFirst AS nameFirst, people.nameLast AS nameLast, managers.yearID AS yearID, teamnames.name AS team_ID, leagues.league AS league, managers.inseason AS inseason, managers.G AS G, managers.W AS W, managers.L AS L, managers.plyrMgr AS plyrMgr').FROM('managers ').JOIN('people', 'managers.playerID = people.playerID ').JOIN('teamnames', 'managers.team_ID = teamnames.ID ').JOIN('leagues', 'managers.lgID = leagues.lgID').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
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
    total_pages_query = Query().SELECT('COUNT(*)').FROM('managers ').JOIN('people', 'managers.playerID = people.playerID ').JOIN('teamnames', 'managers.team_ID = teamnames.ID').WHERE(filter_string).BUILD()
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
        
    return render_template('table_managers/table_managers.html', data_list=data.records, current_page = page, total_pages = total_pages, filter = filter_encoded, sort = sort_encoded, players_list = players_list, teams_list = teams_list, leagues_list = leagues_list)


@table_managers_blueprint.route('/managers/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID = None):
    """
    URL: /tables/managers/update/<string:ID>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and ID is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)
        print(form.to_dict())

        # Get column-value pairs to use in SET clause
        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('managers').SET(col_val_pairs).WHERE('ID = \'%s\'' % ID).BUILD()
        # UPDATE managers SET nameFirst = 'John', nameLast = 'Doe' ... WHERE playerID = 'johndoe01'
        print(query)
        flash(query, 'admin') # display query on page
        col_val_tuple = form.to_tuple()
        print(col_val_tuple)
        db.execute(query, col_val_tuple)

        print('Record updated: ', ID)

    return redirect(url_for('managers.view_table', **other_args))


@table_managers_blueprint.route('/managers/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID=None):
    """
    URL: /tables/managers/delete/<string:ID>
    """
    other_args = request.args.to_dict()

    # Query building
    query = Query().DELETE().FROM('managers').WHERE("ID = %s").BUILD()

    # Execute query
    try:
        db.execute(query, (ID,))
    except Exception as e:
        return exceptionPage(e)

    print('Record updated: ', ID)

    return redirect(url_for('managers.view_table', **other_args))


@table_managers_blueprint.route('/managers/add', methods=['GET', 'POST'])
def add_record():
    """
    URL: /tables/managers/add
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
        query = Query().INSERT_INTO('managers (playerID, yearID, team_ID, lgID, inseason, G, W, L, plyrMgr)').VALUES(col_val_pairs).BUILD()

        query_string = query.BUILD()

        try:
            db.execute(query_string, col_val_tuple)
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('managers.view_table', **other_args))
