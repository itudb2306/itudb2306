from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.teams.table_records import TableRecords
from models.tables.teams.table_forms import FilterForm, SortForm
from models.tables.teams.details_records import DetailsRecord
from models.tables.teams.details_forms import UpdateForm, AddForm
from models.tables.teams.team_names_records import NamesRecords
from models.tables.teams.team_names_forms import NameUpdateForm, NameFilterForm, NameSortForm, NameAddForm
from utility import exceptionPage
from utility import getLeaguesList, getDivisionsList, getTeamNamesList, getParksList, getBestFielders, getBestPitchers, getBestBatters
import urllib.parse

table_teams_blueprint = Blueprint('teams', __name__)


@table_teams_blueprint.route('/teams', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/teams?p=
    """

   # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Rrequest from form
    request_form = request.form.to_dict()

    # Filter arguments from the previous request:
    filter_request_from_prev = request.args.get('filter', None, type=str)
    filter_dict = urllib.parse.parse_qsl(filter_request_from_prev)
    filter_dict = dict(filter_dict)
    filter = FilterForm().from_dict(filter_dict)
    filter_dict = filter.to_dict()
    print(f"Filter request from previous page: {filter.to_dict()}")

    # Filter arguments from the new request:
    filter_request_from_form = FilterForm().from_dict(request_form)
    if not filter_request_from_form.is_empty():
        filter = filter_request_from_form
        filter_dict = filter.to_dict()
        print(f"Filter request from form: {filter.to_dict()}")

    # Construct the filter string
    filter_string = filter.to_and_string()

    # Sorting argıuments from the previous request:
    sort = request.args.get('sort', None, type=str)
    sort_dict = urllib.parse.parse_qsl(sort)
    sort_dict = dict(sort_dict)
    sort = SortForm().from_dict(sort_dict)
    sort_dict = sort.to_dict()
    print(f"Sort request from previous page: {sort.to_dict()}")

    # Sorting arguments from the new request:
    sort_request_from_form = SortForm().from_dict(request_form)
    if not sort_request_from_form.is_empty():
        sort = sort_request_from_form
        sort_dict = sort.to_dict()
        print(f"Sort request from form: {sort.to_dict()}")

    # Construct the sort string
    sort_string = sort.to_and_string()

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('teams_easy').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                    RECORDS_PER_PAGE).BUILD()
    try:
        result = db.fetchall(query)
    except Exception as e:
        return exceptionPage(e)

    # Query building for total pages
    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('teams_easy').WHERE(filter_string).BUILD()
    try:
        total_pages = db.fetchone(total_pages_query)[0]
    except Exception as e:
        return exceptionPage(e)

    total_pages = total_pages // RECORDS_PER_PAGE + 1
    try:
        leagues_list = getLeaguesList()
        divisions_list = getDivisionsList()
        teams_list = getTeamNamesList()
        parks_list = getParksList()
    except Exception as e:
        return exceptionPage(e)

    data = TableRecords()
    data.from_list(result)
    print(f"Records length: {len(data.records)}")

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict)
    sort_encoded = urllib.parse.urlencode(sort_dict)

    return render_template('table_teams/table_teams.html', data_list=data.records, current_page=page, total_pages=total_pages, leagues_list=leagues_list,
                           divisions_list=divisions_list, teams_list=teams_list, parks_list=parks_list, filter=filter_encoded, sort=sort_encoded)


@table_teams_blueprint.route('/teams/details/<string:ID>', methods=['GET', 'POST'])
def view_details(ID):
    """
    URL: /tables/teams/details/<int:ID>
    """

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('teams_details').WHERE('ID = %s' % ID).BUILD()
    try:
        result = db.fetchall(query)
    except Exception as e:
        return exceptionPage(e)

    data = DetailsRecord()
    data.from_list(result[0])

    try:
        leagues_list = getLeaguesList()
        divisions_list = getDivisionsList()
        teams_list = getTeamNamesList()
        parks_list = getParksList()
        best_fielders = getBestFielders(data.team_name_ID, data.year)
        best_pitchers = getBestPitchers(data.team_name_ID, data.year)
        best_batters = getBestBatters(data.team_name_ID, data.year)
    except Exception as e:
        return exceptionPage(e)

    return render_template('table_teams/teams_details.html', data=data, leagues_list=leagues_list, divisions_list=divisions_list, teams_list=teams_list,
                           parks_list=parks_list, best_fielders=best_fielders, best_pitchers=best_pitchers, best_batters=best_batters)


@table_teams_blueprint.route('/teams/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/teams/update/<string:ID>
    """
    if request.method == 'POST' and ID is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)

        # Get column-value pairs to use in SET clause
        set_string = form.to_set_string()

        # Query building
        query = Query().UPDATE('teams').SET(set_string).WHERE(
            'ID = %s' % ID).BUILD()

        vals_tuple = form.to_tuple()

        # Execute query
        try:
            db.execute(query, vals_tuple)
        except Exception as e:
            return exceptionPage(e)

        print('Record updated: ', ID)

    return redirect(url_for('teams.view_details', ID=ID))


@table_teams_blueprint.route('/teams/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID=None):
    """
    URL: /tables/teams/delete/<string:ID>
    """
    other_args = request.args.to_dict()

    # Query building
    query = Query().DELETE().FROM('teams').WHERE("ID = %s").BUILD()

    # Execute query
    try:
        db.execute(query, (ID,))
    except Exception as e:
        return exceptionPage(e)

    print('Record updated: ', ID)

    return redirect(url_for('teams.view_table', **other_args))


@table_teams_blueprint.route('/teams/add', methods=['GET', 'POST'])
def add_record():
    """
    URL: /tables/teams/add
    """
    other_args = request.args.to_dict()

    form = AddForm().from_dict(request.form)

    if request.method == 'POST':
        # Get form data in parametrized format
        col_val_pairs = form.to_dict()

        # Query building for table
        query = Query().INSERT_INTO_MANUAL('teams', col_val_pairs)
        query_string = query.BUILD()

        try:
            db.execute(query_string, tuple(query._PARAMS))
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('teams.view_table', **other_args))


@table_teams_blueprint.route('/teamnames', methods=['GET', 'POST'])
def view_team_names():
    """
    URL: /tables/teamnames?p=
    """

   # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Rrequest from form
    request_form = request.form.to_dict()

    # Filter arguments from the previous request:
    filter_request_from_prev = request.args.get('filter', None, type=str)
    filter_dict = urllib.parse.parse_qsl(filter_request_from_prev)
    filter_dict = dict(filter_dict)
    filter = NameFilterForm().from_dict(filter_dict)
    filter_dict = filter.to_dict()
    print(f"Filter request from previous page: {filter.to_dict()}")

    # Filter arguments from the new request:
    filter_request_from_form = NameFilterForm().from_dict(request_form)
    if not filter_request_from_form.is_empty():
        filter = filter_request_from_form
        filter_dict = filter.to_dict()
        print(f"Filter request from form: {filter.to_dict()}")

    # Construct the filter string
    filter_string = filter.to_and_string()

    # Sorting argıuments from the previous request:
    sort = request.args.get('sort', None, type=str)
    sort_dict = urllib.parse.parse_qsl(sort)
    sort_dict = dict(sort_dict)
    sort = NameSortForm().from_dict(sort_dict)
    sort_dict = sort.to_dict()
    print(f"Sort request from previous page: {sort.to_dict()}")

    # Sorting arguments from the new request:
    sort_request_from_form = NameSortForm().from_dict(request_form)
    if not sort_request_from_form.is_empty():
        sort = sort_request_from_form
        sort_dict = sort.to_dict()
        print(f"Sort request from form: {sort.to_dict()}")

    # Construct the sort string
    sort_string = sort.to_and_string()

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('team_names_count').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                          RECORDS_PER_PAGE).BUILD()
    try:
        result = db.fetchall(query)
    except Exception as e:
        return exceptionPage(e)

    # Query building for total pages
    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('team_names_count').WHERE(filter_string).BUILD()
    try:
        total_pages = db.fetchone(total_pages_query)[0]
    except Exception as e:
        return exceptionPage(e)

    total_pages = total_pages // RECORDS_PER_PAGE + 1

    data = NamesRecords()
    data.from_list(result)
    print(f"Records length: {len(data.records)}")

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict)
    sort_encoded = urllib.parse.urlencode(sort_dict)

    return render_template('table_teams/table_team_names.html', data_list=data.records, current_page=page,
                           total_pages=total_pages, filter=filter_encoded, sort=sort_encoded)


@table_teams_blueprint.route('/teamnames/update/<string:ID>', methods=['GET', 'POST'])
def names_update_record(ID=None):
    """
    URL: /tables/teamnames/update/<string:ID>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and ID is not None:
        # Get form data
        form = NameUpdateForm().from_dict(request.form)
        print(form.to_dict())

        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('teamnames').SET(col_val_pairs).WHERE(
            'ID = \'%s\'' % ID).BUILD()

        vals_tuple = form.to_tuple()

        # Execute query
        try:
            db.execute(query, vals_tuple)
        except Exception as e:
            return exceptionPage(e)

        print('Record updated: ', ID)

    return redirect(url_for('teams.view_team_names', **other_args))


@table_teams_blueprint.route('/teamnames/delete/<string:ID>', methods=['GET', 'POST'])
def names_delete_record(ID=None):
    """
    URL: /tables/teamnames/delete/<string:ID>
    """
    other_args = request.args.to_dict()

    # Query building
    query = Query().DELETE().FROM('teamnames').WHERE("ID = %s").BUILD()

    # Execute query
    try:
        db.execute(query, (ID,))
    except Exception as e:
        return exceptionPage(e)

    print('Record updated: ', ID)

    return redirect(url_for('teams.view_team_names', **other_args))


@table_teams_blueprint.route('/teamnames/add', methods=['GET', 'POST'])
def names_add_record():
    """
    URL: /tables/teamnames/add
    """
    other_args = request.args.to_dict()

    form = NameAddForm().from_dict(request.form)

    if request.method == 'POST':
        # Get form data in parametrized format
        col_val_pairs = form.to_dict()

        # Query building for table
        query = Query().INSERT_INTO('teamnames').VALUES(col_val_pairs)

        query_string = query.BUILD()
        try:
            db.execute(query_string, form.to_tuple())
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('teams.view_team_names', **other_args))
