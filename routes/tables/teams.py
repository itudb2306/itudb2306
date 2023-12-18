from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.teams.table_records import TableRecords
from models.tables.teams.table_forms import FilterForm, SortForm
from models.tables.teams.details_records import DetailsRecord
from models.tables.teams.details_forms import UpdateForm
from models.tables.teams.team_names_records import NamesRecords
from models.tables.teams.team_names_forms import NameUpdateForm, NameFilterForm, NameSortForm
from utility import logQuery
import urllib.parse

table_teams_blueprint = Blueprint('teams', __name__)


def checkTeamsEasyViewExists():
    if not db.checkTableExists('teams_easy'):
        teams_easy_query = """
        create view teams_easy as
        select 
            t.ID as ID,
            t.teamID as team_code,
            tn.name as name,
            t.yearID as year,
            l.league as league,
            d.division as division,
            p.parkname as park,
            t.teamRank as team_rank,
            t.G as games,
            t.Ghome as home_games,
            t.W as wins,
            t.L as losses,
            t.DivWin as division_win,
            t.WCWin as wild_card_win,
            t.LgWin as league_win,
            t.WSWin as world_series_win
        from teams t
        left join leagues l on t.lgID = l.lgID
        left join divisions d on t.div_ID = d.ID
        left join teamnames tn on t.team_ID = tn.ID
        left join parks p on t.park_ID = p.ID
        """
        db.execute(teams_easy_query, None)


def checkTeamsDetailsViewExists():
    if not db.checkTableExists('teams_details'):
        teams_deatails_query = """
        create view teams_details as
        select 
            t.ID as ID,
            t.teamID as team_code,
            tn.name as name,
            tn.ID as team_name_ID,
            t.yearID as year,
            l.league as league,
            l.lgID as league_ID,
            d.division as division,
            d.ID as division_ID,
            p.parkname as park,
            p.ID as park_ID,
            t.teamRank as team_rank,
            t.G as games,
            t.Ghome as home_games,
            t.W as wins,
            t.L as losses,
            t.DivWin as division_win,
            t.WCWin as wild_card_win,
            t.LgWin as league_win,
            t.WSWin as world_series_win,
            t.R as runs_scored,
            t.AB as at_bats,
            t.H as hits,
            t.2B as doubles,
            t.3B as triples,
            t.HR as homeruns,
            t.BB as walks_batters,
            t.SO as strikeouts_batters,
            t.SB as stolen_bases,
            t.CS as caught_stealing,
            t.HBP as hit_by_pitch,
            t.SF as sacrifice_flies,
            t.RA as runs_allowed,
            t.ER as earned_runs_allowed,
            t.ERA as earned_run_average,
            t.CG as complete_games,
            t.SHO as shutouts,
            t.SV as saves,
            t.IPOuts as outs_pitched,
            t.HA as hits_allowed,
            t.HRA as homeruns_allowed,
            t.BBA as walks_allowed,
            t.SOA as strikeouts_pitchers,
            t.E as errors,
            t.DP as double_plays,
            t.FP as fielding_percentage,
            t.attendance as attendance,
            t.BPF as batter_park_factor,
            t.PPF as pitcher_park_factor
        from teams t
        left join leagues l on t.lgID = l.lgID
        left join divisions d on t.div_ID = d.ID
        left join teamnames tn on t.team_ID = tn.ID
        left join parks p on t.park_ID = p.ID
        """
        db.execute(teams_deatails_query, None)


def checkTeamsNamesViewExists():
    if not db.checkTableExists('team_names_count'):
        teams_names_count_query = """
        create view team_names_count as
        select tn1.ID as ID,
            tn1.name as name,
            tn2.cnt as cnt
        from teamnames tn1 join ( select
                teamnames.ID as ID,
                count(teamnames.ID) as cnt
                from teamnames left join teams on
                teams.team_ID = teamnames.ID
                group by teamnames.ID
        ) as tn2 on tn1.ID = tn2.ID;
        """
        db.execute(teams_names_count_query, None)


def getLeaguesList():
    # Query for division league selection
    leagues_list = []
    leagues_query = Query().SELECT('lgID, league').FROM('leagues').BUILD()
    leagues_result = db.fetchall(leagues_query)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })
    return leagues_list


def getDivisionsList():
    # Query for division league selection
    divisions_list = []
    divisions_query = Query().SELECT('ID, division').FROM('divisions').BUILD()
    divisions_result = db.fetchall(divisions_query)
    for row in divisions_result:
        divisions_list.append({'ID': row[0],
                               'division': row[1], })
    return divisions_list


def getTeamNamesList():
    # Query for division league selection
    teams_list = []
    teams_query = Query().SELECT('ID, name').FROM('teamnames').BUILD()
    teams_result = db.fetchall(teams_query)
    for row in teams_result:
        teams_list.append({'ID': row[0],
                           'name': row[1], })
    return teams_list


def getParksList():
    # Query for division league selection
    parks_list = []
    parks_query = Query().SELECT('ID, parkname').FROM('parks').BUILD()
    parks_result = db.fetchall(parks_query)
    for row in parks_result:
        parks_list.append({'ID': row[0],
                           'parkname': row[1], })
    return parks_list


@table_teams_blueprint.route('/teams', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/teams?p=
    """
    # Check if the view exists, if not so, create it.
    checkTeamsEasyViewExists()

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
    logQuery(f"Filter request from previous page: {filter.to_dict()}")

    # Filter arguments from the new request:
    filter_request_from_form = FilterForm().from_dict(request_form)
    if not filter_request_from_form.is_empty():
        filter = filter_request_from_form
        filter_dict = filter.to_dict()
        logQuery(f"Filter request from form: {filter.to_dict()}")

    # Construct the filter string
    filter_string = filter.to_and_string()

    # Sorting argıuments from the previous request:
    sort = request.args.get('sort', None, type=str)
    sort_dict = urllib.parse.parse_qsl(sort)
    sort_dict = dict(sort_dict)
    sort = SortForm().from_dict(sort_dict)
    sort_dict = sort.to_dict()
    logQuery(f"Sort request from previous page: {sort.to_dict()}")

    # Sorting arguments from the new request:
    sort_request_from_form = SortForm().from_dict(request_form)
    if not sort_request_from_form.is_empty():
        sort = sort_request_from_form
        sort_dict = sort.to_dict()
        logQuery(f"Sort request from form: {sort.to_dict()}")

    # Construct the sort string
    sort_string = sort.to_and_string()

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('teams_easy').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                    RECORDS_PER_PAGE).BUILD()
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('teams_easy').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1

    leagues_list = getLeaguesList()
    divisions_list = getDivisionsList()
    teams_list = getTeamNamesList()
    parks_list = getParksList()

    data = TableRecords()
    data.from_list(result)
    logQuery(f"Records length: {len(data.records)}")

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
    # Check if the view exists, if not so, create it.
    checkTeamsDetailsViewExists()

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('teams_details').WHERE('ID = %s' % ID).BUILD()
    result = db.fetchall(query)

    data = DetailsRecord()
    data.from_list(result[0])

    leagues_list = getLeaguesList()
    divisions_list = getDivisionsList()
    teams_list = getTeamNamesList()
    parks_list = getParksList()

    return render_template('table_teams/teams_details.html', data=data, leagues_list=leagues_list, divisions_list=divisions_list, teams_list=teams_list, parks_list=parks_list)


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
        # None values are generating problems for logging
        logQuery(query % vals_tuple)

        # Execute query
        db.execute(query, vals_tuple)
        print('Record updated: ', ID)

    return redirect(url_for('teams.view_details', ID=ID))


@table_teams_blueprint.route('/teamnames', methods=['GET', 'POST'])
def view_team_names():
    """
    URL: /tables/teamnames?p=
    """

    checkTeamsNamesViewExists()

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
    logQuery(f"Filter request from previous page: {filter.to_dict()}")

    # Filter arguments from the new request:
    filter_request_from_form = NameFilterForm().from_dict(request_form)
    if not filter_request_from_form.is_empty():
        filter = filter_request_from_form
        filter_dict = filter.to_dict()
        logQuery(f"Filter request from form: {filter.to_dict()}")

    # Construct the filter string
    filter_string = filter.to_and_string()

    # Sorting argıuments from the previous request:
    sort = request.args.get('sort', None, type=str)
    sort_dict = urllib.parse.parse_qsl(sort)
    sort_dict = dict(sort_dict)
    sort = NameSortForm().from_dict(sort_dict)
    sort_dict = sort.to_dict()
    logQuery(f"Sort request from previous page: {sort.to_dict()}")

    # Sorting arguments from the new request:
    sort_request_from_form = NameSortForm().from_dict(request_form)
    if not sort_request_from_form.is_empty():
        sort = sort_request_from_form
        sort_dict = sort.to_dict()
        logQuery(f"Sort request from form: {sort.to_dict()}")

    # Construct the sort string
    sort_string = sort.to_and_string()

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('team_names_count').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                          RECORDS_PER_PAGE).BUILD()
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('team_names_count').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1

    data = NamesRecords()
    data.from_list(result)
    logQuery(f"Records length: {len(data.records)}")

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
        # None values are generating problems for logging
        logQuery(query % vals_tuple)

        # Execute query
        db.execute(query, vals_tuple)
        print('Record updated: ', ID)

    return redirect(url_for('teams.view_team_names', **other_args))
