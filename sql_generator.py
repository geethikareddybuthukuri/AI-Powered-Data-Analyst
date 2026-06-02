import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:7b"

def generate_sql(
    question,
    columns,
    table_name
):

    prompt = f"""
You are an expert SQLite developer.

Table Name:
{table_name}

Columns:
{columns}

Rules:
1. Return ONLY executable SQL.
2. No markdown.
3. No explanation.
4. No comments.
5. Use SQLite syntax.

Question:
{question}
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    sql = response.json()["response"]

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql