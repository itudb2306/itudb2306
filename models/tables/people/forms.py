

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

class SearchForm:
    def __init__(self, col : str = None, val : str = None):
        self.col = col
        self.val = val
    
    def from_dict(self, dict):
        self.col = dict.get('col', None)
        self.val = dict.get('val', None)

        return self
    
    def to_dict(self):
        return self.__dict__