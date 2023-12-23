-- Forum pages
CREATE TABLE topics (
    topicID int AUTO_INCREMENT,
    userID int unsigned NOT NULL,
    create_time datetime NOT NULL,
    title varchar(64),
    PRIMARY KEY (topicID),
    CONSTRAINT fk_topic_user FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE posts (
    postID int AUTO_INCREMENT,
    topicID int NOT NULL,
    userID int unsigned NOT NULL,
    create_time datetime NOT NULL,
    content text NOT NULL,
    PRIMARY KEY (postID),
    CONSTRAINT fk_post_topic FOREIGN KEY (topicID) REFERENCES topics(topicID),
    CONSTRAINT fk_post_user FOREIGN KEY (userID) REFERENCES users(userID)
);
