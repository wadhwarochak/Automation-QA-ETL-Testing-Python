import pytest

from framework_etl_testing import extract_columns_from_tables_in_list_form, extract_columns_from_mapping_doc
from sql_query_running import *


@pytest.mark.parametrize('tables',
                         [
                             'sales',
                             'date_dim',
                             'customer',
                             'products',
                             'sales_fact',
                             'sales_agg'
                         ]
                         )
def test_availability_of_tables(tables):
    assert run_sql_query_for_validation(f'''
    select count(*) from {tables}
    ''')[0][0] >= 0


@pytest.mark.parametrize('tables',
                         [
                             'sales',
                             'date_dim',
                             'customer',
                             'products',
                             'sales_fact',
                             'sales_agg'
                         ]
                         )
def test_presence_of_records_in_tables(tables):
    assert run_sql_query_for_validation(f'''
select count(*) from {tables}
''')[0][0] >= 1


@pytest.mark.parametrize('tables',
                         [
                             'sales_fact',
                             'sales_agg'
                         ]
                         )
def test_column_names_in_tables(tables):
    assert (sorted(extract_columns_from_tables_in_list_form(tables)) ==
            sorted(extract_columns_from_mapping_doc(tables)))


@pytest.mark.parametrize('primary_key, table_name',
                         [
                             ('sales_id', 'sales'),
                             ('sales_id', 'sales_fact'),
                             ('customer_id', 'sales_agg'),
                             ('date_id', 'date_dim'),
                             ('customer_id', 'customer'),
                             ('product_id', 'products')
                         ]
                         )
def test_duplicate_records_on_the_basis_of_primary_key(primary_key, table_name):
    assert run_sql_query_for_validation(f'''
    select {primary_key}, count(*) from {table_name}
    group by {primary_key}
    having count(*) > 1
''') == []


@pytest.mark.parametrize('source_column, source_table, target_column, target_table',
                         [
                             ('sales_id', 'sales', 'sales_id', 'sales_fact'),
                             ('date_id', 'date_dim', 'date_id', 'sales_fact'),
                             ('customer_id', 'customer', 'customer_id', 'sales_fact'),
                             ('product_id', 'products', 'product_id', 'sales_fact'),
                             ('purchase_quantity', 'sales', 'quantity', 'sales_fact'),
                             ('per_unit_price', 'sales', 'unit_price', 'sales_fact'),
                             ('customer_id', 'customer', 'customer_id', 'sales_agg')
                         ]

                         )
def test_to_ensure_no_records_are_dropped(source_column, source_table, target_column, target_table):
    assert run_sql_query_for_validation(f'''
    select distinct {source_column} from {source_table}
    ''') == run_sql_query_for_validation(f'''
    select distinct {target_column} from {target_table}
    ''')


@pytest.mark.parametrize('sales_id',
                         [
                             40001,
                             40002,
                             40003,
                             40018,
                             40019
                         ])
def test_population_of_the_column_total_revenue_sales_fact(sales_id):
    assert run_sql_query_for_validation(f'''
	 select total_revenue from sales_fact
	 where sales_id = {sales_id}
    ''')[0][0] == run_sql_query_for_validation(f'''
    select purchase_quantity*per_unit_price from sales
	 where sales_id = {sales_id}
    ''')[0][0]


@pytest.mark.parametrize('customer_id',
                         [
                             700123,
                             700124,
                             700138,
                             700139
                         ]
                         )
def test_population_total_quantity_sales_agg(customer_id):
    assert run_sql_query_for_validation(f'''
     select total_quantity from sales_agg
	 where customer_id = {customer_id}
    ''')[0][0] == run_sql_query_for_validation(f'''
     select coalesce(sum(quantity), 0) from sales_fact
	 where customer_id = {customer_id}
    ''')[0][0]


@pytest.mark.parametrize('customer_id',
                         [
                             700127,
                             700128,
                             700136,
                             700137
                         ]
                         )
def test_population_total_revenue_sales_agg(customer_id):
    assert run_sql_query_for_validation(f'''
     select total_revenue from sales_agg
	 where customer_id = {customer_id}
    ''')[0][0] == run_sql_query_for_validation(f'''
     select coalesce(sum(total_revenue), 0) from sales_fact
	 where customer_id = {customer_id}
    ''')[0][0]


def test_population_of_the_table_sales_agg():
    assert run_sql_query_for_validation('''
    select * from sales_agg
    ''') == run_sql_query_for_validation('''
    select customer_id, coalesce(sum(quantity), 0), coalesce(sum(total_revenue), 0)
    from sales_fact
    group by customer_id
    ''')