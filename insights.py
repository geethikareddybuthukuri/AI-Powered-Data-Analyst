import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen2.5:7b"

def generate_insights(df):

    sample = df.head(20).to_string()

    prompt = f"""
Analyze this data:

{sample}

Provide:

1. Key Findings
2. Trends
3. Recommendations

Keep it concise.
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

    return response.json()["response"]