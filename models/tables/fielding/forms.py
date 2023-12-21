class FilterForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.POS in empty and self.G in empty and self.GS in empty and self.InnOuts in empty and self.PO in empty and self.A in empty and self.E in empty and self.DP in empty and self.ID in empty
    
    def from_dict(self, dict):
        self.FirstName = dict.get('filterFirstName', None)
        if self.FirstName == "":
            self.FirstName = None
        self.LastName = dict.get('filterLastName', None)
        if self.LastName == "":
            self.LastName = None
        self.TeamName = dict.get('filterTeamName', None)
        if self.TeamName == "":
            self.TeamName = None
        self.yearID = dict.get('filterYearID', None)
        if self.yearID == "":
            self.yearID = None
        self.stint = dict.get('filterStint', None)
        if self.stint == "":
            self.stint = None
        self.LeagueName = dict.get('filterLeagueName', None)
        if self.LeagueName == "":
            self.LeagueName = None
        self.POS = dict.get('filterPOS', None)
        if self.POS == "":
            self.POS = None
        self.G = dict.get('filterG', None)
        if self.G == "":
            self.G = None
        self.GS = dict.get('filterGS', None)
        if self.GS == "":
            self.GS = None
        self.InnOuts = dict.get('filterInnOuts', None)
        if self.InnOuts == "":
            self.InnOuts = None
        self.PO = dict.get('filterPO', None)
        if self.PO == "":
            self.PO = None
        self.A = dict.get('filterA', None)
        if self.A == "":
            self.A = None
        self.E = dict.get('filterE', None)
        if self.E == "":
            self.E = None
        self.DP = dict.get('filterDP', None)
        if self.DP == "":
            self.DP = None
        self.ID = dict.get('filterID', None)
        if self.ID == "":
            self.ID = None

        return self
    
    def to_dict(self):
        filter_dict =  {
            'filterFirstName': self.FirstName,
            'filterLastName': self.LastName,
            'filterTeamName': self.TeamName,
            'filterYearID': self.yearID,
            'filterStint': self.stint,
            'filterLeagueName': self.LeagueName,
            'filterPOS': self.POS,
            'filterG': self.G,
            'filterGS': self.GS,
            'filterInnOuts': self.InnOuts,
            'filterPO': self.PO,
            'filterA': self.A,
            'filterE': self.E,
            'filterDP': self.DP,
            'filterID': self.ID
        }

        filter_dict = {k: v for k, v in filter_dict.items() if v != '' and v is not None and v != 'None'}
        return filter_dict
    
    def to_and_string(self):
        and_string = ""

        if self.FirstName is not None and self.FirstName != '':
            and_string += f"p.nameFirst LIKE '%{self.FirstName}%' AND "
        
        if self.LastName is not None and self.LastName != '':
            and_string += f"p.nameLast LIKE '%{self.LastName}%' AND "
        
        if self.TeamName is not None and self.TeamName != '':
            and_string += f"t.name LIKE '%{self.TeamName}%' AND "
        
        if self.yearID is not None and self.yearID != '':
            and_string += f"f.yearID = {self.yearID} AND "
        
        if self.stint is not None and self.stint != '':
            and_string += f"f.stint = {self.stint} AND "
        
        if self.LeagueName is not None and self.LeagueName != '':
            and_string += f"l.league LIKE '%{self.LeagueName}%' AND "
        
        if self.POS is not None and self.POS != '':
            and_string += f"f.POS LIKE '%{self.POS}%' AND "
        
        if self.G is not None and self.G != '':
            and_string += f"f.G = {self.G} AND "
        
        if self.GS is not None and self.GS != '':
            and_string += f"f.GS = {self.GS} AND "
        
        if self.InnOuts is not None and self.InnOuts != '':
            and_string += f"f.InnOuts = {self.InnOuts} AND "
        
        if self.PO is not None and self.PO != '':
            and_string += f"f.PO = {self.PO} AND "

        if self.A is not None and self.A != '':
            and_string += f"f.A = {self.A} AND "

        if self.E is not None and self.E != '':
            and_string += f"f.E = {self.E} AND "
        
        if self.DP is not None and self.DP != '':
            and_string += f"f.DP = {self.DP} AND "
        
        if self.ID is not None and self.ID != '':
            and_string += f"f.ID = {self.ID} AND "
        
        if and_string != "":
            and_string = and_string[:-5]
        
        return and_string
    
class SortForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.POS in empty and self.G in empty and self.GS in empty and self.InnOuts in empty and self.PO in empty and self.A in empty and self.E in empty and self.DP in empty and self.ID in empty
    
    def from_dict(self, dict):
        options = ['ASC', 'DESC']
        self.FirstName = dict.get('sortFirstName', None)
        if self.FirstName not in options:
            self.FirstName = None
        self.LastName = dict.get('sortLastName', None)
        if self.LastName not in options:
            self.LastName = None
        self.TeamName = dict.get('sortTeamName', None)
        if self.TeamName not in options:
            self.TeamName = None
        self.yearID = dict.get('sortYearID', None)
        if self.yearID not in options:
            self.yearID = None
        self.stint = dict.get('sortStint', None)
        if self.stint not in options:
            self.stint = None
        self.LeagueName = dict.get('sortLeagueName', None)
        if self.LeagueName not in options:
            self.LeagueName = None
        self.POS = dict.get('sortPOS', None)
        if self.POS not in options:
            self.POS = None
        self.G = dict.get('sortG', None)
        if self.G not in options:
            self.G = None
        self.GS = dict.get('sortGS', None)
        if self.GS not in options:
            self.GS = None
        self.InnOuts = dict.get('sortInnOuts', None)
        if self.InnOuts not in options:
            self.InnOuts = None
        self.PO = dict.get('sortPO', None)
        if self.PO not in options:
            self.PO = None
        self.A = dict.get('sortA', None)
        if self.A not in options:
            self.A = None
        self.E = dict.get('sortE', None)
        if self.E not in options:
            self.E = None
        self.DP = dict.get('sortDP', None)
        if self.DP not in options:
            self.DP = None
        self.ID = dict.get('sortID', None)
        if self.ID not in options:
            self.ID = None

        return self
    
    def to_dict(self):
        sort_dict =  {
            'sortFirstName': self.FirstName,
            'sortLastName': self.LastName,
            'sortTeamName': self.TeamName,
            'sortYearID': self.yearID,
            'sortStint': self.stint,
            'sortLeagueName': self.LeagueName,
            'sortPOS': self.POS,
            'sortG': self.G,
            'sortGS': self.GS,
            'sortInnOuts': self.InnOuts,
            'sortPO': self.PO,
            'sortA': self.A,
            'sortE': self.E,
            'sortDP': self.DP,
            'sortID': self.ID
        }

        sort_dict = {k: v for k, v in sort_dict.items() if v != '' and v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""

        if self.FirstName is not None and self.FirstName != "":
            sort_string += "p.nameFirst {}, ".format(self.FirstName)
        if self.LastName is not None and self.LastName != "":
            sort_string += "p.nameLast {}, ".format(self.LastName)
        if self.TeamName is not None and self.TeamName != "":
            sort_string += "t.name {}, ".format(self.TeamName)
        if self.yearID is not None and self.yearID != "":
            sort_string += "f.yearID {}, ".format(self.yearID)
        if self.stint is not None and self.stint != "":
            sort_string += "f.stint {}, ".format(self.stint)
        if self.LeagueName is not None and self.LeagueName != "":
            sort_string += "l.league {}, ".format(self.LeagueName)
        if self.POS is not None and self.POS != "":
            sort_string += "f.POS {}, ".format(self.POS)
        if self.G is not None and self.G != "":
            sort_string += "f.G {}, ".format(self.G)
        if self.GS is not None and self.GS != "":
            sort_string += "f.GS {}, ".format(self.GS)
        if self.InnOuts is not None and self.InnOuts != "":
            sort_string += "f.InnOuts {}, ".format(self.InnOuts)
        if self.PO is not None and self.PO != "":
            sort_string += "f.PO {}, ".format(self.PO)
        if self.A is not None and self.A != "":
            sort_string += "f.A {}, ".format(self.A)
        if self.E is not None and self.E != "":
            sort_string += "f.E {}, ".format(self.E)
        if self.DP is not None and self.DP != "":
            sort_string += "f.DP {}, ".format(self.DP)
        if self.ID is not None and self.ID != "":
            sort_string += "f.ID {}, ".format(self.ID)
        
        if sort_string != "":
            sort_string = sort_string[:-2]
        
        return sort_string
        
            