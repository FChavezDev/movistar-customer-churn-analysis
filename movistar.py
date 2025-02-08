import pyodbc
import pandas as pd
import numpy as np 

conn = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=FERNANDO\MSSQLSERVER02;DATABASE=bd_movistar;Trusted_Connection=yes')
query = '''

SELECT * FROM clientes_movistar;



'''
df = pd.read_sql(query, conn)
print(df)