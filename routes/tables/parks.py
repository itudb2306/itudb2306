from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.parks.records import Records
from models.tables.parks.forms import UpdateForm, FilterForm
from utility import logQuery

"""
ATTENTION:
    This route is not finished yet. It is just an initial template for the team to create the routes for the tables.
"""

table_parks_blueprint = Blueprint('parks', __name__)


@table_parks_blueprint.route('/parks', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/parks?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Filter arguments from the previous request:
    arg_dict = request.args.to_dict()
    filter = FilterForm().from_dict(arg_dict)
    filter_string = filter.to_and_string()
    filter_dict = filter.to_dict()
    logQuery(f"Filter request from previous page: {filter.to_dict()}")

    # Filter arguments from the new request:
    filter = FilterForm().from_dict(request.form)
    if filter.to_and_string() != '':
        print(f"Filter request from filter form: {filter.to_dict()}")
        filter_string = filter.to_and_string()
        filter_dict = filter.to_dict()

    # Query for table
    query = Query().SELECT('*').FROM('parks').WHERE(filter_string).LIMIT(first_record,
                                                                         RECORDS_PER_PAGE).BUILD()
    logQuery(Query)
    result = db.fetchall(query)

    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('parks').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    logQuery(total_pages_query)

    data = Records()
    data.from_list(result)
    logQuery(f"Records length: {len(data.records)}")

    return render_template('table_parks/table_parks.html', data_list=data.records, current_page=page, total_pages=total_pages, **filter_dict)


@table_parks_blueprint.route('/%s/update/<string:ID>', methods=['GET', 'POST'])
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
        query = Query().UPDATE('parks').SET(col_val_pairs).WHERE(
            'ID = \'%s\'' % ID).BUILD()

        vals_tuple = form.to_tuple()
        # None values are generating problems for logging
        logQuery(query % vals_tuple)

        # Execute query
        db.execute(query, vals_tuple)
        print('Record updated: ', ID)

    return redirect(url_for('parks.view_table', **other_args))
