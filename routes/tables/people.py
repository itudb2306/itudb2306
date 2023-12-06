from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.people.records import Records
from models.tables.people.forms import UpdateForm, FilterForm

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

    # Searching / Filtering

    # Get parameter arguments from previous request
    arg_dict = request.args.to_dict()
    filter = FilterForm().from_dict(arg_dict)
    filter_string = filter.to_and_string()
    filter_dict = filter.to_dict()
    print("Filter request from previous page: ", filter.to_dict())
    
    # Get form data
    filter = FilterForm().from_dict(request.form)

    if filter.to_and_string() != '':
        print("Filter request from filter form: ", filter.to_dict())
        # Get column-value pairs to use in WHERE clause
        filter_string = filter.to_and_string()
        filter_dict = filter.to_dict()

    # Query building for table
    query = Query().SELECT('*').FROM('people').WHERE(filter_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').WHERE(filter_string).FROM('people').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data = Records()
    data.from_list(result)
    print("Records length: ", len(data.records))
        
    return render_template('table_people/table_people.html', data_list=data.records, current_page = page, total_pages = total_pages, search_val = "", **filter_dict)


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
        db.execute(query)

        print('Record updated: ', player_id)

    return redirect(url_for('people.view_table', **other_args))