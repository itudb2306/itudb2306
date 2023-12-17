"""
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


class TableRecord:
    def __init__(self, ID: int = None, team_code: str = None, name: str = None, team_name_ID: int = None, year: int = None,
                 league: str = None, league_ID: int = None, division: str = None, division_ID: int = None,  park: str = None,
                 park_ID: int = None, team_rank: int = None, games: int = None, home_games: int = None, wins: int = None, losses: int = None,
                 division_win: str = None, wild_card_win: str = None, league_win: str = None, world_series_win: str = None,
                 runs_scored: int = None, at_bats: int = None, hits: int = None, doubles: int = None, triples: int = None,
                 homeruns: int = None, walks_batters: int = None, strikeouts_batters: int = None, stolen_bases: int = None,
                 caught_stealing: int = None, hit_by_pitch: int = None, sacrifice_flies: int = None, runs_allowed: int = None,
                 earned_runs_allowed: int = None, earned_run_average: float = None, complete_games: int = None, shutouts: int = None,
                 saves: int = None, outs_pitched: int = None, hits_allowed: int = None, homeruns_allowed: int = None,
                 walks_allowed: int = None, strikeouts_pitchers: int = None, errors: int = None, double_plays: int = None,
                 fielding_percentage: float = None, attendance: int = None, batter_park_factor: float = None, pitcher_park_factor: float = None):
        self.ID = ID
        team_code = team_code
        self.name = name
        self.team_name_ID = team_name_ID
        self.year = year
        self.league = league
        self.league_ID = league_ID
        self.division = division
        self.division_ID = division_ID
        self.park = park
        self.park_ID = park_ID
        self.team_rank = team_rank
        self.games = games
        self.home_games = home_games
        self.wins = wins
        self.losses = losses
        self.division_win = division_win
        self.wild_card_win = wild_card_win
        self.league_win = league_win
        self.world_series_win = world_series_win
        self.runs_scored = runs_scored
        self.at_bats = at_bats
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.homeruns = homeruns
        self.walks_batters = walks_batters
        self.strikeouts_batters = strikeouts_batters
        self.stolen_bases = stolen_bases
        self.caught_stealing = caught_stealing
        self.hit_by_pitch = hit_by_pitch
        self.sacrifice_flies = sacrifice_flies
        self.runs_allowed = runs_allowed
        self.earned_runs_allowed = earned_runs_allowed
        self.earned_run_average = earned_run_average
        self.complete_games = complete_games
        self.shutouts = shutouts
        self.saves = saves
        self.outs_pitched = outs_pitched
        self.hits_allowed = hits_allowed
        self.homeruns_allowed = homeruns_allowed
        self.walks_allowed = walks_allowed
        self.strikeouts_pitchers = strikeouts_pitchers
        self.errors = errors
        self.double_plays = double_plays
        self.fielding_percentage = fielding_percentage
        self.attendance = attendance
        self.batter_park_factor = batter_park_factor
        self.pitcher_park_factor = pitcher_park_factor

    def from_list(self, list):
        self.ID = list[0]
        self.team_code = list[1]
        self.name = list[2]
        self.team_name_ID = list[3]
        self.year = list[4]
        self.league = list[5]
        self.league_ID = list[6]
        self.division = list[7]
        self.division_ID = list[8]
        self.park = list[9]
        self.park_ID = list[10]
        self.team_rank = list[11]
        self.games = list[12]
        self.home_games = list[13]
        self.wins = list[14]
        self.losses = list[15]
        self.division_win = list[16]
        self.wild_card_win = list[17]
        self.league_win = list[18]
        self.world_series_win = list[19]
        self.runs_scored = list[20]
        self.at_bats = list[21]
        self.hits = list[22]
        self.doubles = list[23]
        self.triples = list[24]
        self.homeruns = list[25]
        self.walks_batters = list[26]
        self.strikeouts_batters = list[27]
        self.stolen_bases = list[28]
        self.caught_stealing = list[29]
        self.hit_by_pitch = list[30]
        self.sacrifice_flies = list[31]
        self.runs_allowed = list[32]
        self.earned_runs_allowed = list[33]
        self.earned_run_average = list[34]
        self.complete_games = list[35]
        self.shutouts = list[36]
        self.saves = list[37]
        self.outs_pitched = list[38]
        self.hits_allowed = list[39]
        self.homeruns_allowed = list[40]
        self.walks_allowed = list[41]
        self.strikeouts_pitchers = list[42]
        self.errors = list[43]
        self.double_plays = list[44]
        self.fielding_percentage = list[45]
        self.attendance = list[46]
        self.batter_park_factor = list[47]
        self.pitcher_park_factor = list[48]

        return self

    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        self.team_code = dict.get('team_code', None)
        self.name = dict.get('name', None)
        self.team_name_ID = dict.get('team_name_ID', None)
        self.year = dict.get('year', None)
        self.league = dict.get('league', None)
        self.league_ID = dict.get('league_ID', None)
        self.division = dict.get('division', None)
        self.division_ID = dict.get('division_ID', None)
        self.park = dict.get('park', None)
        self.park_ID = dict.get('park_ID', None)
        self.team_rank = dict.get('team_rank', None)
        self.games = dict.get('games', None)
        self.home_games = dict.get('home_games', None)
        self.wins = dict.get('wins', None)
        self.losses = dict.get('losses', None)
        self.division_win = dict.get('division_win', None)
        self.wild_card_win = dict.get('wild_card_win', None)
        self.league_win = dict.get('league_win', None)
        self.world_series_win = dict.get('world_series_win', None)
        self.runs_scored = dict.get('runs_scored', None)
        self.at_bats = dict.get('at_bats', None)
        self.hits = dict.get('hits', None)
        self.doubles = dict.get('doubles', None)
        self.triples = dict.get('triples', None)
        self.homeruns = dict.get('homeruns', None)
        self.walks_batters = dict.get('walks_batters', None)
        self.strikeouts_batters = dict.get('strikeouts_batters', None)
        self.stolen_bases = dict.get('stolen_bases', None)
        self.caught_stealing = dict.get('caught_stealing', None)
        self.hit_by_pitch = dict.get('hit_by_pitch', None)
        self.sacrifice_flies = dict.get('sacrifice_flies', None)
        self.runs_allowed = dict.get('runs_allowed', None)
        self.earned_runs_allowed = dict.get('earned_runs_allowed', None)
        self.earned_run_average = dict.get('earned_run_average', None)
        self.complete_games = dict.get('complete_games', None)
        self.shutouts = dict.get('shutouts', None)
        self.saves = dict.get('saves', None)
        self.outs_pitched = dict.get('outs_pitched', None)
        self.hits_allowed = dict.get('hits_allowed', None)
        self.homeruns_allowed = dict.get('homeruns_allowed', None)
        self.walks_allowed = dict.get('walks_allowed', None)
        self.strikeouts_pitchers = dict.get('strikeouts_pitchers', None)
        self.errors = dict.get('errors', None)
        self.double_plays = dict.get('double_plays', None)
        self.fielding_percentage = dict.get('fielding_percentage', None)
        self.attendance = dict.get('attendance', None)
        self.batter_park_factor = dict.get('batter_park_factor', None)
        self.pitcher_park_factor = dict.get('pitcher_park_factor', None)

        return self

    def to_list(self):
        return [self.ID, self.team_code, self.name, self.team_name_ID, self.year, self.league, self.league_ID, self.division,
                self.division_ID, self.park, self.park_ID, self.team_rank, self.games, self.home_games, self.wins, self.losses,
                self.division_win, self.wild_card_win, self.league_win, self.world_series_win, self.runs_scored, self.at_bats,
                self.hits, self.doubles, self.triples, self.homeruns, self.walks_batters, self.strikeouts_batters, self.stolen_bases,
                self.caught_stealing, self.hit_by_pitch, self.sacrifice_flies, self.runs_allowed, self.earned_runs_allowed,
                self.earned_run_average, self.complete_games, self.shutouts, self.saves, self.outs_pitched, self.hits_allowed,
                self.homeruns_allowed, self.walks_allowed, self.strikeouts_pitchers, self.errors, self.double_plays,
                self.fielding_percentage, self.attendance, self.batter_park_factor, self.pitcher_park_factor]

    def to_dict(self):
        return {
            'ID': self.ID,
            'team_code': self.team_code,
            'name': self.name,
            'team_name_ID': self.team_name_ID,
            'year': self.year,
            'league': self.league,
            'league_ID': self.league_ID,
            'division': self.division,
            'division_ID': self.division_ID,
            'park': self.park,
            'park_ID': self.park_ID,
            'team_rank': self.team_rank,
            'games': self.games,
            'home_games': self.home_games,
            'wins': self.wins,
            'losses': self.losses,
            'division_win': self.division_win,
            'wild_card_win': self.wild_card_win,
            'league_win': self.league_win,
            'world_series_win': self.world_series_win,
            'runs_scored': self.runs_scored,
            'at_bats': self.at_bats,
            'hits': self.hits,
            'doubles': self.doubles,
            'triples': self.triples,
            'homeruns': self.homeruns,
            'walks_batters': self.walks_batters,
            'strikeouts_batters': self.strikeouts_batters,
            'stolen_bases': self.stolen_bases,
            'caught_stealing': self.caught_stealing,
            'hit_by_pitch': self.hit_by_pitch,
            'sacrifice_flies': self.sacrifice_flies,
            'runs_allowed': self.runs_allowed,
            'earned_runs_allowed': self.earned_runs_allowed,
            'earned_run_average': self.earned_run_average,
            'complete_games': self.complete_games,
            'shutouts': self.shutouts,
            'saves': self.saves,
            'outs_pitched': self.outs_pitched,
            'hits_allowed': self.hits_allowed,
            'homeruns_allowed': self.homeruns_allowed,
            'walks_allowed': self.walks_allowed,
            'strikeouts_pitchers': self.strikeouts_pitchers,
            'errors': self.errors,
            'double_plays': self.double_plays,
            'fielding_percentage': self.fielding_percentage,
            'attendance': self.attendance,
            'batter_park_factor': self.batter_park_factor,
            'pitcher_park_factor': self.pitcher_park_factor
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
