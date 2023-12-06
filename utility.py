from datetime import datetime

# Writes timestamp and called query.
def logQuery(query:str):
    date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    with open("query_log.txt", "a") as log_file:
        log_file.write("[%s] %s\n" % (date_time, query))

