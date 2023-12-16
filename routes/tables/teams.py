from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.teams.table_records import TableRecords
from models.tables.teams.table_forms import FilterForm, SortForm
from utility import logQuery
import urllib.parse

table_teams_blueprint = Blueprint('teams', __name__)


def checkTeamsViewExists():
    # This view joins divisions with leagues.
    if not db.checkTableExists('teams_easy'):
        divisions_leagues_query = """
        create view teams_easy as
        select 
            t.ID as ID,
            tn.name as name,
            t.yearID as year,
            l.league as league,
            d.division as division,
            p.parkname as park,
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
        db.execute(divisions_leagues_query, None)


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
    URL: /tables/divisions?p=
    """
    # Check if the view exists, if not so, create it.
    checkTeamsViewExists()

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

    # Filter arguments from the new request:
    filter = FilterForm().from_dict(request.form)
    if filter.to_and_string() != '':
        print(f"Filter request from filter form: {filter.to_dict()}")
        filter_string = filter.to_and_string()
        filter_dict = filter.to_dict()

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
