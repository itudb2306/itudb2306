from dataclasses import dataclass
from typing import Any, List, Optional

from database import Query
from database import db
from config import RECORDS_PER_PAGE



@dataclass
class Pagination:
    table: Any = None
    current_page: int = 1
    total_pages: int = 1
    records_per_page: int = RECORDS_PER_PAGE

    @property
    def offset(self):
        return (self.current_page - 1) * self.records_per_page
    
    @property
    def limit(self):
        return self.records_per_page
    
    def update(self, current_page: int = None, total_pages: int = None, records_per_page: int = None):
        if current_page is not None:
            print("current_page:", current_page)
            self.current_page = current_page
        if total_pages is not None:
            self.total_pages = total_pages
        if records_per_page is not None:
            self.records_per_page = records_per_page

        return self.table
    
@dataclass
class Search:
    pass

@dataclass
class Sort:
    pass

@dataclass
class Filter:
    pass

@dataclass
class Table:
    """
    A dataclass that represents a table in the database.
    """
    name: str
    title: str
    key: str # Primary key, for the operations that require it such as UPDATE and DELETE
    columns: List[str]
    headers: List[str]
    header_column_map: dict
    data_class: Any = None
    records: List[Any] = None
    """
    Table attributes that are large enough to be considered a class of their own are implemented as subclasses of Table. "Pagination", "Search", "Sort", and "Filter" are subclasses of Table. Their operations must return the table itself. So, the operations can be chained together (as in Query Builder). While adding a new subclass, add a table attribute to that subclass, and set the attribute to the table itself in the __post_init__ method.
    """
    pagination: Pagination = Pagination()
    search: Optional[Search] = None
    sort: Optional[Sort] = None
    filter: Optional[Filter] = None

    def __post_init__(self):
        self.query = Query()
        self.query_prefix_flag = False
        self.query_full_flag = False
        self.total_pages_query = Query().SELECT('COUNT(*)').FROM(self.name).BUILD()
        self.total_pages = 1
        self.records = []
        self.pagination.table = self # Set the table attribute of the subclasses to the table itself
        self.column_index_map = {column: index for index, column in enumerate(self.columns)}
    
    """
    TODO: Functions in dataclasses are not Pythonic(?). Find a better way to implement these functions.
    """
    
    def custom_query_prefix(self, query: Query):
        self.query = query
        self.query_prefix_flag = True
        return self
    
    def custom_query(self, query: Query):
        self.query = query
        self.query_full_flag = True
        return self

    def fetch_records(self):
        if self.query_prefix_flag:
            query = self.query.LIMIT(self.pagination.offset, self.pagination.limit).BUILD()

        elif self.query_full_flag:
            query = self.query.BUILD()

        else:
            query = Query().SELECT(", ".join(self.columns)).FROM(self.name).LIMIT(self.pagination.offset, self.pagination.limit).BUILD()

        print("Query: ", query)

        result = db.fetchall(query)
        self.records = []
        for row in result:
            self.records.append(self.data_class.from_list(row))

    def fetch_total_pages(self):
        self.pagination.total_pages = db.fetchone(self.total_pages_query)[0] // self.pagination.records_per_page + 1
    
    def construct(self):
        self.fetch_records()
        self.fetch_total_pages()
        print("Total Pages Query: ", self.total_pages_query)
        print("records[0]: ", self.records[0])
        print("len(records): ", len(self.records))
        return self
