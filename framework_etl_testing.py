from sql_query_running import run_sql_query_for_validation
import pandas as pd


def extract_columns_from_tables_in_list_form(table):
    raw_column_list = run_sql_query_for_validation(f'''
    select column_name
    from information_schema.columns
    where table_name = '{table}'
''')
    column_list = []
    for items in raw_column_list:
        column_list.append(items[0])
    return column_list


def extract_columns_from_mapping_doc(tab_name):
    column_list_raw = pd.read_excel("Mapping_Doc_ETL_Testing_Automation.xlsx", sheet_name=tab_name)
    column_list = column_list_raw['Target Column'].tolist()
    return column_list
