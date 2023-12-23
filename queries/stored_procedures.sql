DELIMITER $$
CREATE PROCEDURE GetLeaguesList()
BEGIN
SELECT lgID, league FROM leagues;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetDivisionsList()
BEGIN
SELECT ID, division FROM divisions;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetTeamNamesList()
BEGIN
SELECT ID, name FROM teamnames;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetParksList()
BEGIN
SELECT ID, parkname FROM parks;
END$$
DELIMITER ;

-- For forum page
DELIMITER $$
CREATE PROCEDURE GetTopicPage(IN tID INT, IN p INT)
BEGIN
DECLARE page INT;
SET page = (p - 1)*20;
SELECT postID, content, create_time, userID, u.user_name 
FROM posts
JOIN users u ON posts.userID = u.userID
WHERE topicID = tID
ORDER BY create_time ASC
LIMIT page, 20;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE GetTopicPageCount(IN tID INT)
BEGIN
SELECT COUNT(*) FROM posts WHERE topicID = tID;
END$$
DELIMITER ;

-- Stored Procedure for teams details
-- Best Batters
DELIMITER $$
CREATE PROCEDURE GetBestBatters(IN tID INT, IN yID INT)
BEGIN
SELECT 	
    p.nameFirst as nameFirst,
    p.nameLast as nameLast,
    p.nameGiven as nameGiven,
    b.RBI/b.AB AS ratio
FROM batting b
JOIN people p USING(playerID)
WHERE 
    team_ID = tID AND
    yearID = yID
ORDER BY ratio DESC 
LIMIT 3;
END$$
DELIMITER ;

-- Best Pitchers
DELIMITER $$
CREATE PROCEDURE GetBestPitchers(IN tID INT, IN yID INT)
BEGIN
SELECT 	
    p.nameFirst as nameFirst,
    p.nameLast as nameLast,
    p.nameGiven as nameGiven,
    pi.w/pi.g AS ratio
FROM pitching pi
JOIN people p USING(playerID)
WHERE 
    team_ID = tID AND
    yearID = yID
ORDER BY ratio DESC 
LIMIT 3;
END$$
DELIMITER ;

-- Best Fielders
DELIMITER $$
CREATE PROCEDURE GetBestFielders(IN tID INT, IN yID INT)
BEGIN
SELECT 	
    p.nameFirst as nameFirst,
    p.nameLast as nameLast,
    p.nameGiven as nameGiven,
    f.PO/f.InnOuts AS ratio
FROM fielding f
JOIN people p USING(playerID)
WHERE 
    team_ID = tID AND
    yearID = yID
ORDER BY ratio DESC 
LIMIT 3;
END$$
DELIMITER ;