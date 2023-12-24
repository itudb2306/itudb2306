

# ID, nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
class Record:
    def __init__(self, ID = None, nameFirst = None, nameLast = None, year_id = None, name = None, league = None, inseason = None, G = None, W = None, L = None, teamRank = None, plyrMgr = None):
        self.ID = ID
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.year_id = year_id
        self.name = name
        self.league = league
        self.inseason = inseason
        self.G = G
        self.W = W
        self.L = L
        self.teamRank = teamRank
        self.plyrMgr = plyrMgr


    # record.player_id -> record['player_id']
    # No need for this, since we can use record.player_id in jinja2 templates
    #def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.ID = list[0]
        self.nameFirst = list[1]
        self.nameLast = list[2]
        self.year_id = list[3]
        self.name = list[4]
        self.league = list[5]
        self.inseason = list[6]
        self.G = list[7]
        self.W = list[8]
        self.L = list[9]
        # self.teamRank = list[10]
        self.plyrMgr = list[10]
        return self
        

    def from_dict(self, dict):
        self.ID = dict['ID']
        self.nameFirst = dict['nameFirst']
        self.nameLast = dict['nameLast']
        self.year_id = dict['yearID']
        self.name = dict['name']
        self.league = dict['league']
        self.inseason = dict['inseason']
        self.G = dict['G']
        self.W = dict['W']
        self.L = dict['L']
        self.teamRank = dict['teamRank']
        self.plyrMgr = dict['plyrMgr']
        return self

    def to_list(self):
        return [
            self.ID,
            self.nameFirst,
            self.nameLast,
            self.year_id,
            self.name,
            self.league,
            self.inseason,
            self.G,
            self.W,
            self.L,
            self.teamRank,
            self.plyrMgr
        ]

    def to_dict(self):
        return {
            'ID': self.ID,
            'nameFirst': self.nameFirst,
            'nameLast': self.nameLast,
            'yearID': self.year_id,
            'name': self.name,
            'league': self.league,
            'inseason': self.inseason,
            'G': self.G,
            'W': self.W,
            'L': self.L,
            'teamRank': self.teamRank,
            'plyrMgr': self.plyrMgr
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
    


