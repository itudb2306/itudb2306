class TableRecord:
    def __init__(self, ID: int = None, team_code: str = None, name: str = None, year: int = None, league: str = None,
                 division: str = None, park: str = None, team_rank: int = None, games: int = None, home_games: int = None,
                 wins: int = None, losses: int = None, division_win: str = None, wild_card_win: str = None,
                 league_win: str = None, world_series_win: str = None):
        self.ID = ID
        self.team_code = team_code
        self.name = name
        self.year = year
        self.league = league
        self.division = division
        self.park = park
        self.team_rank = team_rank
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
        self.team_code = list[1]
        self.name = list[2]
        self.year = list[3]
        self.league = list[4]
        self.division = list[5]
        self.park = list[6]
        self.team_rank = list[7]
        self.games = list[8]
        self.home_games = list[9]
        self.wins = list[10]
        self.losses = list[11]
        self.division_win = list[12]
        self.wild_card_win = list[13]
        self.league_win = list[14]
        self.world_series_win = list[15]
        return self

    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        self.team_code = dict.get('team_code', None)
        self.name = dict.get('name', None)
        self.year = dict.get('year', None)
        self.league = dict.get('league', None)
        self.division = dict.get('division', None)
        self.park = dict.get('park', None)
        self.team_rank = dict.get('team_rank', None)
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
        return [self.ID, self.team_code, self.name, self.year, self.league,
                self.division, self.park, self.team_rank, self.games, self.home_games,
                self.wins, self.losses, self.division_win, self.wild_card_win,
                self.league_win, self.world_series_win]

    def to_dict(self):
        return {
            'ID': self.ID,
            'team_code': self.team_code,
            'name': self.name,
            'year': self.year,
            'league': self.league,
            'division': self.division,
            'park': self.park,
            'team_rank': self.team_rank,
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
