class Record:
    def __init__(self, FirstName: str = None, LastName: str = None, TeamName: str = None, yearID: int = None, stint: int = None, LeagueName: str = None, W: int = None, L: int = None, G: int = None, GS: int = None, CG: int = None, SHO: int = None, SV: int = None, IPouts: int = None, ID: int = None):
            self.FirstName = FirstName
            self.LastName = LastName
            self.TeamName = TeamName
            self.yearID = yearID
            self.stint = stint
            self.LeagueName = LeagueName
            self.W = W
            self.L = L
            self.G = G
            self.GS = GS
            self.CG = CG
            self.SHO = SHO
            self.SV = SV
            self.IPouts = IPouts
            self.ID = ID

    def from_list(self, list):
        self.FirstName = list[0]
        self.LastName = list[1]
        self.TeamName = list[2]
        self.yearID = list[3]
        self.stint = list[4]
        self.LeagueName = list[5]
        self.W = list[6]
        self.L = list[7]
        self.G = list[8]
        self.GS = list[9]
        self.CG = list[10]
        self.SHO = list[11]
        self.SV = list[12]
        self.IPouts = list[13]
        self.ID = list[14]
        return self

    def from_dict(self, dict):
        self.FirstName = dict['FirstName']
        self.LastName = dict['LastName']
        self.TeamName = dict['TeamName']
        self.yearID = dict['yearID']
        self.stint = dict['stint']
        self.LeagueName = dict['LeagueName']
        self.W = dict['W']
        self.L = dict['L']
        self.G = dict['G']
        self.GS = dict['GS']
        self.CG = dict['CG']
        self.SHO = dict['SHO']
        self.SV = dict['SV']
        self.IPouts = dict['IPouts']
        self.ID = dict['ID']
        return self
    
    def to_list(self):
        return [self.FirstName, self.LastName, self.TeamName, self.yearID, self.stint, self.LeagueName, self.W, self.L, self.G, self.GS, self.CG, self.SHO, self.SV, self.IPouts, self.ID]
    
    def to_dict(self):
        return {
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'TeamName': self.TeamName,
            'yearID': self.yearID,
            'stint': self.stint,
            'LeagueName': self.LeagueName,
            'W': self.W,
            'L': self.L,
            'G': self.G,
            'GS': self.GS,
            'CG': self.CG,
            'SHO': self.SHO,
            'SV': self.SV,
            'IPouts': self.IPouts,
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
       