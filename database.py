import mysql.connector
from config import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
from logger import logQuery


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        self.cursor = self.db.cursor()

    def fetchoneProc(self, query, params=None):
        if params is not None:
            logged_procedure = f"CALL {
                query}({', '.join(['%s'] * len(params))})"
            logQuery(logged_procedure % params)
            self.cursor.callproc(query, params)
        else:
            logged_procedure = f"CALL {query}()"
            logQuery(logged_procedure)
            self.cursor.callproc(query)
        return self.cursor.fetchone()

    def fetchallProc(self, query, params=None):
        if params is not None:
            logged_procedure = f"CALL {
                query}({', '.join(['%s'] * len(params))})"
            logQuery(logged_procedure % params)
            self.cursor.callproc(query, params)
        else:
            logged_procedure = f"CALL {query}()"
            logQuery(logged_procedure)
            self.cursor.callproc(query)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        if params is not None:
            logQuery(query % params)
            self.cursor.execute(query, params)
        else:
            logQuery(query)
            self.cursor.execute(query)
        return self.cursor.fetchone()

    def fetchall(self, query, params=None):
        if params is not None:
            logQuery(query % params)
            self.cursor.execute(query, params)
        else:
            logQuery(query)
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query, params=None):
        if params is not None:
            logQuery(query % params)
            self.cursor.execute(query, params)
        else:
            logQuery(query)
            self.cursor.execute(query)
        self.db.commit()

    def checkTableExists(self, table_name: str) -> bool:
        # placeholder is used for injection attacks
        exists_query = """
        select count(*) = 1 
        from information_schema.tables 
        where table_name = %s;
        """
        logQuery(exists_query % table_name)
        self.cursor.execute(exists_query, (table_name, ))
        return_value = self.cursor.fetchone()[0]
        return bool(return_value)


db = Database()


class Query:
    def __init__(self):
        self._SELECT = ''
        self._UPDATE = ''
        self._INSERT_INTO = ''
        self._VALUES = ''
        self._SET = ''
        self._FROM = ''
        self._WHERE = ''
        self._LIKE = ''
        self._ORDER_BY = ''
        self._LIMIT = ''
        self._DELETE = ''
        self._INSERT_INTO = ''
        self._VALUES = ''
        self._PARAMS = []

    def _create_statements(self):
        self.statements = [self._SELECT, self._UPDATE,  self._DELETE, self._INSERT_INTO, self._SET, self._FROM,
                           self._WHERE, self._LIKE, self._ORDER_BY, self._LIMIT, self._VALUES]

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

    def INSERT_INTO(self, table_name='', fields=[]):
        if table_name == '' or not fields or not isinstance(fields, list) or self._INSERT_INTO != '':
            return self

        self._INSERT_INTO += 'INSERT INTO '
        self._INSERT_INTO += table_name
        self._INSERT_INTO += ' ('
        for field in fields:
            self._INSERT_INTO += '%s, ' % field
        self._INSERT_INTO = self._INSERT_INTO[:-2]
        self._INSERT_INTO += ') '
        return self

    def VALUES(self, *args):
        if not args or not isinstance(args, tuple):
            return self

        self._VALUES += 'VALUES ('
        for arg in args:
            self._VALUES += '%s, '
            self._PARAMS.append(arg)
        self._VALUES = self._VALUES[:-2]
        self._VALUES += ')'
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

    def DELETE(self):
        self._DELETE = 'DELETE '
        return self

    def INSERT_INTO(self, table_name):
        self._INSERT_INTO = 'INSERT INTO %s ' % table_name
        return self

    def VALUES(self, col_val_pairs={}):
        if not col_val_pairs or not isinstance(col_val_pairs, dict):
            return self

        self._VALUES = 'VALUES ('
        for col, val in col_val_pairs.items():
            if val is None or val == 'None' or val == '':
                set_query_with_none = 'NULL, '
                self._VALUES += set_query_with_none
            else:
                # Use parameterized queries to prevent SQL injection
                set_query_param = '%s, '
                self._VALUES += set_query_param % ('%s')
                self._PARAMS.append(val)

        self._VALUES = self._VALUES[:-2]
        self._VALUES += ')'
        return self

    def INSERT_INTO_MANUAL(self, table_name, col_val_pairs):
        if not col_val_pairs or not isinstance(col_val_pairs, dict):
            return self

        if not table_name or not isinstance(table_name, str):
            return self

        column_string = '('
        values_string = ' VALUES ('

        empty = [None, 'None', '', ' ']
        for col, val in col_val_pairs.items():
            if val not in empty:
                column_string += '%s, ' % col
                values_string += '%s, '
                self._PARAMS.append(val)

        column_string = column_string[:-2]
        values_string = values_string[:-2]
        column_string += ')'
        values_string += ')'

        self._INSERT_INTO = 'INSERT INTO %s %s' % (table_name, column_string)
        self._VALUES = values_string
        return self
