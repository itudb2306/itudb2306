class FilterForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.G in empty and self.AB in empty and self.R in empty and self.H in empty and self.HR in empty and self.RBI in empty and self.ID in empty
    
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
        self.G = dict.get('filterG', None)
        if self.G == "":
            self.G = None
        self.AB = dict.get('filterAB', None)
        if self.AB == "":
            self.AB = None
        self.R = dict.get('filterR', None)
        if self.R == "":
            self.R = None
        self.H = dict.get('filterH', None)
        if self.H == "":
            self.H = None
        self.HR = dict.get('filterHR', None)
        if self.HR == "":
            self.HR = None
        self.RBI = dict.get('filterRBI', None)
        if self.RBI == "":
            self.RBI = None
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
            'filterG': self.G,
            'filterAB': self.AB,
            'filterR': self.R,
            'filterH': self.H,
            'filterHR': self.HR,
            'filterRBI': self.RBI,
            'filterID': self.ID
        }

        filter_dict = {k: v for k, v in filter_dict.items() if v is not None and v != 'None'}
        return filter_dict

    def to_and_string(self):
        and_string = ""
        if self.FirstName is not None and self.FirstName != 'None':
            and_string += f"p.nameFirst LIKE '%{self.FirstName}%' AND "

        if self.LastName is not None and self.LastName != 'None':
            and_string += f"p.nameLast LIKE '%{self.LastName}%' AND "

        if self.TeamName is not None and self.TeamName != 'None':
            and_string += f"t.name LIKE '%{self.TeamName}%' AND "

        if self.yearID is not None and self.yearID != 'None':
            and_string += f"b.yearID = {self.yearID} AND "

        if self.stint is not None and self.stint != 'None':
            and_string += f"b.stint = {self.stint} AND "

        if self.LeagueName is not None and self.LeagueName != 'None':
            and_string += f"l.league LIKE '%{self.LeagueName}%' AND "

        if self.G is not None and self.G != 'None':
            and_string += f"b.G = {self.G} AND "

        if self.AB is not None and self.AB != 'None':
            and_string += f"b.AB = {self.AB} AND "

        if self.R is not None and self.R != 'None':
            and_string += f"b.R = {self.R} AND "

        if self.H is not None and self.H != 'None':
            and_string += f"b.H = {self.H} AND "

        if self.HR is not None and self.HR != 'None':
            and_string += f"b.HR = {self.HR} AND "

        if self.RBI is not None and self.RBI != 'None':
            and_string += f"b.RBI = {self.RBI} AND "

        if self.ID is not None and self.ID != 'None':
            and_string += f"b.ID = {self.ID} AND "

        if and_string != "":
            and_string = and_string[:-5]

        return and_string

class SortForm:
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

    def is_empty(self):
        empty = [None, '', 'None']
        return self.FirstName in empty and self.LastName in empty and self.TeamName in empty and self.yearID in empty and self.stint in empty and self.LeagueName in empty and self.G in empty and self.AB in empty and self.R in empty and self.H in empty and self.HR in empty and self.RBI in empty and self.ID in empty
    
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
        self.G = dict.get('sortG', None)
        if self.G not in options:
            self.G = None
        self.AB = dict.get('sortAB', None)
        if self.AB not in options:
            self.AB = None
        self.R = dict.get('sortR', None)
        if self.R not in options:
            self.R = None
        self.H = dict.get('sortH', None)
        if self.H not in options:
            self.H = None
        self.HR = dict.get('sortHR', None)
        if self.HR not in options:
            self.HR = None
        self.RBI = dict.get('sortRBI', None)
        if self.RBI not in options:
            self.RBI = None
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
            'sortG': self.G,
            'sortAB': self.AB,
            'sortR': self.R,
            'sortH': self.H,
            'sortHR': self.HR,
            'sortRBI': self.RBI,
            'sortID': self.ID
        }

        sort_dict = {k: v for k, v in sort_dict.items() if v is not None and v != 'None'}
        return sort_dict
    
    def to_and_string(self):
        sort_string = ""
        if self.FirstName is not None and self.FirstName != 'None':
            sort_string += "p.nameFirst {} , ".format(self.FirstName)
        
        if self.LastName is not None and self.LastName != 'None':
            sort_string += "p.nameLast {} , ".format(self.LastName)
        
        if self.TeamName is not None and self.TeamName != 'None':
            sort_string += "t.name {} , ".format(self.TeamName)
        
        if self.yearID is not None and self.yearID != 'None':
            sort_string += "b.yearID {} , ".format(self.yearID)
        
        if self.stint is not None and self.stint != 'None':
            sort_string += "b.stint {} , ".format(self.stint)
        
        if self.LeagueName is not None and self.LeagueName != 'None':
            sort_string += "l.league {} , ".format(self.LeagueName)

        if self.G is not None and self.G != 'None':
            sort_string += "b.G {} , ".format(self.G)

        if self.AB is not None and self.AB != 'None':
            sort_string += "b.AB {} , ".format(self.AB)

        if self.R is not None and self.R != 'None':
            sort_string += "b.R {} , ".format(self.R)

        if self.H is not None and self.H != 'None':
            sort_string += "b.H {} , ".format(self.H)

        if self.HR is not None and self.HR != 'None':
            sort_string += "b.HR {} , ".format(self.HR)
        
        if self.RBI is not None and self.RBI != 'None':
            sort_string += "b.RBI {} , ".format(self.RBI)
        
        if self.ID is not None and self.ID != 'None':
            sort_string += "b.ID {} , ".format(self.ID)
        
        if sort_string != "":
            sort_string = sort_string[:-2]
        
        return sort_string