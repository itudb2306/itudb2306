from datetime import datetime


def logQuery(query: str):
    date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    # Replace newlines and tabs with spaces
    formatted_string = query.replace('\n', ' ')
    formatted_string = formatted_string.replace('\t', ' ')
    # Replace multiple spaces with one space
    while '  ' in formatted_string:
        formatted_string = formatted_string.replace('  ', ' ')

    with open("query_log.txt", "a") as log_file:
        log_file.write("[%s] %s\n" % (date_time, formatted_string))
