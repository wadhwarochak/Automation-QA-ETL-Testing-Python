from sql_query_running import *

def test_availability_of_tables():
    assert run_sql_query_for_validation('''
        select count(*) from sales
    ''')