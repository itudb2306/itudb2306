from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.homegames.records import Records
from models.tables.homegames.forms import UpdateForm, FilterForm, SortForm
from routes.tables.teams import getLeaguesList, getParksList, getTeamNamesList
from utility import logQuery
import urllib.parse

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""


def checkHomegamesViewExists():
    if not db.checkTableExists('homegames_easy'):
        teams_easy_query = """
        create view homegames_easy as 
        select 
            h.ID as ID,
            h.yearkey as year,
            l.league as league,
            tn.name as team_name,
            p.parkname as park_name,
            h.games as games,
            h.openings as openings,
            h.attendance as attendance,
            h.spanfirst_date as spanfirst_date,
            h.spanlast_date as spanlast_date
            tn.ID as team_ID,
            l.lgID as lgID,
            p.ID as park_ID
        from homegames h
        left join teamnames tn on tn.ID = h.team_ID
        left join parks p on p.ID = h.park_ID
        left join leagues l on h.leaguekey = l.lgID;
        """
        db.execute(teams_easy_query, None)


table_homegames_blueprint = Blueprint('homegames', __name__)


@table_homegames_blueprint.route('/homegames', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/parks?p=
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

    # Query for table
    query = Query().SELECT('*').FROM('homegames_easy').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                        RECORDS_PER_PAGE).BUILD()
    logQuery(query)
    result = db.fetchall(query)

    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('homegames_easy').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    logQuery(total_pages_query)

    data = Records()
    data.from_list(result)
    logQuery(f"Records length: {len(data.records)}")

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict)
    sort_encoded = urllib.parse.urlencode(sort_dict)

    leagues_list = getLeaguesList()
    teams_list = getTeamNamesList()
    parks_list = getParksList()

    return render_template('table_homegames/table_homegames.html', data_list=data.records, current_page=page, total_pages=total_pages,
                           leagues_list=leagues_list, teams_list=teams_list, parks_list=parks_list, filter=filter_encoded, sort=sort_encoded)


@table_homegames_blueprint.route('/homegames/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/parks/update/<string:ID>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and ID is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)
        logQuery(form.to_dict())

        # Get column-value pairs to use in SET clause
        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('homegames').SET(col_val_pairs).WHERE(
            'ID = %s' % ID).BUILD()

        vals_tuple = form.to_tuple()
        # None values are generating problems for logging
        logQuery(query % vals_tuple)

        # Execute query
        db.execute(query, vals_tuple)
        print('Record updated: ', ID)

    return redirect(url_for('homegames.view_table', **other_args))
