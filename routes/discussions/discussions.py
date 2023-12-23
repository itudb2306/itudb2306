from flask import Blueprint, flash, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE
from models.tables.people.records import Records
from models.tables.people.forms import UpdateForm, FilterForm, SortForm
import urllib.parse
from datetime import datetime


discussions_blueprint = Blueprint('discussions', __name__)

@discussions_blueprint.route('/discussions', methods=['GET', 'POST'])
def view_table():
    """
    URL: /tables/discussions?p=
    """
    
    test_data = [{"title": "Test Title", "author": "Test Author", "date_created": datetime(2020, 1, 1, 0, 0, 0), "last_message": "Test Last Message", "last_message_author": "Test Last Message Author", "last_message_date": datetime(2020, 1, 1, 0, 0, 0), "replies": 0, "id": 0}, {"title": "Test Title", "author": "Test Author", "date_created": datetime(2020, 1, 1, 0, 0, 0), "last_message": "Test Last Message", "last_message_author": "Test Last Message Author", "last_message_date": datetime(2020, 1, 1, 0, 0, 0), "replies": 0, "id": 0}, {"title": "Test Title", "author": "Test Author", "date_created": datetime(2020, 1, 1, 0, 0, 0), "last_message": "Test Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last MessageTest Last Message", "last_message_author": "Test Last Message Author", "last_message_date": datetime(2020, 1, 1, 0, 0, 0), "replies": 0, "id": 0}]
    return render_template('discussions/discussions_all.html', data_list=test_data, current_page=1, total_pages=1)



@discussions_blueprint.route('/discussions', methods=['GET', 'POST'])
def view_table_2():
    """
    URL: /discussions/discussions?p=
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
    """
    Select query:
    SELECT d.discussionID, d.userID AS creatorID, u.name AS creator_name, d.title, d.created_at, d.last_messageID, m.userID AS last_message_userID, u2.name AS last_message_user_name, m.message AS last_message, m.created_at AS last_message_created_at
    """
    query = Query().SELECT('d.discussionID, d.userID AS creatorID, u.name AS creator_name, d.title, d.created_at, d.last_messageID, m.userID AS last_message_userID, u2.name AS last_message_user_name, m.message AS last_message, m.created_at AS last_message_created_at').FROM('discussions d ').JOIN('messages m', 'd.last_messageID = m.messageID').JOIN('users u', 'd.userID = u.userID').JOIN('users u2', 'm.userID = u2.userID').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    flash(query, 'admin') # display query on page
    result = db.fetchall(query)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').WHERE(filter_string).FROM('discussions').BUILD()
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
        
    return render_template('table_discussions/table_discussions.html', data_list=data.records, current_page = page, total_pages = total_pages, filter = filter_encoded, sort = sort_encoded)