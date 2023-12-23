


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
    def __init__(self, creator_name=None, title=None, created_at=None, last_message_user_name=None, last_message=None, last_message_created_at=None):
        self.creator_name = creator_name
        self.title = title
        self.created_at = created_at
        self.last_message_user_name = last_message_user_name
        self.last_message = last_message
        self.last_message_created_at = last_message_created_at

    def is_empty(self):
        empty = [None, 'None', '']
        return self.creator_name in empty and self.title in empty and self.created_at in empty and self.last_message_user_name in empty and self.last_message in empty and self.last_message_created_at in empty
    
    def from_dict(self, dict):
        self.creator_name = dict.get('filterCreatorName', None)
        if self.creator_name == '':
            self.creator_name = None
        self.title = dict.get('filterTitle', None)
        if self.title == '':
            self.title = None
        self.created_at = dict.get('filterCreatedAt', None)
        if self.created_at == '':
            self.created_at = None
        self.last_message_user_name = dict.get('filterLastMessageUserName', None)
        if self.last_message_user_name == '':
            self.last_message_user_name = None
        self.last_message = dict.get('filterLastMessage', None)
        if self.last_message == '':
            self.last_message = None
        self.last_message_created_at = dict.get('filterLastMessageCreatedAt', None)
        if self.last_message_created_at == '':
            self.last_message_created_at = None
        return self
    
    def to_dict(self):
        filter_dict = {
            'filterCreatorName': self.creator_name,
            'filterTitle': self.title,
            'filterCreatedAt': self.created_at,
            'filterLastMessageUserName': self.last_message_user_name,
            'filterLastMessage': self.last_message,
            'filterLastMessageCreatedAt': self.last_message_created_at,
        }
        filter_dict = {k: v for k, v in filter_dict.items() if v is not None and v != 'None' and v != ''}
        return filter_dict
    
    def to_and_string(self):
        and_string = ''
        if self.creator_name is not None and self.creator_name != '':
            and_string += " AND creator_name = LIKE %{}%".format(self.creator_name)
        if self.title is not None and self.title != '':
            and_string += " AND title = LIKE %{}%".format(self.title)
        if self.created_at is not None and self.created_at != '':
            and_string += " AND created_at = LIKE %{}%".format(self.created_at)
        if self.last_message_user_name is not None and self.last_message_user_name != '':
            and_string += " AND last_message_user_name = LIKE %{}%".format(self.last_message_user_name)
        if self.last_message is not None and self.last_message != '':
            and_string += " AND last_message = LIKE %{}%".format(self.last_message)
        if self.last_message_created_at is not None and self.last_message_created_at != '':
            and_string += " AND last_message_created_at = LIKE %{}%".format(self.last_message_created_at)
        
        if and_string != '':
            and_string = and_string[5:]
        return and_string

# creator_name, title, created_at, last_message_user_name, last_message, last_message_created_at

class SortForm:
    def __init__(self, creator_name=None, title=None, created_at=None, last_message_user_name=None, last_message=None, last_message_created_at=None):
        self.creator_name = creator_name
        self.title = title
        self.created_at = created_at
        self.last_message_user_name = last_message_user_name
        self.last_message = last_message
        self.last_message_created_at = last_message_created_at

    def is_empty(self):
        empty = [None, 'None', '']
        return self.creator_name in empty and self.title in empty and self.created_at in empty and self.last_message_user_name in empty and self.last_message in empty and self.last_message_created_at in empty
    
    def from_dict(self, dict):
        self.creator_name = dict.get('sortCreatorName', None)
        if self.creator_name == '':
            self.creator_name = None
        self.title = dict.get('sortTitle', None)
        if self.title == '':
            self.title = None
        self.created_at = dict.get('sortCreatedAt', None)
        if self.created_at == '':
            self.created_at = None
        self.last_message_user_name = dict.get('sortLastMessageUserName', None)
        if self.last_message_user_name == '':
            self.last_message_user_name = None
        self.last_message = dict.get('sortLastMessage', None)
        if self.last_message == '':
            self.last_message = None
        self.last_message_created_at = dict.get('sortLastMessageCreatedAt', None)
        if self.last_message_created_at == '':
            self.last_message_created_at = None
        return self
    
    def to_dict(self):
        sort_dict = {
            'sortCreatorName': self.creator_name,
            'sortTitle': self.title,
            'sortCreatedAt': self.created_at,
            'sortLastMessageUserName': self.last_message_user_name,
            'sortLastMessage': self.last_message,
            'sortLastMessageCreatedAt': self.last_message_created_at,
        }
        sort_dict = {k: v for k, v in sort_dict.items() if v is not None and v != 'None' and v != ''}
        return sort_dict
    
    def to_and_string(self):
        and_string = ''
        if self.creator_name is not None and self.creator_name != '':
            and_string += " AND creator_name = LIKE %{}%".format(self.creator_name)
        if self.title is not None and self.title != '':
            and_string += " AND title = LIKE %{}%".format(self.title)
        if self.created_at is not None and self.created_at != '':
            and_string += " AND created_at = LIKE %{}%".format(self.created_at)
        if self.last_message_user_name is not None and self.last_message_user_name != '':
            and_string += " AND last_message_user_name = LIKE %{}%".format(self.last_message_user_name)
        if self.last_message is not None and self.last_message != '':
            and_string += " AND last_message = LIKE %{}%".format(self.last_message)
        if self.last_message_created_at is not None and self.last_message_created_at != '':
            and_string += " AND last_message_created_at = LIKE %{}%".format(self.last_message_created_at)
        
        if and_string != '':
            and_string = and_string[5:]
        return and_string