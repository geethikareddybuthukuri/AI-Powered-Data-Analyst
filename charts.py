import pandas as pd
import plotly.express as px

def create_chart(df):

    if df.empty:
        return None

    if len(df.columns) < 2:
        return None

    cols = list(df.columns)

    x = cols[0]
    y = cols[1]

    time_keywords = [
        "date",
        "month",
        "year",
        "day",
        "time",
        "timestamp"
    ]

    if any(
        keyword in x.lower()
        for keyword in time_keywords
    ):

        if len(df) == 1:

            fig = px.bar(
                df,
                x=x,
                y=y,
                title="Summary"
            )

        else:

            fig = px.line(
                df,
                x=x,
                y=y,
                markers=True,
                title="Trend Analysis"
            )

        return fig

    x_numeric = pd.api.types.is_numeric_dtype(
        df[x]
    )

    y_numeric = pd.api.types.is_numeric_dtype(
        df[y]
    )

    if x_numeric and y_numeric:

        return px.scatter(
            df,
            x=x,
            y=y,
            title="Relationship Analysis"
        )

    distribution_words = [
        "status",
        "priority",
        "category",
        "type",
        "level"
    ]

    if (
        len(df) <= 6
        and any(
            word in x.lower()
            for word in distribution_words
        )
    ):

        fig = px.pie(
            df,
            names=x,
            values=y,
            title="Distribution Analysis"
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        return fig

    if len(df) > 10:

        return px.bar(
            df,
            x=y,
            y=x,
            orientation="h",
            title="Top Categories"
        )

    return px.bar(
        df,
        x=x,
        y=y,
        title="Comparison Analysis"
    )