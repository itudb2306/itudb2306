class FilterForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.W in empty and self.L in empty and self.G in empty and self.GS in empty and self.CG in empty and self.SHO in empty and self.SV in empty and self.IPouts in empty and self.ID in empty
    
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
        self.W = dict.get('filterW', None)
        if self.W == "":
            self.W = None
        self.L = dict.get('filterL', None)
        if self.L == "":
            self.L = None
        self.G = dict.get('filterG', None)
        if self.G == "":
            self.G = None
        self.GS = dict.get('filterGS', None)
        if self.GS == "":
            self.GS = None
        self.CG = dict.get('filterCG', None)
        if self.CG == "":
            self.CG = None
        self.SHO = dict.get('filterSHO', None)
        if self.SHO == "":
            self.SHO = None
        self.SV = dict.get('filterSV', None)
        if self.SV == "":
            self.SV = None
        self.IPouts = dict.get('filterIPouts', None)
        if self.IPouts == "":
            self.IPouts = None
        self.ID = dict.get('filterID', None)
        if self.ID == "":
            self.ID = None
        return self

    def to_dict(self):
        filter_dict = {
            'filterFirstName': self.FirstName,
            'filterLastName': self.LastName,
            'filterTeamName': self.TeamName,
            'filterYearID': self.yearID,
            'filterStint': self.stint,
            'filterLeagueName': self.LeagueName,
            'filterW': self.W,
            'filterL': self.L,
            'filterG': self.G,
            'filterGS': self.GS,
            'filterCG': self.CG,
            'filterSHO': self.SHO,
            'filterSV': self.SV,
            'filterIPouts': self.IPouts,
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
            and_string += f"pitching.yearID = {self.yearID} AND "
        if self.stint is not None and self.stint != '':
            and_string += f"pitching.stint = {self.stint} AND "
        if self.LeagueName is not None and self.LeagueName != '':
            and_string += f"l.name LIKE '%{self.LeagueName}%' AND "
        if self.W is not None and self.W != '':
            and_string += f"pitching.W = {self.W} AND "
        if self.L is not None and self.L != '':
            and_string += f"pitching.L = {self.L} AND "
        if self.G is not None and self.G != '':
            and_string += f"pitching.G = {self.G} AND "
        if self.GS is not None and self.GS != '':
            and_string += f"pitching.GS = {self.GS} AND "
        if self.CG is not None and self.CG != '':
            and_string += f"pitching.CG = {self.CG} AND "
        if self.SHO is not None and self.SHO != '':
            and_string += f"pitching.SHO = {self.SHO} AND "
        if self.SV is not None and self.SV != '':
            and_string += f"pitching.SV = {self.SV} AND "
        if self.IPouts is not None and self.IPouts != '':
            and_string += f"pitching.IPouts = {self.IPouts} AND "
        if self.ID is not None and self.ID != '':
            and_string += f"pitching.ID = {self.ID} AND "
        if and_string != "":
            and_string = and_string[:-5]
        return and_string
    
class SortForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.W in empty and self.L in empty and self.G in empty and self.GS in empty and self.CG in empty and self.SHO in empty and self.SV in empty and self.IPouts in empty and self.ID in empty
    
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
        self.W = dict.get('sortW', None)
        if self.W not in options:
            self.W = None
        self.L = dict.get('sortL', None)
        if self.L not in options:
            self.L = None
        self.G = dict.get('sortG', None)
        if self.G not in options:
            self.G = None
        self.GS = dict.get('sortGS', None)
        if self.GS not in options:
            self.GS = None
        self.CG = dict.get('sortCG', None)
        if self.CG not in options:
            self.CG = None
        self.SHO = dict.get('sortSHO', None)
        if self.SHO not in options:
            self.SHO = None
        self.SV = dict.get('sortSV', None)
        if self.SV not in options:
            self.SV = None
        self.IPouts = dict.get('sortIPouts', None)
        if self.IPouts not in options:
            self.IPouts = None
        self.ID = dict.get('sortID', None)
        if self.ID not in options:
            self.ID = None
        return self
    
    def to_dict(self):
        sort_dict = {
            'sortFirstName': self.FirstName,
            'sortLastName': self.LastName,
            'sortTeamName': self.TeamName,
            'sortYearID': self.yearID,
            'sortStint': self.stint,
            'sortLeagueName': self.LeagueName,
            'sortW': self.W,
            'sortL': self.L,
            'sortG': self.G,
            'sortGS': self.GS,
            'sortCG': self.CG,
            'sortSHO': self.SHO,
            'sortSV': self.SV,
            'sortIPouts': self.IPouts,
            'sortID': self.ID
        }

        sort_dict = {k: v for k, v in sort_dict.items() if v != '' and v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""

        if self.FirstName is not None and self.FirstName != '':
            sort_string += f"p.nameFirst {self.FirstName}, "
        if self.LastName is not None and self.LastName != '':
            sort_string += f"p.nameLast {self.LastName}, "
        if self.TeamName is not None and self.TeamName != '':
            sort_string += f"t.name {self.TeamName}, "
        if self.yearID is not None and self.yearID != '':
            sort_string += f"pitching.yearID {self.yearID}, "
        if self.stint is not None and self.stint != '':
            sort_string += f"pitching.stint {self.stint}, "
        if self.LeagueName is not None and self.LeagueName != '':
            sort_string += f"l.name {self.LeagueName}, "
        if self.W is not None and self.W != '':
            sort_string += f"pitching.W {self.W}, "
        if self.L is not None and self.L != '':
            sort_string += f"pitching.L {self.L}, "
        if self.G is not None and self.G != '':
            sort_string += f"pitching.G {self.G}, "
        if self.GS is not None and self.GS != '':
            sort_string += f"pitching.GS {self.GS}, "
        if self.CG is not None and self.CG != '':
            sort_string += f"pitching.CG {self.CG}, "
        if self.SHO is not None and self.SHO != '':
            sort_string += f"pitching.SHO {self.SHO}, "
        if self.SV is not None and self.SV != '':
            sort_string += f"pitching.SV {self.SV}, "
        if self.IPouts is not None and self.IPouts != '':
            sort_string += f"pitching.IPouts {self.IPouts}, "
        if self.ID is not None and self.ID != '':
            sort_string += f"pitching.ID {self.ID}, "
        if sort_string != "":
            sort_string = sort_string[:-2]
        return sort_string
    