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
