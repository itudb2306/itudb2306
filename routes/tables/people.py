from flask import Blueprint, flash, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.people.records import Records
from models.tables.people.forms import UpdateForm, FilterForm, SortForm
import urllib.parse

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_people_blueprint = Blueprint('people', __name__)

@table_people_blueprint.route('/people', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/people?p=
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


    # Query building for table
    query = Query().SELECT('*').FROM('people').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    flash(query, 'admin') # display query on page
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').WHERE(filter_string).FROM('people').BUILD()
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
        
    return render_template('table_people/table_people.html', data_list=data.records, current_page = page, total_pages = total_pages, filter = filter_encoded, sort = sort_encoded)


@table_people_blueprint.route('/people/update/<string:player_id>', methods=['GET', 'POST'])
def update_record(player_id = None):
    """
    URL: /tables/people/update/<string:player_id>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and player_id is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)
        print(form.to_dict())

        # Get column-value pairs to use in SET clause
        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('people').SET(col_val_pairs).WHERE('playerID = \'%s\'' % player_id).BUILD()
        # UPDATE people SET nameFirst = 'John', nameLast = 'Doe' ... WHERE playerID = 'johndoe01'
        print(query)
        flash(query, 'admin') # display query on page
        col_val_tuple = form.to_tuple()
        print(col_val_tuple)
        db.execute(query, col_val_tuple)

        print('Record updated: ', player_id)

    return redirect(url_for('people.view_table', **other_args))