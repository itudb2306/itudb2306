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

    def execute(self, query, params=None):
        if params is not None:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.db.commit()

    def checkTableExists(self, table_name: str) -> bool:
        # placeholder is used for injection attacks
        exists_query = """
        select count(*) = 1 
        from information_schema.tables 
        where table_name = %s;
        """
        self.cursor.execute(exists_query, (table_name, ))
        return_value = self.cursor.fetchone()[0]
        return bool(return_value)


db = Database()


class Query:
    def __init__(self):
        self._SELECT = ''
        self._UPDATE = ''
        self._SET = ''
        self._FROM = ''
        self._WHERE = ''
        self._LIKE = ''
        self._ORDER_BY = ''
        self._LIMIT = ''
        self._PARAMS = []

    def _create_statements(self):
        self.statements = [self._SELECT, self._UPDATE, self._SET, self._FROM,
                           self._WHERE, self._LIKE, self._ORDER_BY, self._LIMIT]

    def SELECT(self, selection):
        if selection == '':
            return self

        self._SELECT += ', ' if self._SELECT != '' else 'SELECT '
        self._SELECT += selection
        return self

    def UPDATE(self, table_name=''):
        if table_name == '' or type(table_name) != str or self._UPDATE != '':
            return self

        self._UPDATE += 'UPDATE '
        self._UPDATE += table_name
        return self

    def SET(self, col_val_pairs={}):
        # To accept col val pairs as a string
        if isinstance(col_val_pairs, str):
            if col_val_pairs == '':
                return self
            self._SET += ', ' if self._SET != '' else 'SET '
            self._SET += col_val_pairs
            return self

        if not col_val_pairs or not isinstance(col_val_pairs, dict):
            return self

        self._SET += ', ' if self._SET != '' else 'SET '

        set_query = '%s = %s, '

        for col, val in col_val_pairs.items():
            if val is None or val == 'None' or val == '':
                set_query_with_none = '%s = NULL, '
                self._SET += set_query_with_none % col
            else:
                # Use parameterized queries to prevent SQL injection
                set_query_param = '%s = %s, '
                self._SET += set_query_param % (col, '%s')
                self._PARAMS.append(val)

        self._SET = self._SET[:-2]
        print(self._PARAMS)
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

    def ORDER_BY(self, statement):
        if statement == '':
            return self

        self._ORDER_BY += 'AND ' if self._ORDER_BY != '' else 'ORDER BY '
        self._ORDER_BY += statement
        return self

    def LIMIT(self, start, total):
        if start == '':
            return self

        self._LIMIT += 'LIMIT %s, %s' % (start, total)
        return self

    def JOIN(self, table_name, condition):
        if table_name == '' or condition == '':
            return self

        self._FROM += 'JOIN %s ON %s ' % (table_name, condition)
        return self

    def BUILD(self):
        self._create_statements()
        query = ' '.join(self.statements)
        return query
