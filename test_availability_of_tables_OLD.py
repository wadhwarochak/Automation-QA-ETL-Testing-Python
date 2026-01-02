from sql_query_running import *

def test_availability_of_tables_sales():
    assert run_sql_query_for_validation('''
        select count(*) from sales
    ''')[0][0] >=0
    ## 00 means one value



def test_availability_of_tables_customer():
    assert run_sql_query_for_validation('''
        select count(*) from customer
    ''')[0][0] >=0

def test_availability_of_tables_sales_fact():
    assert run_sql_query_for_validation('''
        select count(*) from sales_fact
    ''')[0][0] >=0

def test_availability_of_tables_products():
    assert run_sql_query_for_validation('''
        select count(*) from products
    ''')[0][0] >=0

if __name__ == "__main__":
    test_availability_of_tables_sales()
    test_availability_of_tables_sales_fact()
    test_availability_of_tables_customer()
    test_availability_of_tables_products()