# AI-Powered Data Analyst

An AI-powered analytics platform that allows users to upload CSV or Excel files and ask questions in natural language.

The application uses a locally deployed Qwen2.5 Large Language Model through Ollama to convert user questions into SQL queries, execute them on a SQLite database, generate visualizations, and provide AI-generated insights.

## Features

* Upload CSV and Excel datasets
* Natural Language to SQL
* SQLite query execution
* KPI Cards
* Automatic chart generation
* AI-generated insights
* Download query results
* Local LLM integration using Ollama
* No external API dependency

## Tech Stack

* Python
* Streamlit
* SQLite
* Pandas
* Plotly
* Ollama
* Qwen2.5

## Architecture

Upload Dataset
↓
SQLite Database
↓
Qwen2.5 (Ollama)
↓
SQL Generation
↓
Query Execution
↓
Visualization
↓
AI Insights

## Installation

```bash
git clone <repository-url>
cd AI_Data_Analyst

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

## Example Questions

* Show total number of records
* Show distribution of task status
* Show count of tasks by process name
* Show average pending age by process
* Show top 10 organizational units by task count


