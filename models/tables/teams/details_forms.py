"""
+------------+------------+------+-----+---------+----------------+
| ID         | int        | NO   | PRI | NULL    | auto_increment |
| yearID     | smallint   | NO   | MUL | NULL    |                |
| lgID       | char(2)    | YES  | MUL | NULL    |                |
| teamID     | char(3)    | NO   |     | NULL    |                |
| div_ID     | int        | YES  | MUL | NULL    |                |
| teamRank   | smallint   | YES  |     | NULL    |                |
| G          | smallint   | YES  |     | NULL    |                |
| Ghome      | smallint   | YES  |     | NULL    |                |
| W          | smallint   | YES  |     | NULL    |                |
| L          | smallint   | YES  |     | NULL    |                |
| DivWin     | varchar(1) | YES  |     | NULL    |                |
| WCWin      | varchar(1) | YES  |     | NULL    |                |
| LgWin      | varchar(1) | YES  |     | NULL    |                |
| WSWin      | varchar(1) | YES  |     | NULL    |                |
| R          | smallint   | YES  |     | NULL    |                |
| AB         | smallint   | YES  |     | NULL    |                |
| H          | smallint   | YES  |     | NULL    |                |
| 2B         | smallint   | YES  |     | NULL    |                |
| 3B         | smallint   | YES  |     | NULL    |                |
| HR         | smallint   | YES  |     | NULL    |                |
| BB         | smallint   | YES  |     | NULL    |                |
| SO         | smallint   | YES  |     | NULL    |                |
| SB         | smallint   | YES  |     | NULL    |                |
| CS         | smallint   | YES  |     | NULL    |                |
| HBP        | smallint   | YES  |     | NULL    |                |
| SF         | smallint   | YES  |     | NULL    |                |
| RA         | smallint   | YES  |     | NULL    |                |
| ER         | smallint   | YES  |     | NULL    |                |
| ERA        | double     | YES  |     | NULL    |                |
| CG         | smallint   | YES  |     | NULL    |                |
| SHO        | smallint   | YES  |     | NULL    |                |
| SV         | smallint   | YES  |     | NULL    |                |
| IPouts     | int        | YES  |     | NULL    |                |
| HA         | smallint   | YES  |     | NULL    |                |
| HRA        | smallint   | YES  |     | NULL    |                |
| BBA        | smallint   | YES  |     | NULL    |                |
| SOA        | smallint   | YES  |     | NULL    |                |
| E          | int        | YES  |     | NULL    |                |
| DP         | int        | YES  |     | NULL    |                |
| FP         | double     | YES  |     | NULL    |                |
| attendance | int        | YES  |     | NULL    |                |
| BPF        | int        | YES  |     | NULL    |                |
| PPF        | int        | YES  |     | NULL    |                |
| park_ID    | int        | YES  | MUL | NULL    |                |
| team_ID    | int        | NO   | MUL | NULL    |                |
+------------+------------+------+-----+---------+----------------+

"""


"""
create view teams_details as
select 
    t.ID as ID,
    t.teamID as team_code,
    tn.name as name,
    tn.ID as team_name_ID,
    t.yearID as year,
    l.league as league,
    l.lgID as league_ID,
    d.division as division,
    d.ID as division_ID,
    p.parkname as park,
    p.ID as park_ID,
    t.teamRank as team_rank,
    t.G as games,
    t.Ghome as home_games,
    t.W as wins,
    t.L as losses,
    t.DivWin as division_win,
    t.WCWin as wild_card_win,
    t.LgWin as league_win,
    t.WSWin as world_series_win,
    t.R as runs_scored,
    t.AB as at_bats,
    t.H as hits,
    t.2B as doubles,
    t.3B as triples,
    t.HR as homeruns,
    t.BB as walks_batters,
    t.SO as strikeouts_batters,
    t.SB as stolen_bases,
    t.CS as caught_stealing,
    t.HBP as hit_by_pitch,
    t.SF as sacrifice_flies,
    t.RA as runs_allowed,
    t.ER as earned_runs_allowed,
    t.ERA as earned_run_average,
    t.CG as complete_games,
    t.SHO as shutouts,
    t.SV as saves,
    t.IPOuts as outs_pitched,
    t.HA as hits_allowed,
    t.HRA as homeruns_allowed,
    t.BBA as walks_allowed,
    t.SOA as strikeouts_pitchers,
    t.E as errors,
    t.DP as double_plays,
    t.FP as fielding_percentage,
    t.attendance as attendance,
    t.BPF as batter_park_factor,
    t.PPF as pitcher_park_factor
from teams t
left join leagues l on t.lgID = l.lgID
left join divisions d on t.div_ID = d.ID
left join teamnames tn on t.team_ID = tn.ID
left join parks p on t.park_ID = p.ID
"""


class UpdateForm:
    def __init__(self, ID: int = None, yearID: int = None, lgID: str = None, teamID: str = None,
                 div_ID: int = None, teamRank: int = None, G: int = None, Ghome: int = None, W: int = None,
                 L: int = None, DivWin: str = None, WCWin: str = None, LgWin: str = None, WSWin: str = None,
                 R: int = None, AB: int = None, H: int = None, _2B: int = None, _3B: int = None, HR: int = None,
                 BB: int = None, SO: int = None, SB: int = None, CS: int = None, HBP: int = None, SF: int = None,
                 RA: int = None, ER: int = None, ERA: float = None, CG: int = None, SHO: int = None, SV: int = None,
                 IPouts: int = None, HA: int = None, HRA: int = None, BBA: int = None, SOA: int = None, E: int = None,
                 DP: int = None, FP: float = None, attendance: int = None, BPF: int = None, PPF: int = None,
                 park_ID: int = None, team_ID: int = None):
        self.ID = ID
        self.yearID = yearID
        self.lgID = lgID
        self.teamID = teamID
        self.div_ID = div_ID
        self.teamRank = teamRank
        self.G = G
        self.Ghome = Ghome
        self.W = W
        self.L = L
        self.DivWin = DivWin
        self.WCWin = WCWin
        self.LgWin = LgWin
        self.WSWin = WSWin
        self.R = R
        self.AB = AB
        self.H = H
        self._2B = _2B
        self._3B = _3B
        self.HR = HR
        self.BB = BB
        self.SO = SO
        self.SB = SB
        self.CS = CS
        self.HBP = HBP
        self.SF = SF
        self.RA = RA
        self.ER = ER
        self.ERA = ERA
        self.CG = CG
        self.SHO = SHO
        self.SV = SV
        self.IPouts = IPouts
        self.HA = HA
        self.HRA = HRA
        self.BBA = BBA
        self.SOA = SOA
        self.E = E
        self.DP = DP
        self.FP = FP
        self.attendance = attendance
        self.BPF = BPF
        self.PPF = PPF
        self.park_ID = park_ID
        self.team_ID = team_ID

    # Request args from form
    def from_dict(self, dict):
        self.ID = dict.get('ID', None)
        if self.ID is None:
            raise Exception("ID is required(Primary Key column)")

        self.yearID = dict.get('yearID', None)
        if self.yearID == "":
            self.yearID = None

        self.lgID = dict.get('lgID', None)
        if self.lgID == "":
            self.lgID = None

        self.teamID = dict.get('teamID', None)
        if self.teamID == "":
            self.teamID = None

        self.div_ID = dict.get('div_ID', None)
        if self.div_ID == "":
            self.div_ID = None

        self.teamRank = dict.get('teamRank', None)
        if self.teamRank == "":
            self.teamRank = None

        self.G = dict.get('G', None)
        if self.G == "":
            self.G = None

        self.Ghome = dict.get('Ghome', None)
        if self.Ghome == "":
            self.Ghome = None

        self.W = dict.get('W', None)
        if self.W == "":
            self.W = None

        self.L = dict.get('L', None)
        if self.L == "":
            self.L = None

        self.DivWin = dict.get('DivWin', None)
        if self.DivWin == "":
            self.DivWin = None

        self.WCWin = dict.get('WCWin', None)
        if self.WCWin == "":
            self.WCWin = None

        self.LgWin = dict.get('LgWin', None)
        if self.LgWin == "":
            self.LgWin = None

        self.WSWin = dict.get('WSWin', None)
        if self.WSWin == "":
            self.WSWin = None

        self.R = dict.get('R', None)
        if self.R == "":
            self.R = None

        self.AB = dict.get('AB', None)
        if self.AB == "":
            self.AB = None

        self.H = dict.get('H', None)
        if self.H == "":
            self.H = None

        self._2B = dict.get('2B', None)
        if self._2B == "":
            self._2B = None

        self._3B = dict.get('3B', None)
        if self._3B == "":
            self._3B = None

        self.HR = dict.get('HR', None)
        if self.HR == "":
            self.HR = None

        self.BB = dict.get('BB', None)
        if self.BB == "":
            self.BB = None

        self.SO = dict.get('SO', None)
        if self.SO == "":
            self.SO = None

        self.SB = dict.get('SB', None)
        if self.SB == "":
            self.SB = None

        self.CS = dict.get('CS', None)
        if self.CS == "":
            self.CS = None

        self.HBP = dict.get('HBP', None)
        if self.HBP == "":
            self.HBP = None

        self.SF = dict.get('SF', None)
        if self.SF == "":
            self.SF = None

        self.RA = dict.get('RA', None)
        if self.RA == "":
            self.RA = None

        self.ER = dict.get('ER', None)
        if self.ER == "":
            self.ER = None

        self.ERA = dict.get('ERA', None)
        if self.ERA == "":
            self.ERA = None

        self.CG = dict.get('CG', None)
        if self.CG == "":
            self.CG = None

        self.SHO = dict.get('SHO', None)
        if self.SHO == "":
            self.SHO = None

        self.SV = dict.get('SV', None)
        if self.SV == "":
            self.SV = None

        self.IPouts = dict.get('IPouts', None)
        if self.IPouts == "":
            self.IPouts = None

        self.HA = dict.get('HA', None)
        if self.HA == "":
            self.HA = None

        self.HRA = dict.get('HRA', None)
        if self.HRA == "":
            self.HRA = None

        self.BBA = dict.get('BBA', None)
        if self.BBA == "":
            self.BBA = None

        self.SOA = dict.get('SOA', None)
        if self.SOA == "":
            self.SOA = None

        self.E = dict.get('E', None)
        if self.E == "":
            self.E = None

        self.DP = dict.get('DP', None)
        if self.DP == "":
            self.DP = None

        self.FP = dict.get('FP', None)
        if self.FP == "":
            self.FP = None

        self.attendance = dict.get('attendance', None)
        if self.attendance == "":
            self.attendance = None

        self.BPF = dict.get('BPF', None)
        if self.BPF == "":
            self.BPF = None

        self.PPF = dict.get('PPF', None)
        if self.PPF == "":
            self.PPF = None

        self.park_ID = dict.get('park_ID', None)
        if self.park_ID == "":
            self.park_ID = None

        self.team_ID = dict.get('team_ID', None)
        if self.team_ID == "":
            self.team_ID = None

        return self

    def to_set_string(self):
        empty = [None, '', 'None']
        set_string = ""

        if self.yearID not in empty:
            set_string += "yearID = %s, "
        else:
            set_string += "yearID = NULL, "

        if self.lgID not in empty:
            set_string += "lgID = %s, "
        else:
            set_string += "lgID = NULL, "

        if self.teamID not in empty:
            set_string += "teamID = %s, "
        else:
            set_string += "teamID = NULL, "

        if self.div_ID not in empty:
            set_string += "div_ID = %s, "
        else:
            set_string += "div_ID = NULL, "

        if self.teamRank not in empty:
            set_string += "teamRank = %s, "
        else:
            set_string += "teamRank = NULL, "

        if self.G not in empty:
            set_string += "G = %s, "
        else:
            set_string += "G = NULL, "

        if self.Ghome not in empty:
            set_string += "Ghome = %s, "
        else:
            set_string += "Ghome = NULL, "

        if self.W not in empty:
            set_string += "W = %s, "
        else:
            set_string += "W = NULL, "

        if self.L not in empty:
            set_string += "L = %s, "
        else:
            set_string += "L = NULL, "

        if self.DivWin not in empty:
            set_string += "DivWin = %s, "
        else:
            set_string += "DivWin = NULL, "

        if self.WCWin not in empty:
            set_string += "WCWin = %s, "
        else:
            set_string += "WCWin = NULL, "

        if self.LgWin not in empty:
            set_string += "LgWin = %s, "
        else:
            set_string += "LgWin = NULL, "

        if self.WSWin not in empty:
            set_string += "WSWin = %s, "
        else:
            set_string += "WSWin = NULL, "

        if self.R not in empty:
            set_string += "R = %s, "
        else:
            set_string += "R = NULL, "

        if self.AB not in empty:
            set_string += "AB = %s, "
        else:
            set_string += "AB = NULL, "

        if self.H not in empty:
            set_string += "H = %s, "
        else:
            set_string += "H = NULL, "

        if self._2B not in empty:
            set_string += "2B = %s, "
        else:
            set_string += "2B = NULL, "

        if self._3B not in empty:
            set_string += "3B = %s, "
        else:
            set_string += "3B = NULL, "

        if self.HR not in empty:
            set_string += "HR = %s, "
        else:
            set_string += "HR = NULL, "

        if self.BB not in empty:
            set_string += "BB = %s, "
        else:
            set_string += "BB = NULL, "

        if self.SO not in empty:
            set_string += "SO = %s, "
        else:
            set_string += "SO = NULL, "

        if self.SB not in empty:
            set_string += "SB = %s, "
        else:
            set_string += "SB = NULL, "

        if self.CS not in empty:
            set_string += "CS = %s, "
        else:
            set_string += "CS = NULL, "

        if self.HBP not in empty:
            set_string += "HBP = %s, "
        else:
            set_string += "HBP = NULL, "

        if self.SF not in empty:
            set_string += "SF = %s, "
        else:
            set_string += "SF = NULL, "

        if self.RA not in empty:
            set_string += "RA = %s, "
        else:
            set_string += "RA = NULL, "

        if self.ER not in empty:
            set_string += "ER = %s, "
        else:
            set_string += "ER = NULL, "

        if self.ERA not in empty:
            set_string += "ERA = %s, "
        else:
            set_string += "ERA = NULL, "

        if self.CG not in empty:
            set_string += "CG = %s, "
        else:
            set_string += 'CG = NULL, '

        if self.SHO not in empty:
            set_string += "SHO = %s, "
        else:
            set_string += "SHO = NULL, "

        if self.SV not in empty:
            set_string += "SV = %s, "
        else:
            set_string += "SV = NULL, "

        if self.IPouts not in empty:
            set_string += "IPouts = %s, "
        else:
            set_string += "IPouts = NULL, "

        if self.HA not in empty:
            set_string += "HA = %s, "
        else:
            set_string += "HA = NULL, "

        if self.HRA not in empty:
            set_string += "HRA = %s, "
        else:
            set_string += "HRA = NULL, "

        if self.BBA not in empty:
            set_string += "BBA = %s, "
        else:
            set_string += "BBA = NULL, "

        if self.SOA not in empty:
            set_string += "SOA = %s, "
        else:
            set_string += "SOA = NULL, "

        if self.E not in empty:
            set_string += "E = %s, "
        else:
            set_string += "E = NULL, "

        if self.DP not in empty:
            set_string += "DP = %s, "
        else:
            set_string += "DP = NULL, "

        if self.FP not in empty:
            set_string += "FP = %s, "
        else:
            set_string += "FP = NULL, "

        if self.attendance not in empty:
            set_string += "attendance = %s, "
        else:
            set_string += "attendance = NULL, "

        if self.BPF not in empty:
            set_string += "BPF = %s, "
        else:
            set_string += "BPF = NULL, "

        if self.PPF not in empty:
            set_string += "PPF = %s, "
        else:
            set_string += "PPF = NULL, "

        if self.park_ID not in empty:
            set_string += "park_ID = %s, "
        else:
            set_string += "park_ID = NULL, "

        if self.team_ID not in empty:
            set_string += "team_ID = %s, "
        else:
            set_string += "team_ID = NULL, "

        if set_string != "":
            set_string = set_string[:-2]
        return set_string

    def to_tuple(self):
        tupl = ()
        empty = [None, '', 'None']

        if self.yearID not in empty:
            tupl += (self.yearID,)

        if self.lgID not in empty:
            tupl += (self.lgID,)

        if self.teamID not in empty:
            tupl += (self.teamID,)

        if self.div_ID not in empty:
            tupl += (self.div_ID,)

        if self.teamRank not in empty:
            tupl += (self.teamRank,)

        if self.G not in empty:
            tupl += (self.G,)

        if self.Ghome not in empty:
            tupl += (self.Ghome,)

        if self.W not in empty:
            tupl += (self.W,)

        if self.L not in empty:
            tupl += (self.L,)

        if self.DivWin not in empty:
            tupl += (self.DivWin,)

        if self.WCWin not in empty:
            tupl += (self.WCWin,)

        if self.LgWin not in empty:
            tupl += (self.LgWin,)

        if self.WSWin not in empty:
            tupl += (self.WSWin,)

        if self.R not in empty:
            tupl += (self.R,)

        if self.AB not in empty:
            tupl += (self.AB,)

        if self.H not in empty:
            tupl += (self.H,)

        if self._2B not in empty:
            tupl += (self._2B,)

        if self._3B not in empty:
            tupl += (self._3B,)

        if self.HR not in empty:
            tupl += (self.HR,)

        if self.BB not in empty:
            tupl += (self.BB,)

        if self.SO not in empty:
            tupl += (self.SO,)

        if self.SB not in empty:
            tupl += (self.SB,)

        if self.CS not in empty:
            tupl += (self.CS,)

        if self.HBP not in empty:
            tupl += (self.HBP,)

        if self.SF not in empty:
            tupl += (self.SF,)

        if self.RA not in empty:
            tupl += (self.RA,)

        if self.ER not in empty:
            tupl += (self.ER,)

        if self.ERA not in empty:
            tupl += (self.ERA,)

        if self.CG not in empty:
            tupl += (self.CG,)

        if self.SHO not in empty:
            tupl += (self.SHO,)

        if self.SV not in empty:
            tupl += (self.SV,)

        if self.IPouts not in empty:
            tupl += (self.IPouts,)

        if self.HA not in empty:
            tupl += (self.HA,)

        if self.HRA not in empty:
            tupl += (self.HRA,)

        if self.BBA not in empty:
            tupl += (self.BBA,)

        if self.SOA not in empty:
            tupl += (self.SOA,)

        if self.E not in empty:
            tupl += (self.E,)

        if self.DP not in empty:
            tupl += (self.DP,)

        if self.FP not in empty:
            tupl += (self.FP,)

        if self.attendance not in empty:
            tupl += (self.attendance,)

        if self.BPF not in empty:
            tupl += (self.BPF,)

        if self.PPF not in empty:
            tupl += (self.PPF,)

        if self.park_ID not in empty:
            tupl += (self.park_ID,)

        if self.team_ID not in empty:
            tupl += (self.team_ID,)

        return tupl
