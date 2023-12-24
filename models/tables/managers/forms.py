
# ID, nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
# ID, playerID, yearID, team_ID, lgID, inseason, G, W, L, teamRank, plyrMgr
class UpdateForm:
    def __init__(self, ID = None, playerID : str = None, yearID : str = None, team_ID : str = None, lgID : str = None, inseason : str = None, G : str = None, W : str = None, L : str = None, plyrMgr : str = None):
        self.ID = ID
        self.playerID = playerID
        self.yearID = yearID
        self.team_ID = team_ID
        self.lgID = lgID
        self.inseason = inseason
        self.G = G
        self.W = W
        self.L = L
        self.plyrMgr = plyrMgr

    def from_dict(self, dict):
        self.ID = dict.get('ID', None) # dict['player_id'] if 'player_id' in dict else None
        if self.ID is None:
            raise Exception("player_id is required(Primary Key column)")
        
        self.playerID = dict.get('playerID', None)
        self.yearID = dict.get('yearID', None)
        self.team_ID = dict.get('team_ID', None)
        self.lgID = dict.get('lgID', None)
        self.inseason = dict.get('inseason', None)
        self.G = dict.get('G', None)
        self.W = dict.get('W', None)
        self.L = dict.get('L', None)
        self.plyrMgr = dict.get('plyrMgr', None)

        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.ID is not None and self.ID != '':
            tuple += (self.ID,)
        if self.playerID is not None and self.playerID != '':
            tuple += (self.playerID,)
        if self.yearID is not None and self.yearID != '':
            tuple += (self.yearID,)
        if self.team_ID is not None and self.team_ID != '':
            tuple += (self.team_ID,)
        if self.lgID is not None and self.lgID != '':
            tuple += (self.lgID,)
        if self.inseason is not None and self.inseason != '':
            tuple += (self.inseason,)
        if self.G is not None and self.G != '':
            tuple += (self.G,)
        if self.W is not None and self.W != '':
            tuple += (self.W,)
        if self.L is not None and self.L != '':
            tuple += (self.L,)
        # if self.teamRank is not None and self.teamRank != '':
        #     tuple += (self.teamRank,)
        if self.plyrMgr is not None and self.plyrMgr != '':
            tuple += (self.plyrMgr,)

        return tuple

#nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
class FilterForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, yearID : str = None, name : str = None, league : str = None, inseason : str = None, G : str = None, W : str = None, L : str = None, teamRank : str = None, plyrMgr : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.yearID = yearID
        self.name = name
        self.league = league
        self.inseason = inseason
        self.G = G
        self.W = W
        self.L = L
        self.teamRank = teamRank
        self.plyrMgr = plyrMgr


    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.yearID in empty and self.name in empty and self.league in empty and self.inseason in empty and self.G in empty and self.W in empty and self.L in empty and self.teamRank in empty and self.plyrMgr in empty

    def from_dict(self, dict):
        
        self.nameFirst = dict.get('filterNameFirst', None)
        self.nameLast = dict.get('filterNameLast', None)
        self.yearID = dict.get('filterYearID', None)
        self.name = dict.get('filterName', None)
        self.league = dict.get('filterLeague', None)
        self.inseason = dict.get('filterInseason', None)
        self.G = dict.get('filterG', None)
        self.W = dict.get('filterW', None)
        self.L = dict.get('filterL', None)
        self.teamRank = dict.get('filterTeamRank', None)
        self.plyrMgr = dict.get('filterPlyrMgr', None)


        return self
    
    def to_dict(self):
        filter_dict = {
            'filterNameFirst': self.nameFirst,
            'filterNameLast': self.nameLast,
            'filterYearID': self.yearID,
            'filterName': self.name,
            'filterLeague': self.league,
            'filterInseason': self.inseason,
            'filterG': self.G,
            'filterW': self.W,
            'filterL': self.L,
            'filterTeamRank': self.teamRank,
            'filterPlyrMgr': self.plyrMgr
        }
        filter_dict = {k: v for k, v in filter_dict.items() if v != '' and v is not None and v != 'None'}
        return filter_dict
    
    def to_and_string(self):
        and_string = ""

        if self.nameFirst is not None and self.nameFirst != "":
            and_string += " AND nameFirst = '{}'".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            and_string += " AND nameLast = '{}'".format(self.nameLast)
        if self.yearID is not None and self.yearID != "":
            and_string += " AND yearID = '{}'".format(self.yearID)
        if self.name is not None and self.name != "":
            and_string += " AND name = '{}'".format(self.name)
        if self.league is not None and self.league != "":
            and_string += " AND league = '{}'".format(self.league)
        if self.inseason is not None and self.inseason != "":
            and_string += " AND inseason = '{}'".format(self.inseason)
        if self.G is not None and self.G != "":
            and_string += " AND G = '{}'".format(self.G)
        if self.W is not None and self.W != "":
            and_string += " AND W = '{}'".format(self.W)
        if self.L is not None and self.L != "":
            and_string += " AND L = '{}'".format(self.L)
        if self.teamRank is not None and self.teamRank != "":
            and_string += " AND teamRank = '{}'".format(self.teamRank)
        if self.plyrMgr is not None and self.plyrMgr != "":
            and_string += " AND plyrMgr = '{}'".format(self.plyrMgr)

        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, yearID : str = None, name : str = None, league : str = None, inseason : str = None, G : str = None, W : str = None, L : str = None, teamRank : str = None, plyrMgr : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.yearID = yearID
        self.name = name
        self.league = league
        self.inseason = inseason
        self.G = G
        self.W = W
        self.L = L
        self.teamRank = teamRank
        self.plyrMgr = plyrMgr

    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.yearID in empty and self.name in empty and self.league in empty and self.inseason in empty and self.G in empty and self.W in empty and self.L in empty and self.teamRank in empty and self.plyrMgr in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']
        self.nameFirst = dict.get('sortNameFirst', None)
        if self.nameFirst not in options:
            self.nameFirst = None
        self.nameLast = dict.get('sortNameLast', None)
        if self.nameLast not in options:
            self.nameLast = None
        self.yearID = dict.get('sortYearID', None)
        if self.yearID not in options:
            self.yearID = None
        self.name = dict.get('sortName', None)
        if self.name not in options:
            self.name = None
        self.league = dict.get('sortLeague', None)
        if self.league not in options:
            self.league = None
        self.inseason = dict.get('sortInseason', None)
        if self.inseason not in options:
            self.inseason = None
        self.G = dict.get('sortG', None)
        if self.G not in options:
            self.G = None
        self.W = dict.get('sortW', None)
        if self.W not in options:
            self.W = None
        self.L = dict.get('sortL', None)
        if self.L not in options:
            self.L = None
        self.teamRank = dict.get('sortTeamRank', None)
        if self.teamRank not in options:
            self.teamRank = None
        self.plyrMgr = dict.get('sortPlyrMgr', None)
        if self.plyrMgr not in options:
            self.plyrMgr = None


        return self
    
    def to_dict(self):
        sort_dict = {
            'sortNameFirst': self.nameFirst,
            'sortNameLast': self.nameLast,
            'sortYearID': self.yearID,
            'sortName': self.name,
            'sortLeague': self.league,
            'sortInseason': self.inseason,
            'sortG': self.G,
            'sortW': self.W,
            'sortL': self.L,
            'sortTeamRank': self.teamRank,
            'sortPlyrMgr': self.plyrMgr
        }
        sort_dict = {k: v for k, v in sort_dict.items() if v != '' and v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""

        if self.nameFirst is not None and self.nameFirst != "":
            sort_string += "nameFirst {}, ".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            sort_string += "nameLast {}, ".format(self.nameLast)
        if self.yearID is not None and self.yearID != "":
            sort_string += "yearID {}, ".format(self.yearID)
        if self.name is not None and self.name != "":
            sort_string += "name {}, ".format(self.name)
        if self.league is not None and self.league != "":
            sort_string += "league {}, ".format(self.league)
        if self.inseason is not None and self.inseason != "":
            sort_string += "inseason {}, ".format(self.inseason)
        if self.G is not None and self.G != "":
            sort_string += "G {}, ".format(self.G)
        if self.W is not None and self.W != "":
            sort_string += "W {}, ".format(self.W)
        if self.L is not None and self.L != "":
            sort_string += "L {}, ".format(self.L)
        if self.teamRank is not None and self.teamRank != "":
            sort_string += "teamRank {}, ".format(self.teamRank)
        if self.plyrMgr is not None and self.plyrMgr != "":
            sort_string += "plyrMgr {}, ".format(self.plyrMgr)


        if sort_string != "":
            sort_string = sort_string[:-2]

        return sort_string

# playerID, yearID, team_ID, lgID, inseason, G, W, L, teamRank, plyrMgr
class AddForm:
    def __init__(self, playerID : str = None, yearID : str = None, team_ID : str = None, lgID : str = None, inseason : str = None, G : str = None, W : str = None, L : str = None, teamRank : str = None, plyrMgr : str = None):
        self.playerID = playerID
        self.yearID = yearID
        self.team_ID = team_ID
        self.lgID = lgID
        self.inseason = inseason
        self.G = G
        self.W = W
        self.L = L
        self.teamRank = teamRank
        self.plyrMgr = plyrMgr
    
    def from_dict(self, dict):
        self.playerID = dict.get('playerID', None)
        self.yearID = dict.get('yearID', None)
        self.team_ID = dict.get('team_ID', None)
        self.lgID = dict.get('lgID', None)
        self.inseason = dict.get('inseason', None)
        self.G = dict.get('G', None)
        self.W = dict.get('W', None)
        self.L = dict.get('L', None)
        self.teamRank = dict.get('teamRank', None)
        self.plyrMgr = dict.get('plyrMgr', None)
        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.playerID is not None and self.playerID != '':
            tuple += (self.playerID,)
        if self.yearID is not None and self.yearID != '':
            tuple += (self.yearID,)
        if self.team_ID is not None and self.team_ID != '':
            tuple += (self.team_ID,)
        if self.lgID is not None and self.lgID != '':
            tuple += (self.lgID,)
        if self.inseason is not None and self.inseason != '':
            tuple += (self.inseason,)
        if self.G is not None and self.G != '':
            tuple += (self.G,)
        if self.W is not None and self.W != '':
            tuple += (self.W,)
        if self.L is not None and self.L != '':
            tuple += (self.L,)
        if self.teamRank is not None and self.teamRank != '':
            tuple += (self.teamRank,)
        if self.plyrMgr is not None and self.plyrMgr != '':
            tuple += (self.plyrMgr,)

        return tuple