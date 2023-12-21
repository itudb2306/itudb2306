class NamesRecord:
    def __init__(self, ID: int = None, name: str = None, count: int = None):
        self.ID = ID
        self.name = name
        self.count = count

    def from_list(self, list):
        self.ID = list[0]
        self.name = list[1]
        self.count = list[2]
        return self

    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        self.name = dict.get('name', None)
        self.count = dict.get('count', None)
        return self

    def to_list(self):
        return [self.ID, self.name, self.count]

    def to_dict(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'count': self.count,
        }


class NamesRecords:
    def __init__(self, records: list = None):
        self.records = records

    def from_list(self, list):
        self.records = []
        for row in list:
            record = NamesRecord().from_list(row)
            self.records.append(record)

    def from_dict(self, dict):
        self.records = []
        for row in dict:
            self.records.append(NamesRecord().from_dict(row))

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
