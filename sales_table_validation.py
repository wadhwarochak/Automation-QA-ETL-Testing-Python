import pytest
from sql_query_running import *

@pytest.mark.parametrize('tables',
                         [
                             'sales',
                             'customer',
                             'products',
                             'sales_fact'
                         ]
                         )

def test_availability_of_tables(tables):
    assert run_sql_query_for_validation(f'''
        select count(*) from {tables}
    ''')[0][0] >=0
    ## 00 means one value

def test_presence_of_records_in_tables(tables):
    assert run_sql_query_for_validation(f'''
        select count(*) from {tables}
    ''')[0][0] >=1

if __name__ == "__main__":
    test_availability_of_tables()
    test_presence_of_records_in_tables()