

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
        return {
            'name_first': self.nameFirst,
            'name_last': self.nameLast,
            'name_given': self.nameGiven,
            'birth_date': self.birth_date,
            'birth_country': self.birthCountry,
            'weight': self.weight,
            'height': self.height,
            'bats': self.bats,
            'throws': self.throws
        }
    
    def to_and_string(self):
        and_string = ""
        
        if self.nameFirst is not None and self.nameFirst != "":
            and_string += " AND nameFirst = '%s'" % self.nameFirst
        if self.nameLast is not None and self.nameLast != "":
            and_string += " AND nameLast = '%s'" % self.nameLast
        if self.nameGiven is not None and self.nameGiven != "":
            and_string += " AND nameGiven = '%s'" % self.nameGiven
        if self.birth_date is not None and self.birth_date != "":
            and_string += " AND birth_date = '%s'" % self.birth_date
        if self.birthCountry is not None and self.birthCountry != "":
            and_string += " AND birthCountry = '%s'" % self.birthCountry
        if self.weight is not None and self.weight != "":
            and_string += " AND weight = '%s'" % self.weight
        if self.height is not None and self.height != "":
            and_string += " AND height = '%s'" % self.height
        if self.bats is not None and self.bats != "":
            and_string += " AND bats = '%s'" % self.bats
        if self.throws is not None and self.throws != "":
            and_string += " AND throws = '%s'" % self.throws
        
        if and_string != "":
            and_string = and_string[5:]

        return and_string