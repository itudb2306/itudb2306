-- create view teams_easy to show the teams table with all the foreign keys replaced with their names
-- this is a view that is used in the web app to display the teams table
create view teams_easy as
select 
    t.ID as ID,
    tn.name as name,
    t.yearID as year,
    l.league as league,
    d.division as division,
    p.parkname as park,
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
