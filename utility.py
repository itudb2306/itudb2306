from datetime import datetime
from flask import render_template

# Writes timestamp and called query.


def logQuery(query: str):
    date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    with open("query_log.txt", "a") as log_file:
        log_file.write("[%s] %s\n" % (date_time, query))


def exceptionPage(e: Exception):
    return render_template('error.html', error_type=type(e).__name__, error_message=str(e))
