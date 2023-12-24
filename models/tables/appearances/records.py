

# ID, nameFirst, nameLast, yearID, name(from teamnames table), league, inseason, G, W, L, teamRank, plyrMgr
class Record:
    def __init__(self, ID = None, nameFirst = None, nameLast = None, year_id = None, name = None, league = None, G_all = None, G_batting = None, G_defense = None, G_p = None, G_c = None, G_1b = None, G_2b = None, G_3b = None, G_ss = None, G_lf = None, G_cf = None, G_rf = None, G_of = None, G_dh = None, G_ph = None, G_pr = None):
        self.ID = ID
        self.nameFirst = nameFirst
        self.nameLast = nameLast
        self.year_id = year_id
        self.name = name
        self.league = league
        self.G_all = G_all
        self.G_batting = G_batting
        self.G_defense = G_defense
        self.G_p = G_p
        self.G_c = G_c
        self.G_1b = G_1b
        self.G_2b = G_2b
        self.G_3b = G_3b
        self.G_ss = G_ss
        self.G_lf = G_lf
        self.G_cf = G_cf
        self.G_rf = G_rf
        self.G_of = G_of
        self.G_dh = G_dh
        self.G_ph = G_ph
        self.G_pr = G_pr



    # record.player_id -> record['player_id']
    # No need for this, since we can use record.player_id in jinja2 templates
    #def __getitem__(self, key):
    #    return getattr(self, key)

    def from_list(self, list):
        self.ID = list[0]
        self.nameFirst = list[1]
        self.nameLast = list[2]
        self.year_id = list[3]
        self.name = list[4]
        self.league = list[5]
        self.G_all = list[6]
        self.G_batting = list[7]
        self.G_defense = list[8]
        self.G_p = list[9]
        self.G_c = list[10]
        self.G_1b = list[11]
        self.G_2b = list[12]
        self.G_3b = list[13]
        self.G_ss = list[14]
        self.G_lf = list[15]
        self.G_cf = list[16]
        self.G_rf = list[17]
        self.G_of = list[18]
        self.G_dh = list[19]
        self.G_ph = list[20]
        self.G_pr = list[21]
        return self
        

    def from_dict(self, dict):
        self.ID = dict['ID']
        self.nameFirst = dict['nameFirst']
        self.nameLast = dict['nameLast']
        self.year_id = dict['yearID']
        self.name = dict['name']
        self.league = dict['league']
        self.G_all = dict['G_all']
        self.G_batting = dict['G_batting']
        self.G_defense = dict['G_defense']
        self.G_p = dict['G_p']
        self.G_c = dict['G_c']
        self.G_1b = dict['G_1b']
        self.G_2b = dict['G_2b']
        self.G_3b = dict['G_3b']
        self.G_ss = dict['G_ss']
        self.G_lf = dict['G_lf']
        self.G_cf = dict['G_cf']
        self.G_rf = dict['G_rf']
        self.G_of = dict['G_of']
        self.G_dh = dict['G_dh']
        self.G_ph = dict['G_ph']
        self.G_pr = dict['G_pr']

        return self

    def to_list(self):
        return [
            self.ID,
            self.nameFirst,
            self.nameLast,
            self.year_id,
            self.name,
            self.league,
            self.G_all,
            self.G_batting,
            self.G_defense,
            self.G_p,
            self.G_c,
            self.G_1b,
            self.G_2b,
            self.G_3b,
            self.G_ss,
            self.G_lf,
            self.G_cf,
            self.G_rf,
            self.G_of,
            self.G_dh,
            self.G_ph,
            self.G_pr
        ]

    def to_dict(self):
        return {
            'ID' : self.ID,
            'nameFirst' : self.nameFirst,
            'nameLast' : self.nameLast,
            'yearID' : self.year_id,
            'name' : self.name,
            'league' : self.league,
            'G_all' : self.G_all,
            'G_batting' : self.G_batting,
            'G_defense' : self.G_defense,
            'G_p' : self.G_p,
            'G_c' : self.G_c,
            'G_1b' : self.G_1b,
            'G_2b' : self.G_2b,
            'G_3b' : self.G_3b,
            'G_ss' : self.G_ss,
            'G_lf' : self.G_lf,
            'G_cf' : self.G_cf,
            'G_rf' : self.G_rf,
            'G_of' : self.G_of,
            'G_dh' : self.G_dh,
            'G_ph' : self.G_ph,
            'G_pr' : self.G_pr
        }

class Records:
    def __init__(self, records : list = None):
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
    


