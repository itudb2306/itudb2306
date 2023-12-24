
# ID, nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
# ID, playerID, yearID, team_ID, lgID, inseason, G, W, L, teamRank, plyrMgr
class UpdateForm:
    def __init__(self, ID = None, playerID : str = None, yearID : str = None, team_ID : str = None, lgID : str = None, G_all : str = None, G_batting : str = None, G_defense : str = None, G_p : str = None, G_c : str = None, G_1b : str = None, G_2b : str = None, G_3b : str = None, G_ss : str = None, G_lf : str = None, G_cf : str = None, G_rf : str = None, G_of : str = None, G_dh : str = None, G_ph : str = None, G_pr : str = None):
        self.ID = ID
        self.playerID = playerID
        self.yearID = yearID
        self.team_ID = team_ID
        self.lgID = lgID
        self.G_all = G_all
        self.G_batting = G_batting
        self.G_defense = G_defense
        self.G_p = G_p
        self.G_c = G_c
        self.G_1b = G_1b
        self.G_2b = G_2b
        self.G_3b = G_3b
        self.G_ss = G_ss
        self.G_lf = G_lf
        self.G_cf = G_cf
        self.G_rf = G_rf
        self.G_of = G_of
        self.G_dh = G_dh
        self.G_ph = G_ph
        self.G_pr = G_pr

    def from_dict(self, dict):
        self.ID = dict.get('ID', None) # dict['player_id'] if 'player_id' in dict else None
        if self.ID is None:
            raise Exception("player_id is required(Primary Key column)")
        
        self.playerID = dict.get('playerID', None)
        self.yearID = dict.get('yearID', None)
        self.team_ID = dict.get('team_ID', None)
        self.lgID = dict.get('lgID', None)
        self.G_all = dict.get('G_all', None)
        self.G_batting = dict.get('G_batting', None)
        self.G_defense = dict.get('G_defense', None)
        self.G_p = dict.get('G_p', None)
        self.G_c = dict.get('G_c', None)
        self.G_1b = dict.get('G_1b', None)
        self.G_2b = dict.get('G_2b', None)
        self.G_3b = dict.get('G_3b', None)
        self.G_ss = dict.get('G_ss', None)
        self.G_lf = dict.get('G_lf', None)
        self.G_cf = dict.get('G_cf', None)
        self.G_rf = dict.get('G_rf', None)
        self.G_of = dict.get('G_of', None)
        self.G_dh = dict.get('G_dh', None)
        self.G_ph = dict.get('G_ph', None)
        self.G_pr = dict.get('G_pr', None)

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
        if self.G_all is not None and self.G_all != '':
            tuple += (self.G_all,)
        if self.G_batting is not None and self.G_batting != '':
            tuple += (self.G_batting,)
        if self.G_defense is not None and self.G_defense != '':
            tuple += (self.G_defense,)
        if self.G_p is not None and self.G_p != '':
            tuple += (self.G_p,)
        if self.G_c is not None and self.G_c != '':
            tuple += (self.G_c,)
        if self.G_1b is not None and self.G_1b != '':
            tuple += (self.G_1b,)
        if self.G_2b is not None and self.G_2b != '':
            tuple += (self.G_2b,)
        if self.G_3b is not None and self.G_3b != '':
            tuple += (self.G_3b,)
        if self.G_ss is not None and self.G_ss != '':
            tuple += (self.G_ss,)
        if self.G_lf is not None and self.G_lf != '':
            tuple += (self.G_lf,)
        if self.G_cf is not None and self.G_cf != '':
            tuple += (self.G_cf,)
        if self.G_rf is not None and self.G_rf != '':
            tuple += (self.G_rf,)
        if self.G_of is not None and self.G_of != '':
            tuple += (self.G_of,)
        if self.G_dh is not None and self.G_dh != '':
            tuple += (self.G_dh,)
        if self.G_ph is not None and self.G_ph != '':
            tuple += (self.G_ph,)
        if self.G_pr is not None and self.G_pr != '':
            tuple += (self.G_pr,)

        return tuple

#nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
class FilterForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, yearID : str = None, name : str = None, league : str = None, G_all : str = None, G_batting : str = None, G_defense : str = None, G_p : str = None, G_c : str = None, G_1b : str = None, G_2b : str = None, G_3b : str = None, G_ss : str = None, G_lf : str = None, G_cf : str = None, G_rf : str = None, G_of : str = None, G_dh : str = None, G_ph : str = None, G_pr : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.yearID = yearID
        self.name = name
        self.league = league
        self.G_all = G_all
        self.G_batting = G_batting
        self.G_defense = G_defense
        self.G_p = G_p
        self.G_c = G_c
        self.G_1b = G_1b
        self.G_2b = G_2b
        self.G_3b = G_3b
        self.G_ss = G_ss
        self.G_lf = G_lf
        self.G_cf = G_cf
        self.G_rf = G_rf
        self.G_of = G_of
        self.G_dh = G_dh
        self.G_ph = G_ph
        self.G_pr = G_pr


    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.yearID in empty and self.name in empty and self.league in empty and self.G_all in empty and self.G_batting in empty and self.G_defense in empty and self.G_p in empty and self.G_c in empty and self.G_1b in empty and self.G_2b in empty and self.G_3b in empty and self.G_ss in empty and self.G_lf in empty and self.G_cf in empty and self.G_rf in empty and self.G_of in empty and self.G_dh in empty and self.G_ph in empty and self.G_pr in empty

    def from_dict(self, dict):
        
        self.nameFirst = dict.get('filterNameFirst', None)
        self.nameLast = dict.get('filterNameLast', None)
        self.yearID = dict.get('filterYearID', None)
        self.name = dict.get('filterName', None)
        self.league = dict.get('filterLeague', None)
        self.G_all = dict.get('filterG_all', None)
        self.G_batting = dict.get('filterG_batting', None)
        self.G_defense = dict.get('filterG_defense', None)
        self.G_p = dict.get('filterG_p', None)
        self.G_c = dict.get('filterG_c', None)
        self.G_1b = dict.get('filterG_1b', None)
        self.G_2b = dict.get('filterG_2b', None)
        self.G_3b = dict.get('filterG_3b', None)
        self.G_ss = dict.get('filterG_ss', None)
        self.G_lf = dict.get('filterG_lf', None)
        self.G_cf = dict.get('filterG_cf', None)
        self.G_rf = dict.get('filterG_rf', None)
        self.G_of = dict.get('filterG_of', None)
        self.G_dh = dict.get('filterG_dh', None)
        self.G_ph = dict.get('filterG_ph', None)
        self.G_pr = dict.get('filterG_pr', None)


        return self
    
    def to_dict(self):
        filter_dict = {
            'filterNameFirst': self.nameFirst,
            'filterNameLast': self.nameLast,
            'filterYearID': self.yearID,
            'filterName': self.name,
            'filterLeague': self.league,
            'filterG_all': self.G_all,
            'filterG_batting': self.G_batting,
            'filterG_defense': self.G_defense,
            'filterG_p': self.G_p,
            'filterG_c': self.G_c,
            'filterG_1b': self.G_1b,
            'filterG_2b': self.G_2b,
            'filterG_3b': self.G_3b,
            'filterG_ss': self.G_ss,
            'filterG_lf': self.G_lf,
            'filterG_cf': self.G_cf,
            'filterG_rf': self.G_rf,
            'filterG_of': self.G_of,
            'filterG_dh': self.G_dh,
            'filterG_ph': self.G_ph,
            'filterG_pr': self.G_pr
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
        if self.G_all is not None and self.G_all != "":
            and_string += " AND G_all = '{}'".format(self.G_all)
        if self.G_batting is not None and self.G_batting != "":
            and_string += " AND G_batting = '{}'".format(self.G_batting)
        if self.G_defense is not None and self.G_defense != "":
            and_string += " AND G_defense = '{}'".format(self.G_defense)
        if self.G_p is not None and self.G_p != "":
            and_string += " AND G_p = '{}'".format(self.G_p)
        if self.G_c is not None and self.G_c != "":
            and_string += " AND G_c = '{}'".format(self.G_c)
        if self.G_1b is not None and self.G_1b != "":
            and_string += " AND G_1b = '{}'".format(self.G_1b)
        if self.G_2b is not None and self.G_2b != "":
            and_string += " AND G_2b = '{}'".format(self.G_2b)
        if self.G_3b is not None and self.G_3b != "":
            and_string += " AND G_3b = '{}'".format(self.G_3b)
        if self.G_ss is not None and self.G_ss != "":
            and_string += " AND G_ss = '{}'".format(self.G_ss)
        if self.G_lf is not None and self.G_lf != "":
            and_string += " AND G_lf = '{}'".format(self.G_lf)
        if self.G_cf is not None and self.G_cf != "":
            and_string += " AND G_cf = '{}'".format(self.G_cf)
        if self.G_rf is not None and self.G_rf != "":
            and_string += " AND G_rf = '{}'".format(self.G_rf)
        if self.G_of is not None and self.G_of != "":
            and_string += " AND G_of = '{}'".format(self.G_of)
        if self.G_dh is not None and self.G_dh != "":
            and_string += " AND G_dh = '{}'".format(self.G_dh)
        if self.G_ph is not None and self.G_ph != "":
            and_string += " AND G_ph = '{}'".format(self.G_ph)
        if self.G_pr is not None and self.G_pr != "":
            and_string += " AND G_pr = '{}'".format(self.G_pr)

        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, yearID : str = None, name : str = None, league : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.yearID = yearID
        self.name = name
        self.league = league


    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.yearID in empty and self.name in empty and self.league in empty

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


        return self
    
    def to_dict(self):
        sort_dict = {
            'sortNameFirst': self.nameFirst,
            'sortNameLast': self.nameLast,
            'sortYearID': self.yearID,
            'sortName': self.name,
            'sortLeague': self.league,
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


        if sort_string != "":
            sort_string = sort_string[:-2]

        return sort_string

# playerID, yearID, team_ID, lgID, inseason, G, W, L, teamRank, plyrMgr
class AddForm:
    def __init__(self, playerID : str = None, yearID : str = None, team_ID : str = None, lgID : str = None, G_all : str = None, G_batting : str = None, G_defense : str = None, G_p : str = None, G_c : str = None, G_1b : str = None, G_2b : str = None, G_3b : str = None, G_ss : str = None, G_lf : str = None, G_cf : str = None, G_rf : str = None, G_of : str = None, G_dh : str = None, G_ph : str = None, G_pr : str = None):
        self.playerID = playerID
        self.yearID = yearID
        self.team_ID = team_ID
        self.lgID = lgID
        self.G_all = G_all
        self.G_batting = G_batting
        self.G_defense = G_defense
        self.G_p = G_p
        self.G_c = G_c
        self.G_1b = G_1b
        self.G_2b = G_2b
        self.G_3b = G_3b
        self.G_ss = G_ss
        self.G_lf = G_lf
        self.G_cf = G_cf
        self.G_rf = G_rf
        self.G_of = G_of
        self.G_dh = G_dh
        self.G_ph = G_ph
        self.G_pr = G_pr
    
    def from_dict(self, dict):
        self.playerID = dict.get('playerID', None)
        self.yearID = dict.get('yearID', None)
        self.team_ID = dict.get('team_ID', None)
        self.lgID = dict.get('lgID', None)
        self.G_all = dict.get('G_all', None)
        self.G_batting = dict.get('G_batting', None)
        self.G_defense = dict.get('G_defense', None)
        self.G_p = dict.get('G_p', None)
        self.G_c = dict.get('G_c', None)
        self.G_1b = dict.get('G_1b', None)
        self.G_2b = dict.get('G_2b', None)
        self.G_3b = dict.get('G_3b', None)
        self.G_ss = dict.get('G_ss', None)
        self.G_lf = dict.get('G_lf', None)
        self.G_cf = dict.get('G_cf', None)
        self.G_rf = dict.get('G_rf', None)
        self.G_of = dict.get('G_of', None)
        self.G_dh = dict.get('G_dh', None)
        self.G_ph = dict.get('G_ph', None)
        self.G_pr = dict.get('G_pr', None)


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
        if self.G_all is not None and self.G_all != '':
            tuple += (self.G_all,)
        if self.G_batting is not None and self.G_batting != '':
            tuple += (self.G_batting,)
        if self.G_defense is not None and self.G_defense != '':
            tuple += (self.G_defense,)
        if self.G_p is not None and self.G_p != '':
            tuple += (self.G_p,)
        if self.G_c is not None and self.G_c != '':
            tuple += (self.G_c,)
        if self.G_1b is not None and self.G_1b != '':
            tuple += (self.G_1b,)
        if self.G_2b is not None and self.G_2b != '':
            tuple += (self.G_2b,)
        if self.G_3b is not None and self.G_3b != '':
            tuple += (self.G_3b,)
        if self.G_ss is not None and self.G_ss != '':
            tuple += (self.G_ss,)
        if self.G_lf is not None and self.G_lf != '':
            tuple += (self.G_lf,)
        if self.G_cf is not None and self.G_cf != '':
            tuple += (self.G_cf,)
        if self.G_rf is not None and self.G_rf != '':
            tuple += (self.G_rf,)
        if self.G_of is not None and self.G_of != '':
            tuple += (self.G_of,)
        if self.G_dh is not None and self.G_dh != '':
            tuple += (self.G_dh,)
        if self.G_ph is not None and self.G_ph != '':
            tuple += (self.G_ph,)
        if self.G_pr is not None and self.G_pr != '':
            tuple += (self.G_pr,)


        return tuple