"""
    create view divisions_leagues as 
    select 
        l.lgID as lgID,
        l.league as league,
        l.active as lgActive,
        d.divID as divID,
        d.division as division, 
        d.active as divActive,
        d.ID as ID
    from divisions d, leagues l
    where
        d.lgID=l.lgID;
"""


class Record:
    def __init__(self, ID: int = None, divID: str = None, lgID: str = None, league: str = None,
                 division: str = None, divActive: str = None, lgActive: str = None):
        self.lgID = lgID
        self.league = league
        self.lgActive = lgActive
        self.divID = divID
        self.division = division
        self.divActive = divActive
        self.ID = ID

    # record.ID -> record[ID]
    # No need for this, since we can use record.ID in jinja2 templates
    # def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.lgID = list[0]
        self.league = list[1]
        self.lgActive = list[2]
        self.divID = list[3]
        self.division = list[4]
        self.divActive = list[5]
        self.ID = list[6]
        return self

    def from_dict(self, dict):
        self.lgID = dict.get('lgID', None)
        self.league = dict.get('league', None)
        self.lgActive = dict.get('lgActive', None)
        self.divID = dict.get('divID', None)
        self.division = dict.get('division', None)
        self.divActive = dict.get('divActive', None)
        self.ID = dict.get('ID', None)
        return self

    def to_list(self):
        return [self.lgID, self.league, self.lgActive, self.divID, self.division, self.divActive, self.ID]

    def to_dict(self):
        return {
            'lgID': self.lgID,
            'league': self.league,
            'lgActive': self.lgActive,
            'divID': self.divID,
            'division': self.division,
            'divActive': self.divActive,
            'ID': self.ID
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
