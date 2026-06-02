import streamlit as st

from database import save_to_database
from sql_generator import generate_sql
from query_executor import run_query
from charts import create_chart
from insights import generate_insights
from query_logger import log_query

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="AI Powered Data Analyst",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🤖 AI Data Analyst")

st.sidebar.info(
    """
    Features

    ✅ CSV Upload
    ✅ Excel Upload
    ✅ Natural Language Queries
    ✅ SQL Generation (Ollama)
    ✅ KPI Cards
    ✅ Auto Charts
    ✅ AI Insights
    ✅ Download Results
    """
)

# --------------------------------------------------
# Main Title
# --------------------------------------------------

st.title("🤖 AI Powered Data Analyst")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# --------------------------------------------------
# Main Logic
# --------------------------------------------------

if uploaded_file is not None:

    try:

        # Save uploaded file to database

        df, table_name = save_to_database(
            uploaded_file
        )

        st.success(
            "Dataset uploaded successfully!"
        )

        # Dataset Preview

        with st.expander(
            "Dataset Preview"
        ):
            st.dataframe(
                df.head()
            )

        # Dataset Metrics

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            df.shape[0]
        )

        col2.metric(
            "Columns",
            df.shape[1]
        )

        col3.metric(
            "Table",
            table_name
        )

        # Question Input

        question = st.text_input(
            "Ask your question"
        )

        # Generate Analysis

        if st.button(
            "Generate Analysis"
        ):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                # ----------------------------------
                # Generate SQL
                # ----------------------------------

                with st.spinner(
                    "Generating SQL..."
                ):

                    columns = ", ".join(
                        df.columns
                    )

                    sql = generate_sql(
                        question,
                        columns,
                        table_name
                    )

                # Save query history

                log_query(
                    question,
                    sql
                )

                # Show SQL

                st.subheader(
                    "Generated SQL"
                )

                st.code(
                    sql,
                    language="sql"
                )

                # ----------------------------------
                # Execute Query
                # ----------------------------------

                with st.spinner(
                    "Executing Query..."
                ):

                    result = run_query(
                        sql
                    )

                # ----------------------------------
                # Results
                # ----------------------------------

                st.subheader(
                    "Results"
                )

                st.dataframe(
                    result,
                    use_container_width=True
                )

                # ----------------------------------
                # KPI Detection
                # ----------------------------------

                is_kpi = (
                    len(result) == 1
                    and len(result.columns) >= 1
                )

                if is_kpi:

                    st.subheader(
                        "Key Metrics"
                    )

                    metric_columns = st.columns(
                        len(result.columns)
                    )

                    for i, col in enumerate(
                        result.columns
                    ):

                        metric_columns[i].metric(
                            label=col.replace(
                                "_",
                                " "
                            ).title(),
                            value=result.iloc[0][col]
                        )

                # ----------------------------------
                # Download Button
                # ----------------------------------

                csv = result.to_csv(
                    index=False
                )

                st.download_button(
                    label="📥 Download Results",
                    data=csv,
                    file_name="results.csv",
                    mime="text/csv"
                )

                # ----------------------------------
                # Visualization
                # ----------------------------------

                if (
                    not is_kpi
                    and len(result.columns) > 1
                ):

                    fig = create_chart(
                        result
                    )

                    if fig is not None:

                        st.subheader(
                            "Visualization"
                        )

                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                # ----------------------------------
                # AI Insights
                # ----------------------------------

                st.subheader(
                    "AI Insights"
                )

                try:

                    insights = generate_insights(
                        result
                    )

                    st.write(
                        insights
                    )

                except Exception as e:

                    st.warning(
                        f"Unable to generate insights: {str(e)}"
                    )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )