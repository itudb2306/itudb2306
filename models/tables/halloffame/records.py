

# ID, yearID, votedBy, ballots, needed, votes, inducted, category, nameFirst, nameLast,
class Record:
    def __init__(self, ID = None, year_id = None, voted_by = None, ballots = None, needed = None, votes = None, inducted = None, category = None, nameFirst = None, nameLast = None):
        self.ID = ID
        self.year_id = year_id
        self.voted_by = voted_by
        self.ballots = ballots
        self.needed = needed
        self.votes = votes
        self.inducted = inducted
        self.category = category
        self.nameFirst = nameFirst
        self.nameLast = nameLast


    # record.player_id -> record['player_id']
    # No need for this, since we can use record.player_id in jinja2 templates
    #def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.ID = list[0]
        self.year_id = list[1]
        self.voted_by = list[2]
        self.ballots = list[3]
        self.needed = list[4]
        self.votes = list[5]
        self.inducted = list[6]
        self.category = list[7]
        self.nameFirst = list[8]
        self.nameLast = list[9]
        return self
        

    def from_dict(self, dict):
        self.ID = dict['ID']
        self.year_id = dict['yearID']
        self.voted_by = dict['votedBy']
        self.ballots = dict['ballots']
        self.needed = dict['needed']
        self.votes = dict['votes']
        self.inducted = dict['inducted']
        self.category = dict['category']
        self.nameFirst = dict['nameFirst']
        self.nameLast = dict['nameLast']
        return self

    def to_list(self):
        return [
            self.ID,
            self.nameFirst,
            self.nameLast,
            self.year_id,
            self.voted_by,
            self.ballots,
            self.needed,
            self.votes,
            self.inducted,
            self.category
        ]

    def to_dict(self):
        return {
            'ID': self.ID,
            'nameFirst': self.nameFirst,
            'nameLast': self.nameLast,
            'yearID': self.year_id,
            'votedBy': self.voted_by,
            'ballots': self.ballots,
            'needed': self.needed,
            'votes': self.votes,
            'inducted': self.inducted,
            'category': self.category
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
    


