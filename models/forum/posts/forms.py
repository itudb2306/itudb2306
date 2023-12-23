


class UpdateForm:
    def __init__(self, id=None, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content

    def from_dict(self, dict):
        self.id = dict.get('postID', None)
        if self.id is None:
            raise Exception("postID is required")
        self.title = dict.get('title', None)
        self.content = dict.get('content', None)
        return self
    
    def to_dict(self):
        return {
            'postID': self.id,
            'title': self.title,
            'content': self.content,
        }
    
    def to_tuple(self):
        tuple = ()

        if self.id is not None and self.id != '':
            tuple += (self.id,)
        if self.title is not None and self.title != '':
            tuple += (self.title,)
        if self.content is not None and self.content != '':
            tuple += (self.content,)

        return tuple
    