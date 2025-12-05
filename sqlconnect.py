#connecting postgres sql to vscode remotly
import pandas as pd
#import psycopg2
#db_url = 'postgresql://postgres.ygovampqecciczyfchsw:Dinesh220033@aws-1-ap-south-1.pooler.supabase.com:5432/postgres'
#conn = psycopg2.connect(db_url)
#df = pd.read_sql("select * from public.products",conn)
#print(df)

#connecting to mysql workbench

import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Dinesh@2003',
    database='salesdb'
)
df = pd.read_sql('select * from customers', conn)
print(df)



