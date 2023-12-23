-- this is a view that is used in the web app to display the teams table
create view teams_easy as
select 
    t.ID as ID,
    t.teamID as team_code,
    tn.name as name,
    t.yearID as year,
    l.league as league,
    d.division as division,
    p.parkname as park,
    t.teamRank as team_rank,
    t.G as games,
    t.Ghome as home_games,
    t.W as wins,
    t.L as losses,
    t.DivWin as division_win,
    t.WCWin as wild_card_win,
    t.LgWin as league_win,
    t.WSWin as world_series_win
from teams t
left join leagues l on t.lgID = l.lgID
left join divisions d on t.div_ID = d.ID
left join teamnames tn on t.team_ID = tn.ID
left join parks p on t.park_ID = p.ID

-- This is for holding the details of the teams
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

-- this is used to show homegames table easily with joins
create view homegames_easy as 
select 
	h.ID as ID,
	h.yearkey as year,
    l.league as league,
    tn.name as team_name,
    p.parkname as park_name,
    h.games as games,
    h.openings as openings,
    h.attendance as attendance,
    h.spanfirst_date as spanfirst_date,
    h.spanlast_date as spanlast_date,
    tn.ID as team_ID,
    l.lgID as lgID,
    p.ID as park_ID
from homegames h
left join teamnames tn on tn.ID = h.team_ID
left join parks p on p.ID = h.park_ID
left join leagues l on h.leaguekey = l.lgID;

-- this is used to show team names easily
create view team_names_count as
select tn1.ID as ID,
    tn1.name as name,
    tn2.cnt as cnt
from teamnames tn1 
left join 
( select
        teamnames.ID as ID,
        count(teamnames.ID) as cnt
        from teamnames left join teams on
        teams.team_ID = teamnames.ID
        group by teamnames.ID
) as tn2 on tn1.ID = tn2.ID;

-- this is used to show the divisions table easily
create view divisions_leagues as 
select 
    l.lgID as lgID,
    l.league as league,
    l.active as lgActive,
    d.divID as divID,
    d.division as division, 
    d.active as divActive,
    d.ID as ID
from divisions d 
left join leagues l on d.lgID=l.lgID;