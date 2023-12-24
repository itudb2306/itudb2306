
# ID, yearID, votedBy, ballots, needed, votes, inducted, category, nameFirst, nameLast,

class UpdateForm:
    def __init__(self, ID = None, yearID = None, votedBy = None, ballots = None, needed = None, votes = None, inducted = None, category = None):
        self.ID = ID
        self.yearID = yearID
        self.votedBy = votedBy
        self.ballots = ballots
        self.needed = needed
        self.votes = votes
        self.inducted = inducted
        self.category = category

    def from_dict(self, dict):
        self.ID = dict.get('ID', None) # dict['player_id'] if 'player_id' in dict else None
        if self.ID is None:
            raise Exception("player_id is required(Primary Key column)")
        
        self.yearID = dict.get('yearID', None)
        self.votedBy = dict.get('votedBy', None)
        self.ballots = dict.get('ballots', None)
        self.needed = dict.get('needed', None)
        self.votes = dict.get('votes', None)
        self.inducted = dict.get('inducted', None)
        self.category = dict.get('category', None)

        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.ID is not None and self.ID != '':
            tuple += (self.ID,)
        if self.yearID is not None and self.yearID != '':
            tuple += (self.yearID,)
        if self.votedBy is not None and self.votedBy != '':
            tuple += (self.votedBy,)
        if self.ballots is not None and self.ballots != '':
            tuple += (self.ballots,)
        if self.needed is not None and self.needed != '':
            tuple += (self.needed,)
        if self.votes is not None and self.votes != '':
            tuple += (self.votes,)
        if self.inducted is not None and self.inducted != '':
            tuple += (self.inducted,)
        if self.category is not None and self.category != '':
            tuple += (self.category,)

        return tuple

class FilterForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, yearID = None, votedBy : str = None, ballots = None, needed = None, votes = None, inducted : str = None, category : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.yearID = yearID
        self.votedBy = votedBy
        self.ballots = ballots
        self.needed = needed
        self.votes = votes
        self.inducted = inducted
        self.category = category


    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.yearID in empty and self.votedBy in empty and self.ballots in empty and self.needed in empty and self.votes in empty and self.inducted in empty and self.category in empty

    def from_dict(self, dict):
        
        self.nameFirst = dict.get('filterNameFirst', None)
        self.nameLast = dict.get('filterNameLast', None)
        self.yearID = dict.get('filterYearID', None)
        self.votedBy = dict.get('filterVotedBy', None)
        self.ballots = dict.get('filterBallots', None)
        self.needed = dict.get('filterNeeded', None)
        self.votes = dict.get('filterVotes', None)
        self.inducted = dict.get('filterInducted', None)
        self.category = dict.get('filterCategory', None)

        return self
    
    def to_dict(self):
        filter_dict = {
            'filterNameFirst': self.nameFirst,
            'filterNameLast': self.nameLast,
            'filterYearID': self.yearID,
            'filterVotedBy': self.votedBy,
            'filterBallots': self.ballots,
            'filterNeeded': self.needed,
            'filterVotes': self.votes,
            'filterInducted': self.inducted,
            'filterCategory': self.category
        }
        filter_dict = {k: v for k, v in filter_dict.items() if v != '' and v is not None and v != 'None'}
        return filter_dict
    
    def to_and_string(self):
        and_string = ""

        if self.yearID is not None and self.yearID != "":
            and_string += " AND yearID LIKE '%{}%'".format(self.yearID)
        if self.votedBy is not None and self.votedBy != "":
            and_string += " AND votedBy LIKE '%{}%'".format(self.votedBy)
        if self.ballots is not None and self.ballots != "":
            and_string += " AND ballots LIKE '%{}%'".format(self.ballots)
        if self.needed is not None and self.needed != "":
            and_string += " AND needed LIKE '%{}%'".format(self.needed)
        if self.votes is not None and self.votes != "":
            and_string += " AND votes LIKE '%{}%'".format(self.votes)
        if self.inducted is not None and self.inducted != "":
            and_string += " AND inducted LIKE '%{}%'".format(self.inducted)
        if self.category is not None and self.category != "":
            and_string += " AND category LIKE '%{}%'".format(self.category)
        if self.nameFirst is not None and self.nameFirst != "":
            and_string += " AND nameFirst LIKE '%{}%'".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            and_string += " AND nameLast LIKE '%{}%'".format(self.nameLast)


        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, yearID : str = None, votedBy : str = None, ballots : str = None, needed : str = None, votes : str = None, inducted : str = None, category : str = None, nameFirst : str = None, nameLast : str = None):
        self.yearID = yearID
        self.votedBy = votedBy
        self.ballots = ballots
        self.needed = needed
        self.votes = votes
        self.inducted = inducted
        self.category = category
        self.nameFirst = nameFirst
        self.nameLast = nameLast

    def is_empty(self):
        empty = [None, '', 'None']
        return self.yearID in empty and self.votedBy in empty and self.ballots in empty and self.needed in empty and self.votes in empty and self.inducted in empty and self.category in empty and self.nameFirst in empty and self.nameLast in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']
        self.yearID = dict.get('sortYearID', None)
        if self.yearID not in options:
            self.yearID = None
        self.votedBy = dict.get('sortVotedBy', None)
        if self.votedBy not in options:
            self.votedBy = None
        self.ballots = dict.get('sortBallots', None)
        if self.ballots not in options:
            self.ballots = None
        self.needed = dict.get('sortNeeded', None)
        if self.needed not in options:
            self.needed = None
        self.votes = dict.get('sortVotes', None)
        if self.votes not in options:
            self.votes = None
        self.inducted = dict.get('sortInducted', None)
        if self.inducted not in options:
            self.inducted = None
        self.category = dict.get('sortCategory', None)
        if self.category not in options:
            self.category = None
        self.nameFirst = dict.get('sortNameFirst', None)
        if self.nameFirst not in options:
            self.nameFirst = None
        self.nameLast = dict.get('sortNameLast', None)
        if self.nameLast not in options:
            self.nameLast = None

        return self
    
    def to_dict(self):
        sort_dict = {
            'sortYearID': self.yearID,
            'sortVotedBy': self.votedBy,
            'sortBallots': self.ballots,
            'sortNeeded': self.needed,
            'sortVotes': self.votes,
            'sortInducted': self.inducted,
            'sortCategory': self.category,
            'sortNameFirst': self.nameFirst,
            'sortNameLast': self.nameLast
        }
        sort_dict = {k: v for k, v in sort_dict.items() if v != '' and v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""

        if self.yearID is not None and self.yearID != "":
            sort_string += "yearID {}, ".format(self.yearID)
        if self.votedBy is not None and self.votedBy != "":
            sort_string += "votedBy {}, ".format(self.votedBy)
        if self.ballots is not None and self.ballots != "":
            sort_string += "ballots {}, ".format(self.ballots)
        if self.needed is not None and self.needed != "":
            sort_string += "needed {}, ".format(self.needed)
        if self.votes is not None and self.votes != "":
            sort_string += "votes {}, ".format(self.votes)
        if self.inducted is not None and self.inducted != "":
            sort_string += "inducted {}, ".format(self.inducted)
        if self.category is not None and self.category != "":
            sort_string += "category {}, ".format(self.category)
        if self.nameFirst is not None and self.nameFirst != "":
            sort_string += "nameFirst {}, ".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            sort_string += "nameLast {}, ".format(self.nameLast)


        if sort_string != "":
            sort_string = sort_string[:-2]

        return sort_string


class AddForm:
    def __init__(self, playerID : str = None, yearID : str = None, votedBy : str = None, ballots : str = None, needed : str = None, votes : str = None, inducted : str = None, category : str = None):
        self.playerID = playerID
        self.yearID = yearID
        self.votedBy = votedBy
        self.ballots = ballots
        self.needed = needed
        self.votes = votes
        self.inducted = inducted
        self.category = category
    
    def from_dict(self, dict):
        self.playerID = dict.get('playerID', None)
        self.yearID = dict.get('yearID', None)
        self.votedBy = dict.get('votedBy', None)
        self.ballots = dict.get('ballots', None)
        self.needed = dict.get('needed', None)
        self.votes = dict.get('votes', None)
        self.inducted = dict.get('inducted', None)
        self.category = dict.get('category', None)

        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.playerID is not None and self.playerID != '':
            tuple += (self.playerID,)
        if self.yearID is not None and self.yearID != '':
            tuple += (self.yearID,)
        if self.votedBy is not None and self.votedBy != '':
            tuple += (self.votedBy,)
        if self.ballots is not None and self.ballots != '':
            tuple += (self.ballots,)
        if self.needed is not None and self.needed != '':
            tuple += (self.needed,)
        if self.votes is not None and self.votes != '':
            tuple += (self.votes,)
        if self.inducted is not None and self.inducted != '':
            tuple += (self.inducted,)
        if self.category is not None and self.category != '':
            tuple += (self.category,)

        return tuple