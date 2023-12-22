from datetime import datetime
from flask import render_template
from database import db, Query


def logQuery(query: str):
    date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    # Replace newlines and tabs with spaces
    formatted_string = query.replace('\n', ' ')
    formatted_string = formatted_string.replace('\t', ' ')
    # Replace multiple spaces with one space
    while '  ' in formatted_string:
        formatted_string = formatted_string.replace('  ', ' ')

    with open("query_log.txt", "a") as log_file:
        log_file.write("[%s] %s\n" % (date_time, formatted_string))


def exceptionPage(e: Exception):
    return render_template('error.html', error_type=type(e).__name__, error_message=str(e))


def getLeaguesList():
    # Query for division league selection
    leagues_list = []
    leagues_query = Query().SELECT('lgID, league').FROM('leagues').BUILD()
    leagues_result = db.fetchall(leagues_query)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })
    return leagues_list


def checkDivisionsViewExists():
    # This view joins divisions with leagues.
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
        db.execute(divisions_leagues_query, None)
