import pyodbc

DRIVER_NAME = "SQL SERVER"
SERVER_NAME=r"LAPTOP-DUCAGQBB\SQLEXPRESS"
DATABASE_NAME="etl_testing_automation"

connection_string = f'''
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
uid="test_user"
pwd="StrongP@ssw0rd!"
'''
conn = pyodbc.connect(connection_string)
cursor=conn.cursor()