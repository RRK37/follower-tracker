# app.py
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import os

# CSV file
CSV_FILE = "/data/followers.csv"

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Instagram Followers Tracker"

# App layout
app.layout = html.Div(
    style={"font-family": "Arial, sans-serif", "text-align": "center", "padding": "20px"},
    children=[
        html.H1("Instagram Followers Over Time", style={"color": "#333"}),
        dcc.Graph(id="followers-graph"),
        dcc.Interval(
            id="interval-component",
            interval=10*1000,  # 10 seconds in milliseconds
            n_intervals=0
        ),
        html.P("Auto-updates every 10 seconds", style={"color": "#666", "font-size": "12px"})
    ]
)

# Callback to update the graph
@app.callback(
    Output("followers-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_graph(n):
    # Load CSV
    try:
        df = pd.read_csv(CSV_FILE, parse_dates=["time_and_date"])
    except FileNotFoundError:
        return px.line(title="No data found")

    # Sort by datetime
    df = df.sort_values("time_and_date")

    # Keep only the last 30 days
    last_30_days = df[df["time_and_date"] >= pd.Timestamp.now() - pd.Timedelta(days=30)]

    # Plotly line chart
    fig = px.line(
        last_30_days,
        x="time_and_date",
        y="count",
        title="Followers Over Last 30 Days",
        labels={"time_and_date": "Date & Time", "count": "Followers"},
        template="plotly_dark"  # sleek dark theme
    )
    fig.update_traces(mode="lines+markers", line=dict(width=3, color="#00cc96"))
    fig.update_layout(
        xaxis=dict(showgrid=True, gridcolor="#444"),
        yaxis=dict(showgrid=True, gridcolor="#444"),
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font=dict(color="#fff")
    )
    return fig

# Run the app
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=False)