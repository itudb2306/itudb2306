


class UpdateForm:
    def __init__(self, id=None, title=None):
        self.id = id
        self.title = title
    
    def from_dict(self, dict):
        self.id = dict.get('discussionID', None)
        if self.id is None:
            raise Exception("discussionID is required")
        self.title = dict.get('title', None)
        return self

    def to_dict(self):
        return {
            'discussionID': self.id,
            'title': self.title,
        }

    def to_tuple(self):
        tuple = ()

        if self.id is not None and self.id != '':
            tuple += (self.id,)
        if self.title is not None and self.title != '':
            tuple += (self.title,)

        return tuple



class FilterForm:
    def __init__(self, title=None, create_time=None, author=None, last_post_time=None, last_post_author=None):
        self.title = title
        self.create_time = create_time
        self.author = author
        self.last_post_time = last_post_time
        self.last_post_author = last_post_author

    def is_empty(self):
        empty = [None, 'None', '']
        return self.title in empty and self.create_time in empty and self.author in empty and self.last_post_time in empty and self.last_post_author in empty
    
    def from_dict(self, dict):
        self.title = dict.get('filterTitle', None)
        if self.title == '':
            self.title = None
        self.create_time = dict.get('filterCreateTime', None)
        if self.create_time == '':
            self.create_time = None
        self.author = dict.get('filterAuthor', None)
        if self.author == '':
            self.author = None
        self.last_post_time = dict.get('filterLastPostTime', None)
        if self.last_post_time == '':
            self.last_post_time = None
        self.last_post_author = dict.get('filterLastPostAuthor', None)
        if self.last_post_author == '':
            self.last_post_author = None
        return self
    
    def to_dict(self):
        filter_dict = {
            'filterTitle': self.title,
            'filterCreateTime': self.create_time,
            'filterAuthor': self.author,
            'filterLastPostTime': self.last_post_time,
            'filterLastPostAuthor': self.last_post_author,
        }
        filter_dict = {k: v for k, v in filter_dict.items() if v is not None and v != 'None' and v != ''}
        return filter_dict
    
    def to_and_string(self):
        and_string = ''
        if self.title is not None and self.title != '':
            and_string += " AND title LIKE '%{}%'".format(self.title)
        if self.create_time is not None and self.create_time != '':
            and_string += " AND create_time LIKE '%{}%'".format(self.create_time)
        if self.author is not None and self.author != '':
            and_string += " AND username LIKE '%{}%'".format(self.author)
        if self.last_post_time is not None and self.last_post_time != '':
            and_string += " AND last_post_time LIKE '%{}%'".format(self.last_post_time)
        if self.last_post_author is not None and self.last_post_author != '':
            and_string += " AND last_post_username LIKE '%{}%'".format(self.last_post_author)
        
        if and_string != '':
            and_string = and_string[5:]
        return and_string


class SortForm:
    def __init__(self, title=None, create_time=None, author=None, last_post_time=None, last_post_author=None):
        self.title = title
        self.create_time = create_time
        self.author = author
        self.last_post_time = last_post_time
        self.last_post_author = last_post_author

    def is_empty(self):
        empty = [None, 'None', '']
        return self.title in empty and self.create_time in empty and self.author in empty and self.last_post_time in empty and self.last_post_author in empty
    
    def from_dict(self, dict):
        self.title = dict.get('sortTitle', None)
        if self.title == '':
            self.title = None
        self.create_time = dict.get('sortCreateTime', None)
        if self.create_time == '':
            self.create_time = None
        self.author = dict.get('sortAuthor', None)
        if self.author == '':
            self.author = None
        self.last_post_time = dict.get('sortLastPostTime', None)
        if self.last_post_time == '':
            self.last_post_time = None
        self.last_post_author = dict.get('sortLastPostAuthor', None)
        if self.last_post_author == '':
            self.last_post_author = None
        return self
    
    def to_dict(self):
        sort_dict = {
            'sortTitle': self.title,
            'sortCreateTime': self.create_time,
            'sortAuthor': self.author,
            'sortLastPostTime': self.last_post_time,
            'sortLastPostAuthor': self.last_post_author,
        }
        sort_dict = {k: v for k, v in sort_dict.items() if v is not None and v != 'None' and v != ''}
        return sort_dict
    
    def to_and_string(self):
        and_string = ''
        if self.title is not None and self.title != '':
            and_string += " AND title {}".format(self.title)
        if self.create_time is not None and self.create_time != '':
            and_string += " AND create_time {}".format(self.create_time)
        if self.author is not None and self.author != '':
            and_string += " AND username {}".format(self.author)
        if self.last_post_time is not None and self.last_post_time != '':
            and_string += " AND last_post_time {}".format(self.last_post_time)
        if self.last_post_author is not None and self.last_post_author != '':
            and_string += " AND last_post_username {}".format(self.last_post_author)

        if and_string != '':
            and_string = and_string[5:]
        return and_string