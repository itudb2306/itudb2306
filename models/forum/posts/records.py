

class Record:
    def __init__(self, postID=None, topicID=None, userID=None, create_time=None, content=None, author=None):
        self.postID = postID
        self.topicID = topicID
        self.userID = userID
        self.create_time = create_time
        self.content = content
        self.author = author

    def from_list(self, list):
        self.postID = list[0]
        self.topicID = list[1]
        self.userID = list[2]
        self.create_time = list[3]
        self.content = list[4]
        self.author = list[5]
        return self

    def from_dict(self, dict):
        self.postID = dict['postID']
        self.topicID = dict['topicID']
        self.userID = dict['userID']
        self.create_time = dict['create_time']
        self.content = dict['content']
        self.author = dict['author']
        return self

    def to_list(self):
        return [self.postID, self.topicID, self.userID, self.create_time, self.content, self.author]

    def to_dict(self):
        return {
            'postID': self.postID,
            'topicID': self.topicID,
            'userID': self.userID,
            'create_time': self.create_time,
            'content': self.content,
            'author': self.author
        }
    


class Records:
    def __init__(self, records: list = None):
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