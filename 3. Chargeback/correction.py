import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def query(conn, file, args=None, df=True):
    with open(file, 'r') as file:
        sqlcmd = file.read()    
    result = pd.DataFrame() if df else None
    try:
        if df:
            result = pd.read_sql_query(sqlcmd, conn, params=args)
        else:
            result = conn.execute(sqlcmd, args).fetchall()
            result = result[0] if len(result) == 1 else result
    except Exception as e:
        print("Error encountered: ", e, sep='\n')
    return result

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/postgres', echo=False)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="password"
)

df = pd.read_csv('whatever.csv')
to_be_corrected = df['whateve'].unique()

for item in to_be_corrected:
    # if no cheque then 
    # run sql code
        # find from creditors the count to skip
        # how many cheques there are
        # get latest cheque (Payment)
        # if debtors date falls before 1st jan 2023 then ignore
        # ignore values of 0 for debtors and get remaining rows
        # go back into df and check how many corresponding items there are and make sure they match
        # need to make a receipt for each line
    to_skip = """
                SELECT COUNT(supplier)
                FROM creditors
                WHERE item = {} AND "how many cheques there are"
              """.format(item)

    temp = query(conn,
               """
               SELECT *
               FROM debtors
               WHERE item = {}
               """.format(item))

    temp = temp.iloc[to_skip:]

