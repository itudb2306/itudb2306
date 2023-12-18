class Record:
    def __init__(self, FirstName: str = None, LastName: str = None, TeamName: str = None, yearID: int = None, stint: int = None, LeagueName: str = None, POS: str = None, G: int = None, GS: int = None, InnOuts: int = None, PO: int = None, A: int = None, E: int = None, DP: int = None, ID: int = None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TeamName = TeamName
        self.yearID = yearID
        self.stint = stint
        self.LeagueName = LeagueName
        self.POS = POS
        self.G = G
        self.GS = GS
        self.InnOuts = InnOuts
        self.PO = PO
        self.A = A
        self.E = E
        self.DP = DP
        self.ID = ID

    def from_list(self, list):
        self.FirstName = list[0]
        self.LastName = list[1]
        self.TeamName = list[2]
        self.yearID = list[3]
        self.stint = list[4]
        self.LeagueName = list[5]
        self.POS = list[6]
        self.G = list[7]
        self.GS = list[8]
        self.InnOuts = list[9]
        self.PO = list[10]
        self.A = list[11]
        self.E = list[12]
        self.DP = list[13]
        self.ID = list[14]
        return self

    def from_dict(self, dict):
        self.FirstName = dict['FirstName']
        self.LastName = dict['LastName']
        self.TeamName = dict['TeamName']
        self.yearID = dict['yearID']
        self.stint = dict['stint']
        self.LeagueName = dict['LeagueName']
        self.POS = dict['POS']
        self.G = dict['G']
        self.GS = dict['GS']
        self.InnOuts = dict['InnOuts']
        self.PO = dict['PO']
        self.A = dict['A']
        self.E = dict['E']
        self.DP = dict['DP']
        self.ID = dict['ID']
        return self
    
    def to_list(self):
        return [self.FirstName, self.LastName, self.TeamName, self.yearID, self.stint, self.LeagueName, self.POS, self.G, self.GS, self.InnOuts, self.PO, self.A, self.E, self.DP, self.ID]
    
    def to_dict(self):
        return {
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'TeamName': self.TeamName,
            'yearID': self.yearID,
            'stint': self.stint,
            'LeagueName': self.LeagueName,
            'POS': self.POS,
            'G': self.G,
            'GS': self.GS,
            'InnOuts': self.InnOuts,
            'PO': self.PO,
            'A': self.A,
            'E': self.E,
            'DP': self.DP,
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