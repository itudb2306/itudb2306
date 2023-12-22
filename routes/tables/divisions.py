from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.divisions.records import Records
from models.tables.divisions.forms import UpdateForm, FilterForm, SortForm, AddForm
from utility import exceptionPage, getLeaguesList, checkDivisionsViewExists
import urllib.parse

table_divisions_blueprint = Blueprint('divisions', __name__)


@table_divisions_blueprint.route('/divisions', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/divisions?p=
    """
    # Check if the view exists, if not so, create it.
    checkDivisionsViewExists()

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
    query = Query().SELECT('*').FROM('divisions_leagues').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record,
                                                                                                           RECORDS_PER_PAGE).BUILD()
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT(
        'COUNT(*)').FROM('divisions_leagues').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1

    leagues_list = getLeaguesList()

    data = Records()
    data.from_list(result)
    print(f"Records length: {len(data.records)}")

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict)
    sort_encoded = urllib.parse.urlencode(sort_dict)

    return render_template('table_divisions/table_divisions.html', data_list=data.records, current_page=page, total_pages=total_pages, leagues_list=leagues_list, filter=filter_encoded, sort=sort_encoded)


@table_divisions_blueprint.route('/divisions/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/divisions/update/<string:ID>
    """
    other_args = request.args.to_dict()

    if request.method == 'POST' and ID is not None:
        # Get form data
        form = UpdateForm().from_dict(request.form)
        print(form.to_dict())

        # Get column-value pairs to use in SET clause
        col_val_pairs = form.to_dict()

        # Query building
        query = Query().UPDATE('divisions').SET(col_val_pairs).WHERE(
            'ID = %s' % ID).BUILD()

        vals_tuple = form.to_tuple()

        try:
            db.execute(query, vals_tuple)
        except Exception as e:
            return exceptionPage(e)

        print('Record updated: ', ID)

    return redirect(url_for('divisions.view_table', **other_args))


@table_divisions_blueprint.route('/divisions/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID=None):
    """
    URL: /tables/divisions/delete/<string:ID>
    """
    other_args = request.args.to_dict()

    # Query building
    query = Query().DELETE().FROM('divisions').WHERE("ID = %s").BUILD()

    # Execute query
    try:
        db.execute(query, (ID,))
    except Exception as e:
        return exceptionPage(e)

    print('Record updated: ', ID)

    return redirect(url_for('divisions.view_table', **other_args))


@table_divisions_blueprint.route('/divisions/add', methods=['GET', 'POST'])
def add_record():
    """
    URL: /tables/divisions/add
    """
    other_args = request.args.to_dict()

    form = AddForm().from_dict(request.form)

    if request.method == 'POST':
        # Get form data in parametrized format
        col_val_pairs = form.to_dict()

        # Query building for table
        query = Query().INSERT_INTO('divisions').VALUES(col_val_pairs)

        query_string = query.BUILD()

        try:
            db.execute(query_string, form.to_tuple())
        except Exception as e:
            return exceptionPage(e)

    return redirect(url_for('divisions.view_table', **other_args))
