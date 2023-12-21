"""
+----------------+---------+------+-----+---------+----------------+
| Field          | Type    | Null | Key | Default | Extra          |
+----------------+---------+------+-----+---------+----------------+
| ID             | int     | NO   | PRI | NULL    | auto_increment |
| yearkey        | int     | YES  |     | NULL    |                |
| leaguekey      | char(2) | YES  | MUL | NULL    |                |
| team_ID        | int     | YES  | MUL | NULL    |                |
| park_ID        | int     | YES  | MUL | NULL    |                |
| games          | int     | YES  |     | NULL    |                |
| openings       | int     | YES  |     | NULL    |                |
| attendance     | int     | YES  |     | NULL    |                |
| spanfirst_date | date    | YES  |     | NULL    |                |
| spanlast_date  | date    | YES  |     | NULL    |                |
+----------------+---------+------+-----+---------+----------------+
"""


class UpdateForm:
    def __init__(self, ID: int = None, yearkey: int = None, leaguekey: str = None, team_ID: int = None,
                 park_ID: int = None, games: int = None, openings: int = None, attendance: int = None,
                 spanfirst_date: str = None, spanlast_date: str = None):
        self.ID = ID
        self.yearkey = yearkey
        self.leaguekey = leaguekey
        self.team_ID = team_ID
        self.park_ID = park_ID
        self.games = games
        self.openings = openings
        self.attendance = attendance
        self.spanfirst_date = spanfirst_date
        self.spanlast_date = spanlast_date

    # Request args from form
    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.yearkey = dict.get('yearkey', None)
        if self.yearkey == "":
            self.yearkey = None

        self.leaguekey = dict.get('leaguekey', None)
        if self.leaguekey == "":
            self.leaguekey = None

        self.team_ID = dict.get('team_ID', None)
        if self.team_ID == "":
            self.team_ID = None

        self.park_ID = dict.get('park_ID', None)
        if self.park_ID == "":
            self.park_ID = None

        self.games = dict.get('games', None)
        if self.games == "":
            self.games = None

        self.openings = dict.get('openings', None)
        if self.openings == "":
            self.openings = None

        self.attendance = dict.get('attendance', None)
        if self.attendance == "":
            self.attendance = None

        self.spanfirst_date = dict.get('spanfirst_date', None)
        if self.spanfirst_date == "":
            self.spanfirst_date = None

        self.spanlast_date = dict.get('spanlast_date', None)
        if self.spanlast_date == "":
            self.spanlast_date = None

        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        tupl = ()
        empty = [None, '', 'None']

        if self.ID not in empty:
            tupl += (self.ID,)

        if self.yearkey not in empty:
            tupl += (self.yearkey,)

        if self.leaguekey not in empty:
            tupl += (self.leaguekey,)

        if self.team_ID not in empty:
            tupl += (self.team_ID,)

        if self.park_ID not in empty:
            tupl += (self.park_ID,)

        if self.games not in empty:
            tupl += (self.games,)

        if self.openings not in empty:
            tupl += (self.openings,)

        if self.attendance not in empty:
            tupl += (self.attendance,)

        if self.spanfirst_date not in empty:
            tupl += (self.spanfirst_date,)

        if self.spanlast_date not in empty:
            tupl += (self.spanlast_date,)

        return tupl


"""
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| ID             | int          | NO   |     | 0       |       |
| year           | int          | YES  |     | NULL    |       |
| league         | varchar(50)  | YES  |     | NULL    |       |
| team_name      | varchar(50)  | YES  |     | NULL    |       |
| park_name      | varchar(255) | YES  |     | NULL    |       |
| games          | int          | YES  |     | NULL    |       |
| openings       | int          | YES  |     | NULL    |       |
| attendance     | int          | YES  |     | NULL    |       |
| spanfirst_date | date         | YES  |     | NULL    |       |
| spanlast_date  | date         | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
"""


class FilterForm:
    def __init__(self, yearUL: int = None, yearLL: int = None, lgID: str = None, team_ID: int = None,
                 park_ID: str = None, gamesUL: int = None, gamesLL: int = None, openingsUL: int = None,
                 openingsLL: int = None, attendanceUL: int = None, attendanceLL: int = None,
                 spanfirst_dateUL: str = None, spanfirst_dateLL: str = None, spanlast_dateUL: str = None,
                 spanlast_dateLL: str = None):
        self.yearUL = yearUL
        self.yearLL = yearLL
        self.lgID = lgID
        self.team_ID = team_ID
        self.park_ID = park_ID
        self.gamesUL = gamesUL
        self.gamesLL = gamesLL
        self.openingsUL = openingsUL
        self.openingsLL = openingsLL
        self.attendanceUL = attendanceUL
        self.attendanceLL = attendanceLL
        self.spanfirst_dateUL = spanfirst_dateUL
        self.spanfirst_dateLL = spanfirst_dateLL
        self.spanlast_dateUL = spanlast_dateUL
        self.spanlast_dateLL = spanlast_dateLL

    def is_empty(self):
        empty = [None, '', 'None']
        return (self.yearUL in empty and self.yearLL in empty and self.league in empty and self.team_name in empty and
                self.park_name in empty and self.gamesUL in empty and self.gamesLL in empty and self.openingsUL in empty and
                self.openingsLL in empty and self.attendanceUL in empty and self.attendanceLL in empty and
                self.spanfirst_dateUL in empty and self.spanfirst_dateLL in empty and self.spanlast_dateUL in empty and
                self.spanlast_dateLL in empty)

    def from_dict(self, dict):
        self.yearUL = dict.get('filterYearUL', None)
        if self.yearUL == "":
            self.yearUL = None

        self.yearLL = dict.get('filterYearLL', None)
        if self.yearLL == "":
            self.yearLL = None

        self.league = dict.get('filterLeague', None)
        if self.league == "":
            self.league = None

        self.team_name = dict.get('filterTeamName', None)
        if self.team_name == "":
            self.team_name = None

        self.park_name = dict.get('filterParkName', None)
        if self.park_name == "":
            self.park_name = None

        self.gamesUL = dict.get('filterGamesUL', None)
        if self.gamesUL == "":
            self.gamesUL = None

        self.gamesLL = dict.get('filterGamesLL', None)
        if self.gamesLL == "":
            self.gamesLL = None

        self.openingsUL = dict.get('filterOpeningsUL', None)
        if self.openingsUL == "":
            self.openingsUL = None

        self.openingsLL = dict.get('filterOpeningsLL', None)
        if self.openingsLL == "":
            self.openingsLL = None

        self.attendanceUL = dict.get('filterAttendanceUL', None)
        if self.attendanceUL == "":
            self.attendanceUL = None

        self.attendanceLL = dict.get('filterAttendanceLL', None)
        if self.attendanceLL == "":
            self.attendanceLL = None

        self.spanfirst_dateUL = dict.get('filterSpanFirstDateUL', None)
        if self.spanfirst_dateUL == "":
            self.spanfirst_dateUL = None

        self.spanfirst_dateLL = dict.get('filterSpanFirstDateLL', None)
        if self.spanfirst_dateLL == "":
            self.spanfirst_dateLL = None

        self.spanlast_dateUL = dict.get('filterSpanLastDateUL', None)
        if self.spanlast_dateUL == "":
            self.spanlast_dateUL = None

        self.spanlast_dateLL = dict.get('filterSpanLastDateLL', None)
        if self.spanlast_dateLL == "":
            self.spanlast_dateLL = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        fitler_dict = {
            'filterYearUL': self.yearUL,
            'filterYearLL': self.yearLL,
            'filterLeague': self.lgID,
            'filterTeamName': self.team_ID,
            'filterParkName': self.park_ID,
            'filterGamesUL': self.gamesUL,
            'filterGamesLL': self.gamesLL,
            'filterOpeningsUL': self.openingsUL,
            'filterOpeningsLL': self.openingsLL,
            'filterAttendanceUL': self.attendanceUL,
            'filterAttendanceLL': self.attendanceLL,
            'filterSpanFirstDateUL': self.spanfirst_dateUL,
            'filterSpanFirstDateLL': self.spanfirst_dateLL,
            'filterSpanLastDateUL': self.spanlast_dateUL,
            'filterSpanLastDateLL': self.spanlast_dateLL
        }
        # Don't return empty values
        fitler_dict = {key: value for key,
                       value in fitler_dict.items() if value not in empty}
        return fitler_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.yearUL not in empty:
            and_string += " AND year <= {}".format(self.yearUL)

        if self.yearLL not in empty:
            and_string += " AND year >= {}".format(self.yearLL)

        if self.league not in empty:
            and_string += " AND lgID LIKE '%{}%'".format(self.league)

        if self.team_name not in empty:
            and_string += " AND team_ID = {}".format(self.team_name)

        if self.park_name not in empty:
            and_string += "park_ID = {}".format(self.park_name)

        if self.gamesUL not in empty:
            and_string += " AND games <= {}".format(self.gamesUL)

        if self.gamesLL not in empty:
            and_string += " AND games >= {}".format(self.gamesLL)

        if self.openingsUL not in empty:
            and_string += " AND openings <= {}".format(self.openingsUL)

        if self.openingsLL not in empty:
            and_string += " AND openings >= {}".format(self.openingsLL)

        if self.attendanceUL not in empty:
            and_string += " AND attendance <= {}".format(self.attendanceUL)

        if self.attendanceLL not in empty:
            and_string += " AND attendance >= {}".format(self.attendanceLL)

        if self.spanfirst_dateUL not in empty:
            and_string += " AND spanfirst_date <= '{}'".format(
                self.spanfirst_dateUL)

        if self.spanfirst_dateLL not in empty:
            and_string += " AND spanfirst_date >= '{}'".format(
                self.spanfirst_dateLL)

        if self.spanlast_dateUL not in empty:
            and_string += " AND spanlast_date <= '{}'".format(
                self.spanlast_dateUL)

        if self.spanlast_dateLL not in empty:
            and_string += " AND spanlast_date >= '{}'".format(
                self.spanlast_dateLL)

        # Remove the first " AND " string
        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, year: str = None, league: str = None, team_name: str = None, park_name: str = None,
                 games: str = None, openings: str = None, attendance: str = None, spanfirst_date: str = None,
                 spanlast_date: str = None):
        self.year = year
        self.league = league
        self.team_name = team_name
        self.park_name = park_name
        self.games = games
        self.openings = openings
        self.attendance = attendance
        self.spanfirst_date = spanfirst_date
        self.spanlast_date = spanlast_date

    def is_empty(self):
        empty = [None, '', 'None']
        return (self.year in empty and self.league in empty and self.team_name in empty and self.park_name in empty and
                self.games in empty and self.openings in empty and self.attendance in empty and
                self.spanfirst_date in empty and self.spanlast_date in empty)

    def from_dict(self, dict):
        options = ['ASC', 'DESC']

        self.year = dict.get('sortYear', None)
        if self.year not in options:
            self.year = None

        self.league = dict.get('sortLeague', None)
        if self.league not in options:
            self.league = None

        self.team_name = dict.get('sortTeamName', None)
        if self.team_name not in options:
            self.team_name = None

        self.park_name = dict.get('sortParkName', None)
        if self.park_name not in options:
            self.park_name = None

        self.games = dict.get('sortGames', None)
        if self.games not in options:
            self.games = None

        self.openings = dict.get('sortOpenings', None)
        if self.openings not in options:
            self.openings = None

        self.attendance = dict.get('sortAttendance', None)
        if self.attendance not in options:
            self.attendance = None

        self.spanfirst_date = dict.get('sortSpanFirstDate', None)
        if self.spanfirst_date not in options:
            self.spanfirst_date = None

        self.spanlast_date = dict.get('sortSpanLastDate', None)
        if self.spanlast_date not in options:
            self.spanlast_date = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        sort_dict = {
            'sortYear': self.year,
            'sortLeague': self.league,
            'sortTeamName': self.team_name,
            'sortParkName': self.park_name,
            'sortGames': self.games,
            'sortOpenings': self.openings,
            'sortAttendance': self.attendance,
            'sortSpanFirstDate': self.spanfirst_date,
            'sortSpanLastDate': self.spanlast_date
        }
        # Don't return empty values
        sort_dict = {key: value for key,
                     value in sort_dict.items() if value not in empty}
        return sort_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.year not in empty:
            and_string += "year {}, ".format(self.year)

        if self.league not in empty:
            and_string += "league {}, ".format(self.league)

        if self.team_name not in empty:
            and_string += "team_name {}, ".format(self.team_name)

        if self.park_name not in empty:
            and_string += "park_name {}, ".format(self.park_name)

        if self.games not in empty:
            and_string += "games {}, ".format(self.games)

        if self.openings not in empty:
            and_string += "openings {}, ".format(self.openings)

        if self.attendance not in empty:
            and_string += "attendance {}, ".format(self.attendance)

        if self.spanfirst_date not in empty:
            and_string += "spanfirst_date {}, ".format(self.spanfirst_date)

        if self.spanlast_date not in empty:
            and_string += "spanlast_date {}, ".format(self.spanlast_date)

        # Remove the last ", " string
        if and_string != "":
            and_string = and_string[:-2]

        return and_string
