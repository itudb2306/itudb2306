class FilterForm:
    def __init__(self, team_code: str = None, name: str = None, yearUL: int = None, yearLL: int = None, league: str = None, division: str = None,
                 park: str = None, team_rankUL: int = None, team_rankLL: int = None, gamesUL: int = None, gamesLL: int = None,
                 home_gamesUL: int = None, home_gamesLL: int = None, winsUL: int = None, winsLL: int = None, lossesUL: int = None,
                 lossesLL: int = None, division_win: str = None, wild_card_win: str = None, league_win: str = None, world_series_win: str = None):
        self.team_code = team_code
        self.name = name
        self.yearUL = yearUL
        self.yearLL = yearLL
        self.league = league
        self.division = division
        self.park = park
        self.team_rankUL = team_rankUL
        self.team_rankLL = team_rankLL
        self.gamesUL = gamesUL
        self.gamesLL = gamesLL
        self.home_gamesUL = home_gamesUL
        self.home_gamesLL = home_gamesLL
        self.winsUL = winsUL
        self.winsLL = winsLL
        self.lossesUL = lossesUL
        self.lossesLL = lossesLL
        self.division_win = division_win
        self.wild_card_win = wild_card_win
        self.league_win = league_win
        self.world_series_win = world_series_win

    def is_empty(self):
        empty = [None, '', 'None']
        return (self.team_code in empty and self.name in empty and self.yearUL in empty and self.yearLL in empty and self.league in empty and
                self.division in empty and self.park in empty and self.team_rankUL in empty and self.team_rankLL in empty and
                self.gamesUL in empty and self.gamesLL in empty and self.home_gamesUL in empty and self.home_gamesLL in empty and
                self.winsUL in empty and self.winsLL in empty and self.lossesUL in empty and self.lossesLL in empty and
                self.division_win in empty and self.wild_card_win in empty and self.league_win in empty and self.world_series_win in empty)

    def from_dict(self, dict):
        empty = [None, '', 'None']

        self.team_code = dict.get('filterTeamCode', None)
        if self.team_code in empty:
            self.team_code = None

        self.name = dict.get('filterName', None)
        if self.name in empty:
            self.name = None

        self.yearUL = dict.get('filterYearUL', None)
        if self.yearUL in empty:
            self.yearUL = None

        self.yearLL = dict.get('filterYearLL', None)
        if self.yearLL in empty:
            self.yearLL = None

        self.league = dict.get('filterLeague', None)
        if self.league in empty:
            self.league = None

        self.division = dict.get('filterDivision', None)
        if self.division in empty:
            self.division = None

        self.park = dict.get('filterPark', None)
        if self.park in empty:
            self.park = None

        self.team_rankUL = dict.get('filterTeamRankUL', None)
        if self.team_rankUL in empty:
            self.team_rankUL = None

        self.team_rankLL = dict.get('filterTeamRankLL', None)
        if self.team_rankLL in empty:
            self.team_rankLL = None

        self.gamesUL = dict.get('filterGamesUL', None)
        if self.gamesUL in empty:
            self.gamesUL = None

        self.gamesLL = dict.get('filterGamesLL', None)
        if self.gamesLL in empty:
            self.gamesLL = None

        self.home_gamesUL = dict.get('filterHomeGamesUL', None)
        if self.home_gamesUL in empty:
            self.home_gamesUL = None

        self.home_gamesLL = dict.get('filterHomeGamesLL', None)
        if self.home_gamesLL in empty:
            self.home_gamesLL = None

        self.winsUL = dict.get('filterWinsUL', None)
        if self.winsUL in empty:
            self.winsUL = None

        self.winsLL = dict.get('filterWinsLL', None)
        if self.winsLL in empty:
            self.winsLL = None

        self.lossesUL = dict.get('filterLossesUL', None)
        if self.lossesUL in empty:
            self.lossesUL = None

        self.division_win = dict.get('filterDivisionWin', None)
        if self.division_win in empty:
            self.division_win = None

        self.wild_card_win = dict.get('filterWildCardWin', None)
        if self.wild_card_win in empty:
            self.wild_card_win = None

        self.league_win = dict.get('filterLeagueWin', None)
        if self.league_win in empty:
            self.league_win = None

        self.world_series_win = dict.get('filterWorldSeriesWin', None)
        if self.world_series_win in empty:
            self.world_series_win = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        fitler_dict = {
            'filterTeamCode': self.team_code,
            'filterName': self.name,
            'filterYearUL': self.yearUL,
            'filterYearLL': self.yearLL,
            'filterLeague': self.league,
            'filterDivision': self.division,
            'filterPark': self.park,
            'filterTeamRankUL': self.team_rankUL,
            'filterTeamRankLL': self.team_rankLL,
            'filterGamesUL': self.gamesUL,
            'filterGamesLL': self.gamesLL,
            'filterHomeGamesUL': self.home_gamesUL,
            'filterHomeGamesLL': self.home_gamesLL,
            'filterWinsUL': self.winsUL,
            'filterWinsLL': self.winsLL,
            'filterLossesUL': self.lossesUL,
            'filterLossesLL': self.lossesLL,
            'filterDivisionWin': self.division_win,
            'filterWildCardWin': self.wild_card_win,
            'filterLeagueWin': self.league_win,
            'filterWorldSeriesWin': self.world_series_win
        }
        # Don't return empty values
        fitler_dict = {key: value for key,
                       value in fitler_dict.items() if value not in empty}
        return fitler_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.team_code not in empty:
            and_string += " AND team_code LIKE '%{}%'".format(self.team_code)

        if self.name not in empty:
            and_string += " AND name LIKE '%{}%'".format(self.name)

        if self.yearUL not in empty:
            and_string += " AND year <= {}".format(self.yearUL)

        if self.yearLL not in empty:
            and_string += " AND year >= {}".format(self.yearLL)

        if self.league not in empty:
            and_string += " AND league LIKE '%{}%'".format(self.league)

        if self.division not in empty:
            and_string += " AND division LIKE '%{}%'".format(self.division)

        if self.park not in empty:
            and_string += " AND park LIKE '%{}%'".format(self.park)

        if self.team_rankUL not in empty:
            and_string += " AND team_rank <= {}".format(self.team_rankUL)

        if self.team_rankLL not in empty:
            and_string += " AND team_rank >= {}".format(self.team_rankLL)

        if self.gamesUL not in empty:
            and_string += " AND games <= {}".format(self.gamesUL)

        if self.gamesLL not in empty:
            and_string += " AND games >= {}".format(self.gamesLL)

        if self.home_gamesUL not in empty:
            and_string += " AND home_games <= {}".format(self.home_gamesUL)

        if self.home_gamesLL not in empty:
            and_string += " AND home_games >= {}".format(self.home_gamesLL)

        if self.winsUL not in empty:
            and_string += " AND wins <= {}".format(self.winsUL)

        if self.winsLL not in empty:
            and_string += " AND wins >= {}".format(self.winsLL)

        if self.lossesUL not in empty:
            and_string += " AND losses <= {}".format(self.lossesUL)

        if self.lossesLL not in empty:
            and_string += " AND losses >= {}".format(self.lossesLL)

        if self.division_win not in empty:
            and_string += " AND division_win LIKE '%{}%'".format(
                self.division_win)

        if self.wild_card_win not in empty:
            and_string += " AND wild_card_win LIKE '%{}%'".format(
                self.wild_card_win)

        if self.league_win not in empty:
            and_string += " AND league_win LIKE '%{}%'".format(self.league_win)

        if self.world_series_win not in empty:
            and_string += " AND world_series_win LIKE '%{}%'".format(
                self.world_series_win)

        # Remove the first " AND " string
        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, team_code: str = None, name: str = None, year: int = None, league: str = None, division: str = None, park: str = None,
                 team_rank: int = None, games: int = None, home_games: int = None, wins: int = None, losses: int = None,
                 division_win: str = None, wild_card_win: str = None, league_win: str = None, world_series_win: str = None):
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.team_code in empty and self.name in empty and self.year in empty and self.league in empty and self.division in empty and self.park in empty and self.team_rank in empty and self.games in empty and self.home_games in empty and self.wins in empty and self.losses in empty and self.division_win in empty and self.wild_card_win in empty and self.league_win in empty and self.world_series_win in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']

        self.team_code = dict.get('sortTeamCode', None)
        if self.team_code not in options:
            self.team_code = None

        self.name = dict.get('sortName', None)
        if self.name not in options:
            self.name = None

        self.year = dict.get('sortYear', None)
        if self.year not in options:
            self.year = None

        self.league = dict.get('sortLeague', None)
        if self.league not in options:
            self.league = None

        self.division = dict.get('sortDivision', None)
        if self.division not in options:
            self.division = None

        self.park = dict.get('sortPark', None)
        if self.park not in options:
            self.park = None

        self.team_rank = dict.get('sortTeamRank', None)
        if self.team_rank not in options:
            self.team_rank = None

        self.games = dict.get('sortGames', None)
        if self.games not in options:
            self.games = None

        self.home_games = dict.get('sortHomeGames', None)
        if self.home_games not in options:
            self.home_games = None

        self.wins = dict.get('sortWins', None)
        if self.wins not in options:
            self.wins = None

        self.losses = dict.get('sortLosses', None)
        if self.losses not in options:
            self.losses = None

        self.division_win = dict.get('sortDivisionWin', None)
        if self.division_win not in options:
            self.division_win = None

        self.wild_card_win = dict.get('sortWildCardWin', None)
        if self.wild_card_win not in options:
            self.wild_card_win = None

        self.league_win = dict.get('sortLeagueWin', None)
        if self.league_win not in options:
            self.league_win = None

        self.world_series_win = dict.get('sortWorldSeriesWin', None)
        if self.world_series_win not in options:
            self.world_series_win = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        sort_dict = {
            'sortTeamCode': self.team_code,
            'sortName': self.name,
            'sortYear': self.year,
            'sortLeague': self.league,
            'sortDivision': self.division,
            'sortPark': self.park,
            'sortTeamRank': self.team_rank,
            'sortGames': self.games,
            'sortHomeGames': self.home_games,
            'sortWins': self.wins,
            'sortLosses': self.losses,
            'sortDivisionWin': self.division_win,
            'sortWildCardWin': self.wild_card_win,
            'sortLeagueWin': self.league_win,
            'sortWorldSeriesWin': self.world_series_win
        }
        # Don't return empty values
        sort_dict = {key: value for key,
                     value in sort_dict.items() if value not in empty}
        return sort_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.team_code not in empty:
            and_string += "team_code {}, ".format(self.team_code)

        if self.name not in empty:
            and_string += "name {}, ".format(self.name)

        if self.year not in empty:
            and_string += "year {}, ".format(self.year)

        if self.league not in empty:
            and_string += "league {}, ".format(self.league)

        if self.division not in empty:
            and_string += "division {}, ".format(self.division)

        if self.park not in empty:
            and_string += "park {}, ".format(self.park)

        if self.team_rank not in empty:
            and_string += "team_rank {}, ".format(self.team_rank)

        if self.games not in empty:
            and_string += "games {}, ".format(self.games)

        if self.home_games not in empty:
            and_string += "home_games {}, ".format(self.home_games)

        if self.wins not in empty:
            and_string += "wins {}, ".format(self.wins)

        if self.losses not in empty:
            and_string += "losses {}, ".format(self.losses)

        if self.division_win not in empty:
            and_string += "division_win {}, ".format(self.division_win)

        if self.wild_card_win not in empty:
            and_string += "wild_card_win {}, ".format(self.wild_card_win)

        if self.league_win not in empty:
            and_string += "league_win {}, ".format(self.league_win)

        if self.world_series_win not in empty:
            and_string += "world_series_win {}, ".format(self.world_series_win)

        # Remove the last ", " string
        if and_string != "":
            and_string = and_string[:-2]

        return and_string
