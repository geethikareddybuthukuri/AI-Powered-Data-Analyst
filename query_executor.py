import sqlite3
import pandas as pd

def run_query(sql):

    conn = sqlite3.connect("data.db")

    result = pd.read_sql_query(
        sql,
        conn
    )

    conn.close()

    return result