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


def getDivisionsList():
    # Query for division league selection
    divisions_list = []
    divisions_query = Query().SELECT('ID, division').FROM('divisions').BUILD()
    divisions_result = db.fetchall(divisions_query)
    for row in divisions_result:
        divisions_list.append({'ID': row[0],
                               'division': row[1], })
    return divisions_list


def getTeamNamesList():
    # Query for division league selection
    teams_list = []
    teams_query = Query().SELECT('ID, name').FROM('teamnames').BUILD()
    teams_result = db.fetchall(teams_query)
    for row in teams_result:
        teams_list.append({'ID': row[0],
                           'name': row[1], })
    return teams_list


def getParksList():
    # Query for division league selection
    parks_list = []
    parks_query = Query().SELECT('ID, parkname').FROM('parks').BUILD()
    parks_result = db.fetchall(parks_query)
    for row in parks_result:
        parks_list.append({'ID': row[0],
                           'parkname': row[1], })
    return parks_list


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


def checkTeamsEasyViewExists():
    if not db.checkTableExists('teams_easy'):
        teams_easy_query = """
        create view teams_easy as
        select 
            t.ID as ID,
            t.teamID as team_code,
            tn.name as name,
            t.yearID as year,
            l.league as league,
            d.division as division,
            p.parkname as park,
            t.teamRank as team_rank,
            t.G as games,
            t.Ghome as home_games,
            t.W as wins,
            t.L as losses,
            t.DivWin as division_win,
            t.WCWin as wild_card_win,
            t.LgWin as league_win,
            t.WSWin as world_series_win
        from teams t
        left join leagues l on t.lgID = l.lgID
        left join divisions d on t.div_ID = d.ID
        left join teamnames tn on t.team_ID = tn.ID
        left join parks p on t.park_ID = p.ID
        """
        db.execute(teams_easy_query, None)


def checkTeamsDetailsViewExists():
    if not db.checkTableExists('teams_details'):
        teams_deatails_query = """
        create view teams_details as
        select 
            t.ID as ID,
            t.teamID as team_code,
            tn.name as name,
            tn.ID as team_name_ID,
            t.yearID as year,
            l.league as league,
            l.lgID as league_ID,
            d.division as division,
            d.ID as division_ID,
            p.parkname as park,
            p.ID as park_ID,
            t.teamRank as team_rank,
            t.G as games,
            t.Ghome as home_games,
            t.W as wins,
            t.L as losses,
            t.DivWin as division_win,
            t.WCWin as wild_card_win,
            t.LgWin as league_win,
            t.WSWin as world_series_win,
            t.R as runs_scored,
            t.AB as at_bats,
            t.H as hits,
            t.2B as doubles,
            t.3B as triples,
            t.HR as homeruns,
            t.BB as walks_batters,
            t.SO as strikeouts_batters,
            t.SB as stolen_bases,
            t.CS as caught_stealing,
            t.HBP as hit_by_pitch,
            t.SF as sacrifice_flies,
            t.RA as runs_allowed,
            t.ER as earned_runs_allowed,
            t.ERA as earned_run_average,
            t.CG as complete_games,
            t.SHO as shutouts,
            t.SV as saves,
            t.IPOuts as outs_pitched,
            t.HA as hits_allowed,
            t.HRA as homeruns_allowed,
            t.BBA as walks_allowed,
            t.SOA as strikeouts_pitchers,
            t.E as errors,
            t.DP as double_plays,
            t.FP as fielding_percentage,
            t.attendance as attendance,
            t.BPF as batter_park_factor,
            t.PPF as pitcher_park_factor
        from teams t
        left join leagues l on t.lgID = l.lgID
        left join divisions d on t.div_ID = d.ID
        left join teamnames tn on t.team_ID = tn.ID
        left join parks p on t.park_ID = p.ID
        """
        db.execute(teams_deatails_query, None)


def checkTeamsNamesViewExists():
    if not db.checkTableExists('team_names_count'):
        teams_names_count_query = """
        create view team_names_count as
        select tn1.ID as ID,
            tn1.name as name,
            tn2.cnt as cnt
        from teamnames tn1 join ( select
                teamnames.ID as ID,
                count(teamnames.ID) as cnt
                from teamnames left join teams on
                teams.team_ID = teamnames.ID
                group by teamnames.ID
        ) as tn2 on tn1.ID = tn2.ID;
        """
        db.execute(teams_names_count_query, None)


def checkHomegamesViewExists():
    if not db.checkTableExists('homegames_easy'):
        teams_easy_query = """
        create view homegames_easy as 
        select 
            h.ID as ID,
            h.yearkey as year,
            l.league as league,
            tn.name as team_name,
            p.parkname as park_name,
            h.games as games,
            h.openings as openings,
            h.attendance as attendance,
            h.spanfirst_date as spanfirst_date,
            h.spanlast_date as spanlast_date
            tn.ID as team_ID,
            l.lgID as lgID,
            p.ID as park_ID
        from homegames h
        left join teamnames tn on tn.ID = h.team_ID
        left join parks p on p.ID = h.park_ID
        left join leagues l on h.leaguekey = l.lgID;
        """
        db.execute(teams_easy_query, None)
