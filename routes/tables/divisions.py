from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Query

from config import RECORDS_PER_PAGE

table_divisions_blueprint = Blueprint('divisions', __name__)


@table_divisions_blueprint.route('divisions')
def view_table():
    """
    URL: /tables/divisions?p=
    """

    # Check whether view exists
    if not db.checkTableExists('divisions_leagues'):
        divisions_leagues_query = """
        create view divisions_leagues as 
        select 
            l.lgID as lgID,
            l.league as league,
            l.active as lgActive,
            d.divID as divID,
            d.division as division, 
            d.active as divActive,
            d.ID as ID
        from divisions d, leagues l
        where
            d.lgID=l.lgID;
        """
        db.execute(divisions_leagues_query)

    # Pagination
    page = request.args.get('p', 1, type=int)
    first_record = (page - 1) * RECORDS_PER_PAGE

    # Divisions and leagues query
    query = Query().SELECT('*').FROM('divisions_leagues').LIMIT(first_record,
                                                                RECORDS_PER_PAGE).BUILD()
    print(query)
    result = db.fetchall(query)

    # Query building for total pages
    """
    select count(*) 
    from divisions_leagues;
    """
    total_pages_query = Query().SELECT('COUNT(*)').FROM(
        'divisions_leagues').BUILD()
    total_pages = db.fetchone(total_pages_query)[0]
    total_pages = total_pages // RECORDS_PER_PAGE + 1
    print(total_pages_query)

    data_recordings = []
    for row in result:
        data_recordings.append({'lgID': row[0],
                                'league': row[1],
                                'lgActive': row[2],
                                'divID': row[3],
                                'division': row[4],
                                'divActive': row[5],
                                'ID': row[6]})

    # Query for division league selection
    leagues_list = []
    leagues_query = Query().SELECT('lgID, league').FROM('leagues').BUILD()
    leagues_result = db.fetchall(leagues_query)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })

    return render_template('table_divisions.html', data_list=data_recordings, current_page=page, total_pages=total_pages, leagues_list=leagues_list)


@table_divisions_blueprint.route('/divisions/update/<int:ID>', methods=['GET', 'POST'])
def update_record(ID=None):
    """
    URL: /tables/divisions/update/<int:ID>
    """

    if request.method == 'POST' and ID is not None:
        # Get form data
        col_val_pairs = {
            'lgID': request.form['lgID'],
            'division': request.form['division'],
            'active': request.form['active'],
            'divID': request.form['divID']
        }

        # Query building
        query = Query().UPDATE('divisions').SET(col_val_pairs).WHERE(
            'ID = %d' % ID).BUILD()
        # UPDATE divisions SET lgID = 'AB', division = 'ABC', active = 'N' ... WHERE ID = 5
        print(query)
        try:
            db.execute(query)
        except:
            return "<p> There is already a league %s and division %s </p>" % (col_val_pairs['lgID'], col_val_pairs['divID'])

        print('Record updated: ', ID)

    return redirect(url_for('divisions.view_table'))
