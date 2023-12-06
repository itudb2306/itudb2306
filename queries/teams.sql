select t.*, l.league, d.division from teams t left join leagues l on t.lgID=l.lgID left join divisions d on t.div_ID=d.ID order by yearID desc; 
