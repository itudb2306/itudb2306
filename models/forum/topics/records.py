

# [(1, 'a', datetime.datetime(2023, 12, 23, 16, 25, 3), 1, 'admin', 1, 1, datetime.datetime(2023, 12, 23, 16, 25, 3), 1, 'admin'), (2, 'aa', datetime.datetime(2023, 12, 23, 17, 4, 6), 1, 'admin', 1, 2, datetime.datetime(2023, 12, 23, 17, 4, 6), 1, 'admin')]

# topicID, title, create_time, author, authorID, last_postID, last_post_time, last_post_author, last_post_authorID

class Record:
    def __init__(self, topicID = None, title = None, create_time = None, author = None, authorID = None, last_postID = None, last_post_time = None, last_post_author = None, last_post_authorID = None, count_post = None):
        self.topicID = topicID
        self.title = title
        self.create_time = create_time
        self.author = author
        self.authorID = authorID
        self.count_post = count_post
        self.last_postID = last_postID
        self.last_post_time = last_post_time
        self.last_post_author = last_post_author
        self.last_post_authorID = last_post_authorID

    def from_list(self, list):
        self.topicID = list[0]
        self.title = list[1]
        self.create_time = list[2]
        self.authorID = list[3]
        self.author = list[4]
        self.count_post = list[5]
        self.last_postID = list[6]
        self.last_post_time = list[7]
        self.last_post_authorID = list[8]
        self.last_post_author = list[9]
        return self

    def from_dict(self, dict):
        self.topicID = dict['topicID']
        self.title = dict['title']
        self.create_time = dict['create_time']
        self.authorID = dict['authorID']
        self.author = dict['author']
        self.count_post = dict['count_post']
        self.last_postID = dict['last_postID']
        self.last_post_time = dict['last_post_time']
        self.last_post_authorID = dict['last_post_authorID']
        self.last_post_author = dict['last_post_author']
        return self
    
    def to_list(self):
        return [self.topicID, self.title, self.create_time, self.authorID, self.author, self.count_post, self.last_postID, self.last_post_time, self.last_post_authorID, self.last_post_author]
    
    def to_dict(self):
        return {
            'topicID': self.topicID,
            'title': self.title,
            'create_time': self.create_time,
            'authorID': self.authorID,
            'author': self.author,
            'count_post': self.count_post,
            'last_postID': self.last_postID,
            'last_post_time': self.last_post_time,
            'last_post_authorID': self.last_post_authorID,
            'last_post_author': self.last_post_author
        }
    

class Records:
    def __init__(self, records : list = None):
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
    