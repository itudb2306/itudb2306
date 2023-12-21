class Record:
    def __init__(self, lgID: str = None, league: str = None, active: str = None, ID: int = None):
        self.lgID = lgID
        self.league = league
        self.active = active

    def from_list(self, list):
        self.lgID = list[0]
        self.league = list[1]
        self.active = list[2]
        return self
    
    def from_dict(self, dict):
        self.lgID = dict['lgID']
        self.league = dict['league']
        self.active = dict['active']
        return self
    
    def to_list(self):
        return [self.lgID, self.league, self.active]
    
    def to_dict(self):
        return {
            'lgID': self.lgID,
            'league': self.league,
            'active': self.active
        }
    
class Records: 
    def __init__(self):
        self.records = []
    
    def from_list(self, list):
        for row in list:
            self.records.append(Record().from_list(row))
        return self
    
    def from_dict(self, dict):
        for row in dict:
            self.records.append(Record().from_dict(row))
        return self

    def to_list(self):
        list = []
        for row in self.records:
            list.append(row.to_list())
        return list
    
    def to_dict(self):
        dict = []
        for row in self.records:
            dict.append(row.to_dict())
        return dict
    
