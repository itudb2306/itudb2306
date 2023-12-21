class Record:
    def __init__(self, FirstName: str = None, LastName: str = None, TeamName: str = None, yearID: int = None, stint: int = None, LeagueName: str = None, G: int = None, AB: int = None, R: int = None, H: int = None, HR: int = None, RBI: int = None, ID: int = None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TeamName = TeamName
        self.yearID = yearID
        self.stint = stint
        self.LeagueName = LeagueName
        self.G = G
        self.AB = AB
        self.R = R
        self.H = H
        self.HR = HR
        self.RBI = RBI
        self.ID = ID

    def from_list(self, list):
        self.FirstName = list[0]
        self.LastName = list[1]
        self.TeamName = list[2]
        self.yearID = list[3]
        self.stint = list[4]
        self.LeagueName = list[5]
        self.G = list[6]
        self.AB = list[7]
        self.R = list[8]
        self.H = list[9]
        self.HR = list[10]
        self.RBI = list[11]
        self.ID = list[12]
        return self
    
    def from_dict(self, dict):
        self.FirstName = dict['FirstName']
        self.LastName = dict['LastName']
        self.TeamName = dict['TeamName']
        self.yearID = dict['yearID']
        self.stint = dict['stint']
        self.LeagueName = dict['LeagueName']
        self.G = dict['G']
        self.AB = dict['AB']
        self.R = dict['R']
        self.H = dict['H']
        self.HR = dict['HR']
        self.RBI = dict['RBI']
        self.ID = dict['ID']
        return self
    
    def to_list(self):
        return [self.FirstName, self.LastName, self.TeamName, self.yearID, self.stint, self.LeagueName, self.G, self.AB, self.R, self.H, self.HR, self.RBI, self.ID]
    
    def to_dict(self):
        return {
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'TeamName': self.TeamName,
            'yearID': self.yearID,
            'stint': self.stint,
            'LeagueName': self.LeagueName,
            'G': self.G,
            'AB': self.AB,
            'R': self.R,
            'H': self.H,
            'HR': self.HR,
            'RBI': self.RBI,
            'ID': self.ID
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