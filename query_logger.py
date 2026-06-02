import pandas as pd
from datetime import datetime

def log_query(question, sql):

    record = pd.DataFrame([{
        "timestamp": datetime.now(),
        "question": question,
        "sql": sql
    }])

    try:

        old = pd.read_csv(
            "query_history.csv"
        )

        record = pd.concat(
            [old, record]
        )

    except:

        pass

    record.to_csv(
        "query_history.csv",
        index=False
    )