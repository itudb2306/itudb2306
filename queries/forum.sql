-- Forum pages
CREATE TABLE topics (
    topicID int AUTO_INCREMENT,
    userID int unsigned NOT NULL,
    create_time datetime NOT NULL,
    title varchar(64),
    PRIMARY KEY (topicID),
    CONSTRAINT fk_topic_user FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE posts (
    postID int AUTO_INCREMENT,
    topicID int NOT NULL,
    userID int unsigned NOT NULL,
    create_time datetime NOT NULL,
    content text NOT NULL,
    PRIMARY KEY (postID),
    CONSTRAINT fk_post_topic FOREIGN KEY (topicID) REFERENCES topics(topicID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_post_user FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP VIEW IF EXISTS topic_view;

-- ADD count post
CREATE VIEW topic_view AS
SELECT
    t.topicID as topicID,
    t.title as title,
    t.create_time as create_time,
    t.userID as userID,
    t.username as username,
    t.count_post,
    p.postID as last_post_ID,
    p.create_time as last_post_time,
    p.userID as last_post_userID,
    u.username as last_post_username
FROM (SELECT 
    t1.topicID as topicID,
    t1.title as title,
    t1.create_time as create_time,
    t1.userID as userID,
    u1.username as username,
    COUNT(p1.postID) as count_post,
    MAX(p1.create_time) as last_post_time
FROM topics t1
JOIN users u1 ON t1.userID = u1.userID
JOIN posts p1 ON t1.topicID = p1.topicID
GROUP BY t1.topicID) as t
JOIN posts p ON t.last_post_time = p.create_time
JOIN users u ON p.userID = u.userID;

DROP VIEW IF EXISTS post_view;

CREATE VIEW post_view AS
SELECT
    p.postID as postID,
    p.topicID as topicID,
    p.userID as userID,
    p.create_time as create_time,
    p.content as content,
    u.username as username
FROM posts p
JOIN users u ON p.userID = u.userID;

