from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user
from database import db, Query

from models.forum.topics.records import Records as TopicRecords
from models.forum.topics.forms import UpdateForm as TopicUpdateForm, FilterForm as TopicFilterForm, SortForm as TopicSortForm
from models.forum.posts.records import Records as PostRecords
from models.forum.posts.forms import UpdateForm as PostUpdateForm
import urllib.parse
from datetime import datetime

RECORDS_PER_PAGE = 5


forum_blueprint = Blueprint('forum', __name__)

@forum_blueprint.route('/', methods=['GET', 'POST'])
def view_table():
    """
    URL: /forum/forum?p=
    """
    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE


    # Request from form
    request_form = request.form.to_dict()
    print(request_form)


    # Filtering
    filter_request_from_prev = request.args.get('filter', None, type=str) # filter=nameFirst=John&nameLast=Doe&...
    filter_dict = urllib.parse.parse_qsl(filter_request_from_prev) # [('nameFirst', 'John'), ('nameLast', 'Doe'), ...]
    filter_dict = dict(filter_dict) # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    filter = TopicFilterForm().from_dict(filter_dict) # TopicFilterForm object
    filter_dict = filter.to_dict() # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
    print("Filter request from previous page: ", filter_dict)

    filter_request_from_form = TopicFilterForm().from_dict(request_form) # TopicFilterForm object
    if not filter_request_from_form.is_empty(): # if not empty
        filter = filter_request_from_form # update filter
        filter_dict = filter.to_dict() # {'nameFirst': 'John', 'nameLast': 'Doe', ...}
        print("Filter request from form: ", filter_dict)

    filter_string = filter.to_and_string() # nameFirst = 'John' AND nameLast = 'Doe' AND ...


    # Sorting
    sort = request.args.get('sort', None, type=str) # sort=nameFirst=ASC&nameLast=DESC&...
    sort_dict = urllib.parse.parse_qsl(sort) # [('nameFirst', 'ASC'), ('nameLast', 'DESC'), ...]
    sort_dict = dict(sort_dict) # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    sort = TopicSortForm().from_dict(sort_dict) # TopicSortForm object
    sort_dict = sort.to_dict() # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
    print("Sort request from previous page: ", sort_dict)

    sort_request_from_form = TopicSortForm().from_dict(request_form) # TopicSortForm object
    if not sort_request_from_form.is_empty(): # if not empty
        sort = sort_request_from_form # update sort
        sort_dict = sort.to_dict() # {'nameFirst': 'ASC', 'nameLast': 'DESC', ...}
        print("Sort request from form: ", sort_dict)

    sort_string = sort.to_and_string() # nameFirst ASC, nameLast DESC, ...


    # Query building for table
    query = Query().SELECT('*').FROM('topic_view').WHERE(filter_string).ORDER_BY(sort_string).LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    flash(query, 'admin') # display query on page
    result = db.fetchall(query)
    print(result)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('topic_view').WHERE(filter_string).BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)
    flash(total_pages_query, 'admin') # display query on page

    data = TopicRecords()
    data.from_list(result)
    print("TopicRecords length: ", len(data.records))

    # Encode filter and sort to pass to template as one string
    filter_encoded = urllib.parse.urlencode(filter_dict) # nameFirst=John&nameLast=Doe&...
    sort_encoded = urllib.parse.urlencode(sort_dict) # nameFirst=ASC&nameLast=DESC&...
        
    return render_template('forum/forum_page/forum_page.html', data_list=data.records, current_page = page, total_pages = total_pages, filter = filter_encoded, sort = sort_encoded)

@forum_blueprint.route('/forum/topic', methods=['GET', 'POST'])
def view_topic(topic_id = None):
    """
    URL: /tables/discussions/topic/<int:topic_id>
    """

    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE


    if topic_id is None:
        topic_id = request.args.get('topic_id', None, type=int)
    if topic_id is None:
        flash("Topic does not exist", 'error')
        print("Topic does not exist")
        return redirect(url_for('forum.view_table'))

    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    get_title_and_author = Query().SELECT('title, userName').FROM('topic_view').WHERE('topicID = \'%s\'').BUILD()
    print(get_title_and_author)
    flash(get_title_and_author, 'admin')
    title_and_author = db.fetchone(get_title_and_author, (topic_id,))
    print(title_and_author)
    if title_and_author is None:
        flash("Topic does not exist", 'error')
        print("Topic does not exist")
        return redirect(url_for('forum.view_table'))
    
    topic_title, topic_author = title_and_author

    # Query building for table
    query = Query().SELECT('*').FROM('post_view').WHERE('topicID = \'%s\'').LIMIT(first_record, RECORDS_PER_PAGE).BUILD()
    print(query)
    flash(query, 'admin')
    result = db.fetchall(query, (topic_id,))
    print(result)

    # Query building for total pages
    total_pages_query = Query().SELECT('COUNT(*)').FROM('post_view').WHERE('topicID = \'%s\'').BUILD()
    total_pages = db.fetchone(total_pages_query, (topic_id,))[0]
    print("Total records:", total_pages)
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)
    flash(total_pages_query, 'admin')
    print("Total pages: ", total_pages)

    data_list = PostRecords()
    data_list.from_list(result)
    print("PostRecords length: ", len(data_list.records))

    return render_template('forum/topic_page/topic_page.html', data_list=data_list.records, current_page = page, total_pages = total_pages, topicID = topic_id, topic_title = topic_title, topic_author = topic_author)


@forum_blueprint.route('/forum/create_topic', methods=['GET', 'POST'])
def create_topic():
    """
    URL: /forum/create_topic
    """
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to create a topic", 'error')
        print("You must be logged in to create a topic")
        return redirect(url_for('forum.view_table'))
    
    title = request.form.get('title')
    content = request.form.get('content')

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and topic exists
    check_topic = Query().SELECT('topicID').FROM('topics').WHERE('title = %s AND userID = %s').BUILD()
    print(check_topic)
    topic_id = db.fetchone(check_topic, (title, user_id,))
    if topic_id is not None:
        flash("Topic already exists", 'error')
        print("Topic already exists")
        return redirect(url_for('forum.view_table'))

    create_time = datetime.now()
    insert_topic = Query().INSERT_INTO('topics (userID, title, create_time)').VALUES({'userID': '%s', 'title': '%s', 'create_time': '%s'}).BUILD()
    print(insert_topic)
    flash(insert_topic, 'admin') # display query on page
    db.execute(insert_topic, (user_id, title, create_time,))

    # Get topic id
    get_topic_id = Query().SELECT('topicID').FROM('topics').WHERE('title = %s AND userID = %s').BUILD()
    topic_id = db.fetchone(get_topic_id, (title, user_id,))[0]
    print("Topic ID: ", topic_id)

    insert_post = Query().INSERT_INTO('posts (userID, topicID, content, create_time)').VALUES({'userID': '%s', 'topicID': '%s', 'content': '%s', 'create_time': '%s'}).BUILD()
    print(insert_post)
    flash(insert_post, 'admin') # display query on page
    db.execute(insert_post, (user_id, topic_id, content, create_time,))
    flash("Topic created", 'success')
    return redirect(url_for('forum.view_topic', topic_id=topic_id))

@forum_blueprint.route('/forum/update_topic', methods=['GET', 'POST'])
def update_topic():
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to update a topic", 'error')
        print("You must be logged in to update a topic")
        return redirect(url_for('forum.view_table'))
    
    topicID = request.form.get('topicID')
    title = request.form.get('title')
    print("topicID:", topicID)

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and topic author match
    check_topic = Query().SELECT('userID').FROM('topics').WHERE('topicID = %s').BUILD()
    print(check_topic)
    topic_author_id = db.fetchone(check_topic, (topicID,))
    if topic_author_id is None:
        flash("Topic does not exist", 'error')
        print("Topic does not exist")
        return redirect(url_for('forum.view_table'))
    topic_author_id = topic_author_id[0]
    print("Topic author ID: ", topic_author_id)
    
    if topic_author_id != user_id and not current_user.is_admin:
        flash("You are not the author of this topic", 'error')
        print("You are not the author of this topic")
        return redirect(url_for('forum.view_table'))
    
    update_topic = Query().UPDATE('topics').SET('title = %s').WHERE('topicID = %s').BUILD()
    print(update_topic)
    flash(update_topic, 'admin') # display query on page
    db.execute(update_topic, (title, topicID,))
    flash("Topic updated", 'success')

    return redirect(url_for('forum.view_topic', topic_id=topicID))


@forum_blueprint.route('/forum/delete_topic', methods=['GET', 'POST'])
def delete_topic():
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to delete a topic", 'error')
        print("You must be logged in to delete a topic")
        return redirect(url_for('forum.view_table'))
    
    topicID = request.form.get('topicID')

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and topic author match
    check_topic = Query().SELECT('userID').FROM('topics').WHERE('topicID = %s').BUILD()
    print(check_topic)
    topic_author_id = db.fetchone(check_topic, (topicID,))
    if topic_author_id is None:
        flash("Topic does not exist", 'error')
        print("Topic does not exist")
        return redirect(url_for('forum.view_table'))
    topic_author_id = topic_author_id[0]
    print("Topic author ID: ", topic_author_id)
    
    if topic_author_id != user_id and not current_user.is_admin:
        flash("You are not the author of this topic", 'error')
        print("You are not the author of this topic")
        return redirect(url_for('forum.view_table'))
    
    delete_topic = Query().DELETE().FROM('topics').WHERE('topicID = %s').BUILD()
    print(delete_topic)
    flash(delete_topic, 'admin') # display query on page
    db.execute(delete_topic, (topicID,))
    flash("Topic deleted", 'success')

    return redirect(url_for('forum.view_table'))


@forum_blueprint.route('/forum/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to create a post", 'error')
        print("You must be logged in to create a post")
        return redirect(url_for('forum.view_table'))
    
    topicID = request.form.get('topicID')
    content = request.form.get('content')

    print("Topic ID: ", topicID)
    print("Content: ", content)

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and topic exists
    check_topic = Query().SELECT('topicID').FROM('topic_view').WHERE('topicID = %s').BUILD()
    print(check_topic)
    topic_id = db.fetchone(check_topic, (topicID,))
    if topic_id is None:
        flash("Topic does not exist", 'error')
        print("Topic does not exist")
        return redirect(url_for('forum.view_table'))
    
    create_time = datetime.now()
    insert_post = Query().INSERT_INTO('posts (userID, topicID, content, create_time)').VALUES({'userID': '%s', 'topicID': '%s', 'content': '%s', 'create_time': '%s'}).BUILD()
    print(insert_post)
    flash(insert_post, 'admin') # display query on page
    db.execute(insert_post, (user_id, topicID, content, create_time,))
    flash("Post created", 'success')
    return redirect(url_for('forum.view_topic', topic_id=topicID))


@forum_blueprint.route('/forum/update_post', methods=['GET', 'POST'])
def update_post():
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to update a post", 'error')
        print("You must be logged in to update a post")
        return redirect(url_for('forum.view_table'))
    
    topicID = request.form.get('topicID')
    postID = request.form.get('postID')
    content = request.form.get('content')

    print("Topic ID: ", topicID)
    print("Post ID: ", postID)
    print("Content: ", content)

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and post author match
    check_post = Query().SELECT('userID').FROM('post_view').WHERE('postID = %s').BUILD()
    print(check_post)
    post_author_id = db.fetchone(check_post, (postID,))
    if post_author_id is None:
        flash("Post does not exist", 'error')
        print("Post does not exist")
        return redirect(url_for('forum.view_table'))
    # (1,) -> 1
    post_author_id = post_author_id[0]
    print("Post author ID: ", post_author_id)
    
    if str(post_author_id) != str(user_id) and not current_user.is_admin:
        print("You are not the author of this post")
        flash("You are not the author of this post", 'error')
        return redirect(url_for('forum.view_table'))
    
    update_post = Query().UPDATE('posts').SET('content = %s').WHERE('postID = %s').BUILD()
    print(update_post)
    flash(update_post, 'admin') # display query on page
    db.execute(update_post, (content, postID,))
    flash("Post updated", 'success')

    return redirect(url_for('forum.view_topic', topic_id=topicID))


@forum_blueprint.route('/forum/delete_post', methods=['GET', 'POST'])
def delete_post():
    if request.method == 'GET':
        print("GET")
        return redirect(url_for('forum.view_table'))
    
    if not current_user.is_authenticated:
        flash("You must be logged in to delete a post", 'error')
        print("You must be logged in to delete a post")
        return redirect(url_for('forum.view_table'))
    
    topicID = request.form.get('topicID')
    postID = request.form.get('postID')

    get_user = Query().SELECT('userID').FROM('users').WHERE('userName = %s').BUILD()
    print(get_user)
    user_id = db.fetchone(get_user, (current_user.username,))[0]
    print("User ID: ", user_id)

    # Check if user and post author match
    check_post = Query().SELECT('userID').FROM('post_view').WHERE('postID = %s').BUILD()
    print(check_post)
    post_author_id = db.fetchone(check_post, (postID,))
    if post_author_id is None:
        flash("Post does not exist", 'error')
        print("Post does not exist")
        return redirect(url_for('forum.view_table'))
    post_author_id = post_author_id[0]
    print("Post author ID: ", post_author_id)
    
    if str(post_author_id) != str(user_id) and not current_user.is_admin:
        print("You are not the author of this post")
        flash("You are not the author of this post", 'error')
        return redirect(url_for('forum.view_table'))
    
    delete_post = Query().DELETE().FROM('posts').WHERE('postID = %s').BUILD()
    print(delete_post)
    flash(delete_post, 'admin') # display query on page
    db.execute(delete_post, (postID,))
    flash("Post deleted", 'success')

    return redirect(url_for('forum.view_topic', topic_id=topicID))