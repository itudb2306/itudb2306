class UpdateForm:
    def __init__(self, ID: int = None, parkalias: str = None, parkkey: str = None,
                 parkname: str = None, city: str = None, state: str = None, country: str = None):
        self.ID = ID
        self.parkalias = parkalias
        self.parkkey = parkkey
        self.parkname = parkname
        self.city = city
        self.state = state
        self.country = country

    # Request args from form
    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.parkalias = dict.get('parkalias', None)
        self.parkkey = dict.get('parkkey', None)
        self.parkname = dict.get('parkname', None)
        self.city = dict.get('city', None)
        self.state = dict.get('state', None)
        self.country = dict.get('country', None)

        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        tupl = ()

        if self.ID is not None and self.ID != '':
            tupl += (self.ID,)

        if self.parkalias is not None and self.parkalias != '':
            tupl += (self.parkalias,)

        if self.parkkey is not None and self.parkkey != '':
            tupl += (self.parkkey,)

        if self.parkname is not None and self.parkname != '':
            tupl += (self.parkname,)

        if self.city is not None and self.city != '':
            tupl += (self.city,)

        if self.state is not None and self.state != '':
            tupl += (self.state,)

        if self.country is not None and self.country != '':
            tupl += (self.country,)

        return tupl


class FilterForm:
    def __init__(self, parkalias: str = None, parkkey: str = None, parkname: str = None,
                 city: str = None, state: str = None, country: str = None):
        self.parkalias = parkalias
        self.parkkey = parkkey
        self.parkname = parkname
        self.city = city
        self.state = state
        self.country = country

    def is_empty(self):
        empty = [None, '', 'None']
        return self.parkalias in empty and self.parkkey in empty and self.parkname in empty and self.city in empty and self.state in empty and self.country in empty

    def from_dict(self, dict):
        self.parkalias = dict.get('filterParkAlias', None)
        if self.parkalias == "":
            self.parkalias = None

        self.parkkey = dict.get('filterParkKey', None)
        if self.parkkey == "":
            self.parkkey = None

        self.parkname = dict.get('filterParkName', None)
        if self.parkname == "":
            self.parkname = None

        self.city = dict.get('filterCity', None)
        if self.city == "":
            self.city = None

        self.state = dict.get('filterState', None)
        if self.state == "":
            self.state = None

        self.country = dict.get('filterCountry', None)
        if self.country == "":
            self.country = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        fitler_dict = {
            'filterParkAlias': self.parkalias,
            'filterParkKey': self.parkkey,
            'filterParkName': self.parkname,
            'filterCity': self.city,
            'filterState': self.state,
            'filterCountry': self.country
        }
        # Don't return empty values
        fitler_dict = {key: value for key,
                       value in fitler_dict.items() if value not in empty}
        return fitler_dict

    def to_and_string(self):
        and_string = ""

        if self.parkalias is not None and self.parkalias != "":
            and_string += " AND parkalias LIKE '%{}%'".format(self.parkalias)

        if self.parkkey is not None and self.parkkey != "":
            and_string += " AND parkkey LIKE '%{}%'".format(self.parkkey)

        if self.parkname is not None and self.parkname != "":
            and_string += " AND parkname LIKE '%{}%'".format(self.parkname)

        if self.city is not None and self.city != "":
            and_string += " AND city LIKE '%{}%'".format(self.city)

        if self.state is not None and self.state != "":
            and_string += " AND state LIKE '%{}%'".format(self.state)

        if self.country is not None and self.country != "":
            and_string += " AND country LIKE '%{}%'".format(self.country)

        # Remove the first " AND " string
        if and_string != "":
            and_string = and_string[5:]

        return and_string


class SortForm:
    def __init__(self, parkalias: str = None, parkkey: str = None, parkname: str = None,
                 city: str = None, state: str = None, country: str = None):
        self.parkalias = parkalias
        self.parkkey = parkkey
        self.parkname = parkname
        self.city = city
        self.state = state
        self.country = country

    def is_empty(self):
        empty = [None, '', 'None']
        return self.parkalias in empty and self.parkkey in empty and self.parkname in empty and self.city in empty and self.state in empty and self.country in empty

    def from_dict(self, dict):
        options = ['ASC', 'DESC']

        self.parkalias = dict.get('sortParkAlias', None)
        if self.parkalias not in options:
            self.parkalias = None

        self.parkkey = dict.get('sortParkKey', None)
        if self.parkkey not in options:
            self.parkkey = None

        self.parkname = dict.get('sortParkName', None)
        if self.parkname not in options:
            self.parkname = None

        self.city = dict.get('sortCity', None)
        if self.city not in options:
            self.city = None

        self.state = dict.get('sortState', None)
        if self.state not in options:
            self.state = None

        self.country = dict.get('sortCountry', None)
        if self.country not in options:
            self.country = None

        return self

    def to_dict(self):
        empty = [None, '', 'None']

        sort_dict = {
            'sortParkAlias': self.parkalias,
            'sortParkKey': self.parkkey,
            'sortParkName': self.parkname,
            'sortCity': self.city,
            'sortState': self.state,
            'sortCountry': self.country
        }
        # Don't return empty values
        sort_dict = {key: value for key,
                     value in sort_dict.items() if value not in empty}
        return sort_dict

    def to_and_string(self):
        and_string = ""
        empty = [None, '', 'None']

        if self.parkname not in empty:
            and_string += "parkname {}, ".format(self.parkname)

        if self.parkkey not in empty:
            and_string += "parkkey {}, ".format(self.parkkey)

        if self.parkalias not in empty:
            and_string += "parkalias {}, ".format(self.parkalias)

        if self.country not in empty:
            and_string += "country {}, ".format(self.country)

        if self.state not in empty:
            and_string += "state {}, ".format(self.state)

        if self.city not in empty:
            and_string += "city {}, ".format(self.city)

        # Remove the last ", " string
        if and_string != "":
            and_string = and_string[:-2]

        return and_string


class AddForm:
    def __init__(self, parkalias: str = None, parkkey: str = None,
                 parkname: str = None, city: str = None, state: str = None, country: str = None):
        # ID is not included because it is auto-incremented in the database
        self.ID = None
        self.parkalias = parkalias
        self.parkkey = parkkey
        self.parkname = parkname
        self.city = city
        self.state = state
        self.country = country

    def from_dict(self, dict):
        self.parkalias = dict.get('parkalias', None)
        self.parkkey = dict.get('parkkey', None)
        self.parkname = dict.get('parkname', None)
        self.city = dict.get('city', None)
        self.state = dict.get('state', None)
        self.country = dict.get('country', None)

        return self

    def to_dict(self):
        return self.__dict__

    def to_tuple(self):
        tupl = ()

        if self.parkalias is not None and self.parkalias != '':
            tupl += (self.parkalias,)

        if self.parkkey is not None and self.parkkey != '':
            tupl += (self.parkkey,)

        if self.parkname is not None and self.parkname != '':
            tupl += (self.parkname,)

        if self.city is not None and self.city != '':
            tupl += (self.city,)

        if self.state is not None and self.state != '':
            tupl += (self.state,)

        if self.country is not None and self.country != '':
            tupl += (self.country,)

        return tupl
