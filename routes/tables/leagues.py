from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query
from models.tables.leagues.records import Records
from config import RECORDS_PER_PAGE

table_leagues_blueprint = Blueprint('leagues', __name__)

@table_leagues_blueprint.route('/leagues', methods=['GET'])
def view_table():
    # pagination
    page = request.args.get('page', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # query
    query = Query().SELECT('*'
    ).FROM('leagues'
    ).LIMIT(first_record, RECORDS_PER_PAGE
    ).BUILD()

    print(query)
    result = db.fetchall(query)

    # query for total records
    total_pages_query = Query().SELECT('COUNT(*)'
    ).FROM('leagues'
    ).BUILD()

    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data = Records()
    data.from_list(result)
    print(f"Records length: {len(data.records)}")

    return render_template('table_leagues/table_leagues.html', data_list = data.records, current_page = page, total_pages = total_pages)

@table_leagues_blueprint.route('/leagues/details/<string:ID>', methods=['GET', 'POST'])
def view_details(ID):
    query = Query().SELECT('*'
    ).FROM('leagues'
    ).WHERE(f"lgID = '{ID}'"
    ).BUILD()

    print(query)
    result = db.fetchall(query)

    data = Records()
    data.from_list(result)

    return render_template('table_leagues/leagues_details.html', data = data.records[0])

@table_leagues_blueprint.route('/leagues/add', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        col_val_pairs = {
            'lgID': request.form['lgID'],
            'league': request.form['league'],
            'active': request.form['active']
        }

        query = Query().INSERT_INTO('leagues').VALUES(col_val_pairs)
        queryString = query.BUILD()
        db.execute(queryString, tuple(query._PARAMS))
        print(queryString)

    return redirect(url_for('leagues.view_table'))

@table_leagues_blueprint.route('/leagues/update/<string:ID>', methods=['GET', 'POST'])
def update_record(ID = None):
    if request.method == 'POST' and ID is not None:
        col_val_pairs = {
            'league': request.form['league'],
            'active': request.form['active']
        }

        query = Query().UPDATE('leagues').SET(col_val_pairs).WHERE(f"lgID = '{ID}'")
        queryString = query.BUILD()
        db.execute(queryString, tuple(query._PARAMS))
        print(queryString)

    return redirect(url_for('leagues.view_table'))

@table_leagues_blueprint.route('/leagues/delete/<string:ID>', methods=['GET', 'POST'])
def delete_record(ID = None):
    if request.method == 'POST' and ID is not None:
        query = Query().DELETE().FROM('leagues').WHERE(f"lgID = '{ID}'")
        queryString = query.BUILD()
        db.execute(queryString)
        print(queryString)

    return redirect(url_for('leagues.view_table'))

