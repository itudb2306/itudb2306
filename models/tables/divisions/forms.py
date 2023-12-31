class UpdateForm:
    def __init__(self, ID: int = None, divID: str = None, lgID: str = None,
                 division: str = None, active: str = None):
        self.ID = ID
        self.divID = divID
        self.lgID = lgID
        self.division = division
        self.active = active

    # Request args from form
    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.divID = dict.get('divID', None)
        if self.divID == "":
            self.divID = None

        self.lgID = dict.get('lgID', None)
        if self.lgID == "":
            self.lgID = None

        self.division = dict.get('division', None)
        if self.division == "":
            self.division = None

        self.active = dict.get('active', None)
        if self.active == "":
            self.active = None

        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        tupl = ()
        empty = [None, '', 'None']

        if self.ID not in empty:
            tupl += (self.ID,)

        if self.divID not in empty:
            tupl += (self.divID,)

        if self.lgID not in empty:
            tupl += (self.lgID,)

        if self.division not in empty:
            tupl += (self.division,)

        if self.active not in empty:
            tupl += (self.active,)

        return tupl


class FilterForm:
    def __init__(self, lgID: str = None, league: str = None, lgActive: str = None, divID: str = None, division: str = None, divActive: str = None):
        self.lgID = lgID
        self.league = league
        self.lgActive = lgActive
        self.divID = divID
        self.division = division
        self.divActive = divActive

    def is_empty(self):
        empty = [None, '', 'None']
        return self.lgID in empty and self.league in empty and self.lgActive in empty and self.divID in empty and self.division in empty and self.divActive in empty

    def from_dict(self, dict):
        empty = [None, '', 'None']

        self.lgID = dict.get('filterLgID', None)
        if self.lgID in empty:
            self.lgID = None

        self.league = dict.get('filterLeague', None)
        if self.league in empty:
            self.league = None

        self.lgActive = dict.get('filterLgActive', None)
        if self.lgActive in empty:
            self.lgActive = None

        self.divID = dict.get('filterDivID', None)
        if self.divID in empty:
            self.divID = None

        self.division = dict.get('filterDivision', None)
        if self.division in empty:
            self.division = None

        self.divActive = dict.get('filterDivActive', None)
        if self.divActive in empty:
            self.divActive = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        fitler_dict = {
            'filterLgID': self.lgID,
            'filterLeague': self.league,
            'filterLgActive': self.lgActive,
            'filterDivID': self.divID,
            'filterDivision': self.division,
            'filterDivActive': self.divActive
        }
        # Don't return empty values
        fitler_dict = {key: value for key,
                       value in fitler_dict.items() if value not in empty}
        return fitler_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.lgID not in empty:
            and_string += " AND lgID LIKE '%{}%'".format(self.lgID)

        if self.league not in empty:
            and_string += " AND league LIKE '%{}%'".format(self.league)

        if self.lgActive not in empty:
            and_string += " AND lgActive LIKE '%{}%'".format(self.lgActive)

        if self.divID not in empty:
            and_string += " AND divID LIKE '%{}%'".format(self.divID)

        if self.division not in empty:
            and_string += " AND division LIKE '%{}%'".format(self.division)

        if self.divActive not in empty:
            and_string += " AND divActive LIKE '%{}%'".format(self.divActive)

        # Remove the first " AND " string
        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, lgID: str = None, league: str = None, lgActive: str = None, divID: str = None, division: str = None, divActive: str = None):
        self.lgID = lgID
        self.league = league
        self.lgActive = lgActive
        self.divID = divID
        self.division = division
        self.divActive = divActive

    def is_empty(self):
        empty = [None, '', 'None']
        return self.lgID in empty and self.league in empty and self.lgActive in empty and self.divID in empty and self.division in empty and self.divActive in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']

        self.lgID = dict.get('sortLgID', None)
        if self.lgID not in options:
            self.lgID = None

        self.league = dict.get('sortLeague', None)
        if self.league not in options:
            self.league = None

        self.lgActive = dict.get('sortLgActive', None)
        if self.lgActive not in options:
            self.lgActive = None

        self.divID = dict.get('sortDivID', None)
        if self.divID not in options:
            self.divID = None

        self.division = dict.get('sortDivision', None)
        if self.division not in options:
            self.division = None

        self.divActive = dict.get('sortDivActive', None)
        if self.divActive not in options:
            self.divActive = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        sort_dict = {
            'sortLgID': self.lgID,
            'sortLeague': self.league,
            'sortLgActive': self.lgActive,
            'sortDivID': self.divID,
            'sortDivision': self.division,
            'sortDivActive': self.divActive
        }
        # Don't return empty values
        sort_dict = {key: value for key,
                     value in sort_dict.items() if value not in empty}
        return sort_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.lgID not in empty:
            and_string += "lgID {}, ".format(self.lgID)

        if self.league not in empty:
            and_string += "league {}, ".format(self.league)

        if self.lgActive not in empty:
            and_string += "lgActive {}, ".format(self.lgActive)

        if self.divID not in empty:
            and_string += "divID {}, ".format(self.divID)

        if self.division not in empty:
            and_string += "division {}, ".format(self.division)

        if self.divActive not in empty:
            and_string += "divActive {}, ".format(self.divActive)

        # Remove the last ", " string
        if and_string != "":
            and_string = and_string[:-2]

        return and_string


class AddForm:
    def __init__(self, divID: str = None, lgID: str = None,
                 division: str = None, active: str = None):
        self.ID = None
        self.divID = divID
        self.lgID = lgID
        self.division = division
        self.active = active

    # Request args from form
    def from_dict(self, dict):
        self.divID = dict.get('divID', None)
        if self.divID == "":
            self.divID = None

        self.lgID = dict.get('lgID', None)
        if self.lgID == "":
            self.lgID = None

        self.division = dict.get('division', None)
        if self.division == "":
            self.division = None

        self.active = dict.get('active', None)
        if self.active == "":
            self.active = None

        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        tupl = ()
        empty = [None, '', 'None']

        if self.divID not in empty:
            tupl += (self.divID,)

        if self.lgID not in empty:
            tupl += (self.lgID,)

        if self.division not in empty:
            tupl += (self.division,)

        if self.active not in empty:
            tupl += (self.active,)

        return tupl
