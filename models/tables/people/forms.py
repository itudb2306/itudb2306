

class UpdateForm:
    def __init__(self, playerId : str = None, nameFirst : str = None, nameLast : str = None, nameGiven : str = None, birth_date : str = None, birthCountry : str = None, weight : str = None, height : str = None, bats : str = None, throws : str = None):
        self.playerId = playerId
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.nameGiven = nameGiven
        self.birth_date = birth_date
        self.birthCountry = birthCountry
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws
    
    def from_dict(self, dict):
        self.playerId = dict.get('player_id', None) # dict['player_id'] if 'player_id' in dict else None
        if self.playerId is None:
            raise Exception("player_id is required(Primary Key column)")
        
        self.nameFirst = dict.get('name_first', None)
        self.nameLast = dict.get('name_last', None)
        self.nameGiven = dict.get('name_given', None)
        self.birth_date = dict.get('birth_date', None)
        self.birthCountry = dict.get('birth_country', None)
        self.weight = dict.get('weight', None)
        self.height = dict.get('height', None)
        self.bats = dict.get('bats', None)
        self.throws = dict.get('throws', None)

        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.playerId is not None and self.playerId != '':
            tuple += (self.playerId,)

        if self.nameFirst is not None and self.nameFirst != '':
            tuple += (self.nameFirst,)

        if self.nameLast is not None and self.nameLast != '':
            tuple += (self.nameLast,)

        if self.nameGiven is not None and self.nameGiven != '':
            tuple += (self.nameGiven,)

        if self.birth_date is not None and self.birth_date != '':
            tuple += (self.birth_date,)

        if self.birthCountry is not None and self.birthCountry != '':
            tuple += (self.birthCountry,)

        if self.weight is not None and self.weight != '':
            tuple += (self.weight,)

        if self.height is not None and self.height != '':
            tuple += (self.height,)

        if self.bats is not None and self.bats != '':
            tuple += (self.bats,)

        if self.throws is not None and self.throws != '':
            tuple += (self.throws,)

        return tuple

class FilterForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, nameGiven : str = None, birth_date : str = None, birthCountry : str = None, weight : str = None, height : str = None, bats : str = None, throws : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.nameGiven = nameGiven
        self.birth_date = birth_date
        self.birthCountry = birthCountry
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws

    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.nameGiven in empty and self.birth_date in empty and self.birthCountry in empty and self.weight in empty and self.height in empty and self.bats in empty and self.throws in empty

    def from_dict(self, dict):
        
        self.nameFirst = dict.get('filterNameFirst', None)
        if self.nameFirst == "":
            self.nameFirst = None
        self.nameLast = dict.get('filterNameLast', None)
        if self.nameLast == "":
            self.nameLast = None
        self.nameGiven = dict.get('filterNameGiven', None)
        if self.nameGiven == "":
            self.nameGiven = None
        self.birth_date = dict.get('filterBirthDate', None)
        if self.birth_date == "":
            self.birth_date = None
        self.birthCountry = dict.get('filterBirthCountry', None)
        if self.birthCountry == "":
            self.birthCountry = None
        self.weight = dict.get('filterWeight', None)
        if self.weight == "":
            self.weight = None
        self.height = dict.get('filterHeight', None)
        if self.height == "":
            self.height = None
        self.bats = dict.get('filterBats', None)
        if self.bats == "":
            self.bats = None
        self.throws = dict.get('filterThrows', None)
        if self.throws == "":
            self.throws = None

        return self
    
    def to_dict(self):
        filter_dict = {
            'filterNameFirst': self.nameFirst,
            'filterNameLast': self.nameLast,
            'filterNameGiven': self.nameGiven,
            'filterBirthDate': self.birth_date,
            'filterBirthCountry': self.birthCountry,
            'filterWeight': self.weight,
            'filterHeight': self.height,
            'filterBats': self.bats,
            'filterThrows': self.throws
        }
        filter_dict = {k: v for k, v in filter_dict.items() if v != '' and v is not None and v != 'None'}
        return filter_dict
    
    def to_and_string(self):
        and_string = ""

        if self.nameFirst is not None and self.nameFirst != "":
            and_string += " AND nameFirst LIKE '%{}%'".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            and_string += " AND nameLast LIKE '%{}%'".format(self.nameLast)
        if self.nameGiven is not None and self.nameGiven != "":
            and_string += " AND nameGiven LIKE '%{}%'".format(self.nameGiven)
        if self.birth_date is not None and self.birth_date != "":
            and_string += " AND birth_date LIKE '%{}%'".format(self.birth_date)
        if self.birthCountry is not None and self.birthCountry != "":
            and_string += " AND birthCountry LIKE '%{}%'".format(self.birthCountry)
        if self.weight is not None and self.weight != "":
            and_string += " AND weight LIKE '%{}%'".format(self.weight)
        if self.height is not None and self.height != "":
            and_string += " AND height LIKE '%{}%'".format(self.height)
        if self.bats is not None and self.bats != "":
            and_string += " AND bats LIKE '%{}%'".format(self.bats)
        if self.throws is not None and self.throws != "":
            and_string += " AND throws LIKE '%{}%'".format(self.throws)

        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, nameGiven : str = None, birth_date : str = None, birthCountry : str = None, weight : str = None, height : str = None, bats : str = None, throws : str = None):
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.nameGiven = nameGiven
        self.birth_date = birth_date
        self.birthCountry = birthCountry
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws

    def is_empty(self):
        empty = [None, '', 'None']
        return self.nameFirst in empty and self.nameLast in empty and self.nameGiven in empty and self.birth_date in empty and self.birthCountry in empty and self.weight in empty and self.height in empty and self.bats in empty and self.throws in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']
        self.nameFirst = dict.get('sortNameFirst', None)
        if self.nameFirst not in options:
            self.nameFirst = None
        self.nameLast = dict.get('sortNameLast', None)
        if self.nameLast not in options:
            self.nameLast = None
        self.nameGiven = dict.get('sortNameGiven', None)
        if self.nameGiven not in options:
            self.nameGiven = None
        self.birth_date = dict.get('sortBirthDate', None)
        if self.birth_date not in options:
            self.birth_date = None
        self.birthCountry = dict.get('sortBirthCountry', None)
        if self.birthCountry not in options:
            self.birthCountry = None
        self.weight = dict.get('sortWeight', None)
        if self.weight not in options:
            self.weight = None
        self.height = dict.get('sortHeight', None)
        if self.height not in options:
            self.height = None
        self.bats = dict.get('sortBats', None)
        if self.bats not in options:
            self.bats = None
        self.throws = dict.get('sortThrows', None)
        if self.throws not in options:
            self.throws = None

        return self
    
    def to_dict(self):
        sort_dict = {
            'sortNameFirst': self.nameFirst,
            'sortNameLast': self.nameLast,
            'sortNameGiven': self.nameGiven,
            'sortBirthDate': self.birth_date,
            'sortBirthCountry': self.birthCountry,
            'sortWeight': self.weight,
            'sortHeight': self.height,
            'sortBats': self.bats,
            'sortThrows': self.throws
        }
        sort_dict = {k: v for k, v in sort_dict.items() if v != '' and v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""

        if self.nameFirst is not None and self.nameFirst != "":
            sort_string += "nameFirst {}, ".format(self.nameFirst)
        if self.nameLast is not None and self.nameLast != "":
            sort_string += "nameLast {}, ".format(self.nameLast)
        if self.nameGiven is not None and self.nameGiven != "":
            sort_string += "nameGiven {}, ".format(self.nameGiven)
        if self.birth_date is not None and self.birth_date != "":
            sort_string += "birth_date {}, ".format(self.birth_date)
        if self.birthCountry is not None and self.birthCountry != "":
            sort_string += "birthCountry {}, ".format(self.birthCountry)
        if self.weight is not None and self.weight != "":
            sort_string += "weight {}, ".format(self.weight)
        if self.height is not None and self.height != "":
            sort_string += "height {}, ".format(self.height)
        if self.bats is not None and self.bats != "":
            sort_string += "bats {}, ".format(self.bats)
        if self.throws is not None and self.throws != "":
            sort_string += "throws {}, ".format(self.throws)

        if sort_string != "":
            sort_string = sort_string[:-2]

        return sort_string


class AddForm:
    def __init__(self, nameFirst : str = None, nameLast : str = None, nameGiven : str = None, birth_date : str = None, birthCountry : str = None, weight : str = None, height : str = None, bats : str = None, throws : str = None):
        self.playerID = None
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.nameGiven = nameGiven
        self.birth_date = birth_date
        self.birthCountry = birthCountry
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws
    
    def from_dict(self, dict):
        self.nameFirst = dict.get('name_first', None)
        self.nameLast = dict.get('name_last', None)
        self.nameGiven = dict.get('name_given', None)
        self.birth_date = dict.get('birth_date', None)
        self.birthCountry = dict.get('birth_country', None)
        self.weight = dict.get('weight', None)
        self.height = dict.get('height', None)
        self.bats = dict.get('bats', None)
        self.throws = dict.get('throws', None)

        return self
    
    def to_dict(self):
        return self.__dict__
    
    def to_tuple(self):
        tuple = ()

        if self.playerID is not None and self.playerID != '':
            tuple += (self.playerID,)

        if self.nameFirst is not None and self.nameFirst != '':
            tuple += (self.nameFirst,)

        if self.nameLast is not None and self.nameLast != '':
            tuple += (self.nameLast,)

        if self.nameGiven is not None and self.nameGiven != '':
            tuple += (self.nameGiven,)

        if self.birth_date is not None and self.birth_date != '':
            tuple += (self.birth_date,)

        if self.birthCountry is not None and self.birthCountry != '':
            tuple += (self.birthCountry,)

        if self.weight is not None and self.weight != '':
            tuple += (self.weight,)

        if self.height is not None and self.height != '':
            tuple += (self.height,)

        if self.bats is not None and self.bats != '':
            tuple += (self.bats,)

        if self.throws is not None and self.throws != '':
            tuple += (self.throws,)

        return tuple