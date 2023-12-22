class NameUpdateForm:
    def __init__(self, ID: int = None, name: str = None):
        self.ID = ID
        self.name = name

    # Request args from form
    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.name = dict.get('name', None)
        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        empty = [None, '', 'None']
        tupl = ()

        if self.ID not in empty:
            tupl += (self.ID,)

        if self.name not in empty:
            tupl += (self.name,)

        return tupl


class NameFilterForm:
    def __init__(self, name: str = None, countUL: int = None, countLL: int = None):
        self.name = name
        self.countUL = countUL
        self.countLL = countLL

    def is_empty(self):
        empty = [None, '', 'None']
        return self.name in empty and self.countUL in empty and self.countLL in empty

    def from_dict(self, dict):
        empty = [None, '', 'None']

        self.name = dict.get('filterName', None)
        if self.name in empty:
            self.name = None

        self.countUL = dict.get('filterCountUL', None)
        if self.countUL in empty:
            self.countUL = None

        self.countLL = dict.get('filterCountLL', None)
        if self.countLL in empty:
            self.countLL = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        fitler_dict = {
            'filterName': self.name,
            'filterCountUL': self.countUL,
            'filterCountLL': self.countLL,
        }
        # Don't return empty values
        fitler_dict = {key: value for key,
                       value in fitler_dict.items() if value not in empty}
        return fitler_dict

    def to_and_string(self):
        empty = [None, '', 'None']
        and_string = ""

        if self.name not in empty:
            and_string += " AND name LIKE '%{}%'".format(self.name)

        if self.countUL not in empty:
            and_string += " AND cnt <= {}".format(self.countUL)

        if self.countLL not in empty:
            and_string += " AND cnt >= {}".format(self.countLL)

        # Remove the first " AND " string
        if and_string != "":
            and_string = and_string[5:]

        return and_string


class NameSortForm:
    def __init__(self, name: str = None, count: str = None):
        self.name = name
        self.count = count

    def is_empty(self):
        empty = [None, '', 'None']
        return self.name in empty and self.count in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']

        self.name = dict.get('sortName', None)
        if self.name not in options:
            self.name = None

        self.count = dict.get('sortCount', None)
        if self.count not in options:
            self.count = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        sort_dict = {
            'sortName': self.name,
            'sortCount': self.count,
        }
        # Don't return empty values
        sort_dict = {key: value for key,
                     value in sort_dict.items() if value not in empty}
        return sort_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.name not in empty:
            and_string += "name {}, ".format(self.name)

        if self.count not in empty:
            and_string += "cnt {}, ".format(self.count)

        # Remove the last ", " string
        if and_string != "":
            and_string = and_string[:-2]

        return and_string


class NameAddForm:
    def __init__(self, name: str = None):
        self.ID = None
        self.name = name

    # Request args from form
    def from_dict(self, dict):
        self.name = dict.get('name', None)
        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        empty = [None, '', 'None']
        tupl = ()

        if self.name not in empty:
            tupl += (self.name,)

        return tupl
