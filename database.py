import mysql.connector
from config import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.cursor = self.db.cursor()

    
    def fetchone(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetchall(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


db = Database()


class Query:
    def __init__(self):
        self._SELECT = ''
        self._FROM = ''
        self._WHERE = ''
        self._LIKE = ''
        self._LIMIT = ''
        
    def _create_statements(self):
        self.statements = [self._SELECT, self._FROM, self._WHERE, self._LIKE, self._LIMIT]

    def SELECT(self, selection):
        if selection == '':
            return self
        
        self._SELECT += ', ' if self._SELECT != '' else 'SELECT '
        self._SELECT += selection
        return self
    
    def FROM(self, table_name):
        if table_name == '':
            return self
        
        self._FROM += ', ' if self._FROM != '' else 'FROM '
        self._FROM += table_name
        return self

    def WHERE(self, statement):
        if statement == '':
            return self
        
        self._WHERE += 'AND ' if self._WHERE != '' else 'WHERE '
        self._WHERE += statement
        return self
    
    def LIKE(self, statement):
        if statement == '':
            return self
        
        self._LIKE += 'AND ' if self._LIKE != '' else 'LIKE '
        self._LIKE += statement
        return self
    
    def LIMIT(self, start, total):
        if start == '':
            return self
        
        self._LIMIT += 'LIMIT %s, %s' % (start, total)
        return self
    
    def BUILD(self):
        self._create_statements()
        query = ' '.join(self.statements)
        return query