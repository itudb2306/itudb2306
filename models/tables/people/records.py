


class Record:
    def __init__(self, player_id : str = None, name_first : str = None, name_last : str = None, name_given : str = None, birth_date : str = None, birth_country : str = None, weight : str = None, height : str = None, bats : str = None, throws : str = None):
        self.player_id = player_id
        self.name_first = name_first
        self.name_last = name_last
        self.name_given = name_given
        self.birth_date = birth_date
        self.birth_country = birth_country
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws

    # record.player_id -> record['player_id']
    # No need for this, since we can use record.player_id in jinja2 templates
    #def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.player_id = list[0]
        self.name_first = list[13]
        self.name_last = list[14]
        self.name_given = list[15]
        self.birth_date = list[25]
        self.birth_country = list[4]
        self.weight = list[16]
        self.height = list[17]
        self.bats = list[18]
        self.throws = list[19]
        return self

    def from_dict(self, dict):
        self.player_id = dict['player_id']
        self.name_first = dict['name_first']
        self.name_last = dict['name_last']
        self.name_given = dict['name_given']
        self.birth_date = dict['birth_date']
        self.birth_country = dict['birth_country']
        self.weight = dict['weight']
        self.height = dict['height']
        self.bats = dict['bats']
        self.throws = dict['throws']
        return self

    def to_list(self):
        return [self.player_id, self.name_first, self.name_last, self.name_given, self.birth_date, self.birth_country, self.weight, self.height, self.bats, self.throws]

    def to_dict(self):
        return {
            'player_id': self.player_id,
            'name_first': self.name_first,
            'name_last': self.name_last,
            'name_given': self.name_given,
            'birth_date': self.birth_date,
            'birth_country': self.birth_country,
            'weight': self.weight,
            'height': self.height,
            'bats': self.bats,
            'throws': self.throws
        }
    

class Records:
    def __init__(self, records : list = None):
        self.records = records

    def from_list(self, list):
        self.records = []
        for row in list:
            record = Record().from_list(row)
            self.records.append(record)

    def from_dict(self, dict):
        self.records = []
        for row in dict:
            self.records.append(Record().from_dict(row))

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
    


