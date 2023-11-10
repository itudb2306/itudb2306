from flask import request
from models.table import Table
from typing import Any


def table_view_decorator(table_dict: str, data_class: Any = None):
    def decorator(func):
        def view_table(*args, **kwargs):
            page = request.args.get('p', default=1, type=int)
            table = Table(title=table_dict['title'], name=table_dict['name'], key=table_dict['key'], columns=table_dict['columns'], headers=table_dict['headers'], header_column_map=table_dict['header_column_map'], data_class=data_class).pagination.update(current_page=page)
            return func(table=table, *args, **kwargs)
        return view_table
    return decorator