


# DB Schema: discussions
"""
CREATE TABLE messages (
    messageID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    userID INT UNSIGNED NOT NULL,
    discussionID INT UNSIGNED NOT NULL,
    message TEXT NOT NULL,
    PRIMARY KEY (messageID),
    FOREIGN KEY (userID) REFERENCES users(userID),
    FOREIGN KEY (discssionID) REFERENCES discussions(discussionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE discussions (
    discussionID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    userID INT UNSIGNED NOT NULL,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_messageID INT UNSIGNED NOT NULL,
    PRIMARY KEY (discussionID),
    FOREIGN KEY (userID) REFERENCES users(userID),
    FOREIGN KEY (last_messageID) REFERENCES messages(messageID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

AFTER JOIN:
discussionID, creatorID, creator_name, title, created_at, last_messageID, last_message_userID, last_message_user_name, last_message, last_message_created_at
JOIN Query:
SELECT d.discussionID, d.userID AS creatorID, u.name AS creator_name, d.title, d.created_at, d.last_messageID, m.userID AS last_message_userID, u2.name AS last_message_user_name, m.message AS last_message, m.created_at AS last_message_created_at
"""

class Record:
    def __init__(self, discussionID : int = None, creatorID : int = None, creator_name : str = None, title : str = None, created_at : str = None, last_messageID : int = None, last_message_userID : int = None, last_message_user_name : str = None, last_message : str = None, last_message_created_at : str = None):
        self.discussionID = discussionID
        self.creatorID = creatorID
        self.creator_name = creator_name
        self.title = title
        self.created_at = created_at
        self.last_messageID = last_messageID
        self.last_message_userID = last_message_userID
        self.last_message_user_name = last_message_user_name
        self.last_message = last_message
        self.last_message_created_at = last_message_created_at

    def from_list(self, list):
        self.discussionID = list[0]
        self.creatorID = list[1]
        self.creator_name = list[2]
        self.title = list[3]
        self.created_at = list[4]
        self.last_messageID = list[5]
        self.last_message_userID = list[6]
        self.last_message_user_name = list[7]
        self.last_message = list[8]
        self.last_message_created_at = list[9]
        return self

    def from_dict(self, dict):
        self.discussionID = dict['discussionID']
        self.creatorID = dict['creatorID']
        self.creator_name = dict['creator_name']
        self.title = dict['title']
        self.created_at = dict['created_at']
        self.last_messageID = dict['last_messageID']
        self.last_message_userID = dict['last_message_userID']
        self.last_message_user_name = dict['last_message_user_name']
        self.last_message = dict['last_message']
        self.last_message_created_at = dict['last_message_created_at']
        return self

    def to_list(self):
        return [self.discussionID, self.creatorID, self.creator_name, self.title, self.created_at, self.last_messageID, self.last_message_userID, self.last_message_user_name, self.last_message, self.last_message_created_at]

    def to_dict(self):
        return {
            'discussionID': self.discussionID,
            'creatorID': self.creatorID,
            'creator_name': self.creator_name,
            'title': self.title,
            'created_at': self.created_at,
            'last_messageID': self.last_messageID,
            'last_message_userID': self.last_message_userID,
            'last_message_user_name': self.last_message_user_name,
            'last_message': self.last_message,
            'last_message_created_at': self.last_message_created_at,
        }
    
    def __repr__(self):
        return str(self.to_dict())
    

class Records:
    def __init__(self, records : list = None):
        self.records = records

    def from_list(self, list):
        self.records = []
        for item in list:
            self.records.append(Record().from_list(item))
        return self

    def from_dict(self, dict):
        self.records = []
        for item in dict:
            self.records.append(Record().from_dict(item))
        return self

    def to_list(self):
        list = []
        for item in self.records:
            list.append(item.to_list())
        return list

    def to_dict(self):
        dict = []
        for item in self.records:
            dict.append(item.to_dict())
        return dict

    def __repr__(self):
        return str(self.to_dict())
    