import pandas as pd
import sqlite3

def save_to_database(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif filename.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file type")

    conn = sqlite3.connect("data.db")

    table_name = "user_data"

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    return df, table_name