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

    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.parkalias = dict.get('park_alias', None)
        self.parkkey = dict.get('park_key', None)
        self.parkname = dict.get('park_name', None)
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

    def from_dict(self, dict):

        self.parkalias = dict.get('park_alias', None)
        self.parkkey = dict.get('park_key', None)
        self.parkname = dict.get('park_name', None)
        self.city = dict.get('city', None)
        self.state = dict.get('state', None)
        self.country = dict.get('country', None)

        return self

    def to_dict(self):
        return {
            'park_alias': self.parkalias,
            'park_key': self.parkkey,
            'park_name': self.parkname,
            'city': self.city,
            'state': self.state,
            'country': self.country
        }

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

        if and_string != "":
            and_string = and_string[5:]

        return and_string
