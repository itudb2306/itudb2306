"""
+------------+------------+------+-----+---------+----------------+
| Field      | Type       | Null | Key | Default | Extra          |
+------------+------------+------+-----+---------+----------------+
| ID         | int        | NO   | PRI | NULL    | auto_increment |
| yearID     | smallint   | NO   | MUL | NULL    |                |
| lgID       | char(2)    | YES  | MUL | NULL    |                |
| teamID     | char(3)    | NO   |     | NULL    |                |
| div_ID     | int        | YES  | MUL | NULL    |                |
| teamRank   | smallint   | YES  |     | NULL    |                |
| G          | smallint   | YES  |     | NULL    |                |
| Ghome      | smallint   | YES  |     | NULL    |                |
| W          | smallint   | YES  |     | NULL    |                |
| L          | smallint   | YES  |     | NULL    |                |
| DivWin     | varchar(1) | YES  |     | NULL    |                |
| WCWin      | varchar(1) | YES  |     | NULL    |                |
| LgWin      | varchar(1) | YES  |     | NULL    |                |
| WSWin      | varchar(1) | YES  |     | NULL    |                |
| R          | smallint   | YES  |     | NULL    |                |
| AB         | smallint   | YES  |     | NULL    |                |
| H          | smallint   | YES  |     | NULL    |                |
| 2B         | smallint   | YES  |     | NULL    |                |
| 3B         | smallint   | YES  |     | NULL    |                |
| HR         | smallint   | YES  |     | NULL    |                |
| BB         | smallint   | YES  |     | NULL    |                |
| SO         | smallint   | YES  |     | NULL    |                |
| SB         | smallint   | YES  |     | NULL    |                |
| CS         | smallint   | YES  |     | NULL    |                |
| HBP        | smallint   | YES  |     | NULL    |                |
| SF         | smallint   | YES  |     | NULL    |                |
| RA         | smallint   | YES  |     | NULL    |                |
| ER         | smallint   | YES  |     | NULL    |                |
| ERA        | double     | YES  |     | NULL    |                |
| CG         | smallint   | YES  |     | NULL    |                |
| SHO        | smallint   | YES  |     | NULL    |                |
| SV         | smallint   | YES  |     | NULL    |                |
| IPouts     | int        | YES  |     | NULL    |                |
| HA         | smallint   | YES  |     | NULL    |                |
| HRA        | smallint   | YES  |     | NULL    |                |
| BBA        | smallint   | YES  |     | NULL    |                |
| SOA        | smallint   | YES  |     | NULL    |                |
| E          | int        | YES  |     | NULL    |                |
| DP         | int        | YES  |     | NULL    |                |
| FP         | double     | YES  |     | NULL    |                |
| attendance | int        | YES  |     | NULL    |                |
| BPF        | int        | YES  |     | NULL    |                |
| PPF        | int        | YES  |     | NULL    |                |
| park_ID    | int        | YES  | MUL | NULL    |                |
| team_ID    | int        | NO   | MUL | NULL    |                |
+------------+------------+------+-----+---------+----------------+
"""


class TableRecord:
    def __init__(self, ID: int = None, name: str = None, year: int = None, league: str = None,
                 division: str = None, park: str = None, games: int = None, home_games: int = None,
                 wins: int = None, losses: int = None, division_win: str = None, wild_card_win: str = None,
                 league_win: str = None, world_series_win: str = None):
        self.ID = ID
        self.name = name
        self.year = year
        self.league = league
        self.division = division
        self.park = park
        self.games = games
        self.home_games = home_games
        self.wins = wins
        self.losses = losses
        self.division_win = division_win
        self.wild_card_win = wild_card_win
        self.league_win = league_win
        self.world_series_win = world_series_win

    def from_list(self, list):
        self.ID = list[0]
        self.name = list[1]
        self.year = list[2]
        self.league = list[3]
        self.division = list[4]
        self.park = list[5]
        self.games = list[6]
        self.home_games = list[7]
        self.wins = list[8]
        self.losses = list[9]
        self.division_win = list[10]
        self.wild_card_win = list[11]
        self.league_win = list[12]
        self.world_series_win = list[13]
        return self

    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        self.name = dict.get('name', None)
        self.year = dict.get('year', None)
        self.league = dict.get('league', None)
        self.division = dict.get('division', None)
        self.park = dict.get('park', None)
        self.games = dict.get('games', None)
        self.home_games = dict.get('home_games', None)
        self.wins = dict.get('wins', None)
        self.losses = dict.get('losses', None)
        self.division_win = dict.get('division_win', None)
        self.wild_card_win = dict.get('wild_card_win', None)
        self.league_win = dict.get('league_win', None)
        self.world_series_win = dict.get('world_series_win', None)
        return self

    def to_list(self):
        return [self.ID, self.name, self.year, self.league,
                self.division, self.park, self.games, self.home_games,
                self.wins, self.losses, self.division_win, self.wild_card_win,
                self.league_win, self.world_series_win]

    def to_dict(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'year': self.year,
            'league': self.league,
            'division': self.division,
            'park': self.park,
            'games': self.games,
            'home_games': self.home_games,
            'wins': self.wins,
            'losses': self.losses,
            'division_win': self.division_win,
            'wild_card_win': self.wild_card_win,
            'league_win': self.league_win,
            'world_series_win': self.world_series_win
        }


class TableRecords:
    def __init__(self, records: list = None):
        self.records = records

    def from_list(self, list):
        self.records = []
        for row in list:
            record = TableRecord().from_list(row)
            self.records.append(record)

    def from_dict(self, dict):
        self.records = []
        for row in dict:
            self.records.append(TableRecord().from_dict(row))

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
