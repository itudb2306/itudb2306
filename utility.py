from flask import render_template
from database import db, Query


def exceptionPage(e: Exception):
    return render_template('error.html', error_type=type(e).__name__, error_message=str(e))


def getLeaguesList():
    # Query for division league selection
    leagues_list = []
    leagues_proc = "GetLeaguesList"
    leagues_result = db.fetchallProc(leagues_proc)
    for row in leagues_result:
        leagues_list.append({'lgID': row[0],
                             'league': row[1], })
    return leagues_list


def getDivisionsList():
    # Query for division league selection
    divisions_list = []
    divisions_proc = "GetDivisionsList"
    divisions_result = db.fetchallProc(divisions_proc)
    for row in divisions_result:
        divisions_list.append({'ID': row[0],
                               'division': row[1], })
    return divisions_list


def getTeamNamesList():
    # Query for division league selection
    teams_list = []
    teams_proc = "GetTeamNamesList"
    teams_result = db.fetchallProc(teams_proc)
    for row in teams_result:
        teams_list.append({'ID': row[0],
                           'name': row[1], })
    return teams_list


def getParksList():
    # Query for division league selection
    parks_list = []
    parks_proc = "GetParksList"
    parks_result = db.fetchallProc(parks_proc)
    for row in parks_result:
        parks_list.append({'ID': row[0],
                           'parkname': row[1], })
    return parks_list
