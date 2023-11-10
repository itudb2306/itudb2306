from dataclasses import dataclass


@dataclass
class PeopleData:
    playerID: str
    nameFirst: str
    nameLast: str
    nameGiven: str
    birth_date: str
    birthCountry: str
    weight: str
    height: str
    bats: str
    throws: str

    def __getitem__(self, key):
        return getattr(self, key)

    @staticmethod
    def from_list(list):
        return PeopleData(
            playerID=list[0],
            nameFirst=list[1],
            nameLast=list[2],
            nameGiven=list[3],
            birth_date=list[4],
            birthCountry=list[5],
            weight=list[6],
            height=list[7],
            bats=list[8],
            throws=list[9]
        )
    
    @staticmethod
    def to_dict(self):
        return {
            'playerID': self.playerID,
            'nameFirst': self.nameFirst,
            'nameLast': self.nameLast,
            'nameGiven': self.nameGiven,
            'birth_date': self.birth_date,
            'birthCountry': self.birthCountry,
            'weight': self.weight,
            'height': self.height,
            'bats': self.bats,
            'throws': self.throws
        }
    
