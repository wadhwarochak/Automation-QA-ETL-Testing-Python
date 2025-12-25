from connection_to_database import *

def run_sql_query_for_validation(sql_query_to_be_run):
    cursor.execute(sql_query_to_be_run)
    print("===============================================")
    print(f"Running SQL Query: {sql_query_to_be_run}")
    print("------------------------------------------------")
    print("End of the query")
    data = cursor.fetchall()
    return data