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


class Record:
    def __init__(self, ID: int = None, year: int = None, league: str = None, team_name: str = None,
                 park_name: str = None, games: int = None, openings: int = None, attendance: int = None,
                 spanfirst_date: str = None, spanlast_date: str = None):
        self.ID = ID
        self.year = year
        self.league = league
        self.team_name = team_name
        self.park_name = park_name
        self.games = games
        self.openings = openings
        self.attendance = attendance
        self.spanfirst_date = spanfirst_date
        self.spanlast_date = spanlast_date

    # record.ID -> record[ID]
    # No need for this, since we can use record.ID in jinja2 templates
    # def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.ID = list[0]
        self.year = list[1]
        self.league = list[2]
        self.team_name = list[3]
        self.park_name = list[4]
        self.games = list[5]
        self.openings = list[6]
        self.attendance = list[7]
        self.spanfirst_date = list[8]
        self.spanlast_date = list[9]
        return self

    def from_dict(self, dict):
        self.ID = dict['ID']
        self.year = dict['year']
        self.league = dict['league']
        self.team_name = dict['team_name']
        self.park_name = dict['park_name']
        self.games = dict['games']
        self.openings = dict['openings']
        self.attendance = dict['attendance']
        self.spanfirst_date = dict['spanfirst_date']
        self.spanlast_date = dict['spanlast_date']
        return self

    def to_list(self):
        return [self.ID, self.year, self.league, self.team_name, self.park_name, self.games, self.openings,
                self.attendance, self.spanfirst_date, self.spanlast_date]

    def to_dict(self):
        return {
            'ID': self.ID,
            'year': self.year,
            'league': self.league,
            'team_name': self.team_name,
            'park_name': self.park_name,
            'games': self.games,
            'openings': self.openings,
            'attendance': self.attendance,
            'spanfirst_date': self.spanfirst_date,
            'spanlast_date': self.spanlast_date,
        }


class Records:
    def __init__(self, records: list = None):
        self.records = records

    def from_list(self, list):
        self.records = []
        for row in list:
            record = Record().from_list(row)
            self.records.append(record)

    def from_dict(self, dict):
        self.records = []
        for row in dict:
            self.records.append(Record().from_dict(row))

    def to_list(self):
        list = []
        for record in self.records:
            list.append(record.to_list())
        return list

    def to_dict(self):
        dict = []
        for record in self.records:
            dict.append(record.to_dict())
        return dict
