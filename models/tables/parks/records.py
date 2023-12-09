class Record:
    def __init__(self, ID: int = None, parkalias: str = None, parkkey: str = None,
                 parkname: str = None, city: str = None, state: str = None, country: str = None):
        self.ID = ID
        self.parkalias = parkalias
        self.parkkey = parkkey
        self.parkname = parkname
        self.city = city
        self.state = state
        self.country = country

    # record.ID -> record[ID]
    # No need for this, since we can use record.ID in jinja2 templates
    # def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.ID = list[0]
        self.parkalias = list[1]
        self.parkkey = list[2]
        self.parkname = list[3]
        self.city = list[4]
        self.state = list[5]
        self.country = list[6]
        return self

    def from_dict(self, dict):
        self.ID = dict['ID']
        self.parkalias = dict['park_alias']
        self.parkkey = dict['park_key']
        self.parkname = dict['park_name']
        self.city = dict['city']
        self.state = dict['state']
        self.country = dict['country']
        return self

    def to_list(self):
        return [self.ID, self.parkalias, self.parkkey, self.parkname, self.city, self.state, self.country]

    def to_dict(self):
        return {
            'ID': self.ID,
            'park_alias': self.parkalias,
            'park_key': self.parkkey,
            'park_name': self.parkname,
            'city': self.city,
            'state': self.state,
            'country': self.country
        }


class Records:
    def __init__(self, records: list = None):
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
