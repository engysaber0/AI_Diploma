import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
# load data
DATA_PATH = "gobike_processed.csv"
df = pd.read_csv(DATA_PATH)
# design system
NAVY = "#14213D"
AMBER = "#FF9F1C"
TEAL = "#2EC4B6"
CORAL = "#FF6B6B"
BACKGROUND = "#F7F8FA"
WHITE = "#FFFFFF"
TEXT = "#14213D"
MUTED = "#5B6472"
LIGHT_BORDER = "#E6E9EF"
# dash app
app = Dash(__name__)
app.title = "Ford GoBike Dashboard"
# helper functions
def section_title(title, subtitle, accent=NAVY):
    """
    Creates a section title with a colored marker.
    """
    return html.Div(
        style={
            "marginBottom": "18px",
        },
        children=[
            html.Div(
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                    "marginBottom": "5px",
                },
                children=[
                    html.Div(
                        style={
                            "width": "5px",
                            "height": "26px",
                            "backgroundColor": accent,
                            "borderRadius": "4px",
                        }
                    ),
                    html.H2(
                        title,
                        style={
                            "margin": "0",
                            "fontFamily": "Poppins, sans-serif",
                            "fontSize": "24px",
                            "fontWeight": "700",
                            "color": NAVY,
                        },
                    ),
                ],
            ),
            html.P(
                subtitle,
                style={
                    "margin": "0 0 0 15px",
                    "fontFamily": "Inter, sans-serif",
                    "fontSize": "14px",
                    "color": MUTED,
                },
            ),
        ],
    )
def chart_card(figure):
    """
    Wraps a Plotly figure inside a white rounded card.
    """
    return html.Div(
        style={
            "backgroundColor": WHITE,
            "borderRadius": "14px",
            "padding": "18px",
            "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
            "border": f"1px solid {LIGHT_BORDER}",
            "height": "100%",
        },
        children=[
            dcc.Graph(
                figure=figure,
                config={
                    "displayModeBar": False,
                    "responsive": True,
                },
                style={
                    "height": "380px",
                },
            )
        ],
    )
def kpi_card(title, value, accent):
    """
    Creates a KPI card with a colored left border.
    """
    return html.Div(
        style={
            "backgroundColor": WHITE,
            "borderRadius": "14px",
            "padding": "20px",
            "borderLeft": f"5px solid {accent}",
            "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
            "borderTop": f"1px solid {LIGHT_BORDER}",
            "borderRight": f"1px solid {LIGHT_BORDER}",
            "borderBottom": f"1px solid {LIGHT_BORDER}",
            "minHeight": "110px",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
        },
        children=[
            html.P(
                title,
                style={
                    "margin": "0 0 8px 0",
                    "fontFamily": "Inter, sans-serif",
                    "fontSize": "13px",
                    "fontWeight": "600",
                    "color": MUTED,
                },
            ),
            html.H3(
                value,
                style={
                    "margin": "0",
                    "fontFamily": "Poppins, sans-serif",
                    "fontSize": "28px",
                    "fontWeight": "700",
                    "color": NAVY,
                },
            ),
        ],
    )
def style_figure(fig, title=None):
    """
    Applies common styling to Plotly charts.
    """
    fig.update_layout(
        title=title,
        title_font={
            "family": "Poppins, sans-serif",
            "size": 18,
            "color": NAVY,
        },
        font={
            "family": "Inter, sans-serif",
            "color": TEXT,
        },
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE,
        margin={
            "l": 45,
            "r": 25,
            "t": 55,
            "b": 45,
        },
        legend={
            "font": {
                "family": "Inter, sans-serif",
                "size": 12,
            }
        },
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="#EEF0F4",
        zeroline=False,
        linecolor="#D9DDE5",
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#EEF0F4",
        zeroline=False,
        linecolor="#D9DDE5",
    )
    return fig
def filter_df(data, user_type, genders, age_groups):
    """
    Applies dashboard filters.
    """
    filtered = data.copy()
    # user type filter
    if user_type and user_type != "All":
        if "user_type" in filtered.columns:
            filtered = filtered[
                filtered["user_type"] == user_type
            ]
    # gender filter
    if genders:
        if "member_gender" in filtered.columns:
            filtered = filtered[
                filtered["member_gender"].isin(genders)
            ]
    # age group filter
    if age_groups:
        if "age_group" in filtered.columns:
            filtered = filtered[
                filtered["age_group"].isin(age_groups)
            ]
    return filtered
# get filter options
if "user_type" in df.columns:
    user_type_options = [
        {"label": "All", "value": "All"}
    ] + [
        {
            "label": str(value),
            "value": str(value),
        }
        for value in sorted(
            df["user_type"].dropna().unique()
        )
    ]
else:
    user_type_options = [
        {
            "label": "All",
            "value": "All",
        }
    ]
if "member_gender" in df.columns:
    gender_options = [
        {
            "label": str(value),
            "value": str(value),
        }
        for value in sorted(
            df["member_gender"].dropna().unique()
        )
    ]
else:
    gender_options = []
if "age_group" in df.columns:
    age_group_options = [
        {
            "label": str(value),
            "value": str(value),
        }
        for value in sorted(
            df["age_group"].dropna().unique()
        )
    ]
else:
    age_group_options = []
# dashboard layout
app.layout = html.Div(
    style={
        "backgroundColor": BACKGROUND,
        "minHeight": "100vh",
        "fontFamily": "Inter, sans-serif",
    },
    children=[
        # header
        html.Div(
            style={
                "backgroundColor": NAVY,
                "padding": "28px 5%",
                "boxShadow": "0 2px 8px rgba(20, 33, 61, 0.15)",
            },
            children=[
                html.Div(
                    style={
                        "maxWidth": "1400px",
                        "margin": "0 auto",
                    },
                    children=[
                        html.H1(
                            "Ford GoBike Interactive Dashboard",
                            style={
                                "margin": "0",
                                "fontFamily": "Poppins, sans-serif",
                                "fontSize": "32px",
                                "fontWeight": "700",
                                "color": WHITE,
                            },
                        ),
                        html.P(
                            "Explore bike-sharing trips, users, stations, and trip duration",
                            style={
                                "margin": "7px 0 0 0",
                                "fontFamily": "Inter, sans-serif",
                                "fontSize": "15px",
                                "color": "#DCE2EC",
                            },
                        ),
                    ],
                )
            ],
        ),
        # main content
        html.Div(
            style={
                "maxWidth": "1400px",
                "margin": "0 auto",
                "padding": "35px 5% 50px 5%",
            },
            children=[
                # filters
                section_title(
                    "Filters",
                    "Use the filters below to explore the dataset",
                    AMBER,
                ),
                html.Div(
                    style={
                        "backgroundColor": WHITE,
                        "borderRadius": "14px",
                        "padding": "22px",
                        "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                        "border": f"1px solid {LIGHT_BORDER}",
                        "marginBottom": "35px",
                    },
                    children=[
                        html.Div(
                            style={
                                "display": "grid",
                                "gridTemplateColumns": "repeat(auto-fit, minmax(250px, 1fr))",
                                "gap": "25px",
                            },
                            children=[
                                # user type
                                html.Div(
                                    children=[
                                        html.Label(
                                            "User Type",
                                            style={
                                                "fontFamily": "Inter, sans-serif",
                                                "fontSize": "13px",
                                                "fontWeight": "600",
                                                "color": TEXT,
                                                "display": "block",
                                                "marginBottom": "8px",
                                            },
                                        ),
                                        dcc.Dropdown(
                                            id="user-type-filter",
                                            options=user_type_options,
                                            value="All",
                                            clearable=False,
                                            style={
                                                "fontFamily": "Inter, sans-serif",
                                            },
                                        ),
                                    ],
                                ),
                                # gender
                                html.Div(
                                    children=[
                                        html.Label(
                                            "Gender",
                                            style={
                                                "fontFamily": "Inter, sans-serif",
                                                "fontSize": "13px",
                                                "fontWeight": "600",
                                                "color": TEXT,
                                                "display": "block",
                                                "marginBottom": "10px",
                                            },
                                        ),
                                        dcc.Checklist(
                                            id="gender-filter",
                                            options=gender_options,
                                            value=[
                                                option["value"]
                                                for option in gender_options
                                            ],
                                            inline=True,
                                            inputStyle={
                                                "marginRight": "5px",
                                                "marginLeft": "8px",
                                            },
                                            labelStyle={
                                                "fontFamily": "Inter, sans-serif",
                                                "fontSize": "13px",
                                                "color": MUTED,
                                            },
                                        ),
                                    ],
                                ),
                                # age group
                                html.Div(
                                    children=[
                                        html.Label(
                                            "Age Group",
                                            style={
                                                "fontFamily": "Inter, sans-serif",
                                                "fontSize": "13px",
                                                "fontWeight": "600",
                                                "color": TEXT,
                                                "display": "block",
                                                "marginBottom": "10px",
                                            },
                                        ),
                                        dcc.Checklist(
                                            id="age-group-filter",
                                            options=age_group_options,
                                            value=[
                                                option["value"]
                                                for option in age_group_options
                                            ],
                                            inline=True,
                                            inputStyle={
                                                "marginRight": "5px",
                                                "marginLeft": "8px",
                                            },
                                            labelStyle={
                                                "fontFamily": "Inter, sans-serif",
                                                "fontSize": "13px",
                                                "color": MUTED,
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                # kpi section
                section_title(
                    "Key Metrics",
                    "A quick overview of the selected trips",
                    TEAL,
                ),
                html.Div(
                    id="kpi-container",
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "repeat(auto-fit, minmax(210px, 1fr))",
                        "gap": "18px",
                        "marginBottom": "40px",
                    },
                ),
                # user demographics
                section_title(
                    "User Demographics",
                    "Understand who is using the bike-sharing service",
                    CORAL,
                ),
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "repeat(auto-fit, minmax(350px, 1fr))",
                        "gap": "22px",
                        "marginBottom": "40px",
                    },
                    children=[
                        html.Div(
                            children=[
                                chart_card(None)
                                if False
                                else dcc.Graph(
                                    id="user-type-chart",
                                    config={
                                        "displayModeBar": False,
                                        "responsive": True,
                                    },
                                    style={
                                        "height": "380px",
                                    },
                                )
                            ],
                            style={
                                "backgroundColor": WHITE,
                                "borderRadius": "14px",
                                "padding": "18px",
                                "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                                "border": f"1px solid {LIGHT_BORDER}",
                            },
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="gender-chart",
                                    config={
                                        "displayModeBar": False,
                                        "responsive": True,
                                    },
                                    style={
                                        "height": "380px",
                                    },
                                )
                            ],
                            style={
                                "backgroundColor": WHITE,
                                "borderRadius": "14px",
                                "padding": "18px",
                                "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                                "border": f"1px solid {LIGHT_BORDER}",
                            },
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="age-group-chart",
                                    config={
                                        "displayModeBar": False,
                                        "responsive": True,
                                    },
                                    style={
                                        "height": "380px",
                                    },
                                )
                            ],
                            style={
                                "backgroundColor": WHITE,
                                "borderRadius": "14px",
                                "padding": "18px",
                                "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                                "border": f"1px solid {LIGHT_BORDER}",
                            },
                        ),
                    ],
                ),
                # station analysis
                section_title(
                    "Station Analysis",
                    "Discover the most popular starting and ending stations",
                    AMBER,
                ),
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "repeat(auto-fit, minmax(450px, 1fr))",
                        "gap": "22px",
                        "marginBottom": "40px",
                    },
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="start-stations-chart",
                                    config={
                                        "displayModeBar": False,
                                        "responsive": True,
                                    },
                                    style={
                                        "height": "420px",
                                    },
                                )
                            ],
                            style={
                                "backgroundColor": WHITE,
                                "borderRadius": "14px",
                                "padding": "18px",
                                "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                                "border": f"1px solid {LIGHT_BORDER}",
                            },
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="end-stations-chart",
                                    config={
                                        "displayModeBar": False,
                                        "responsive": True,
                                    },
                                    style={
                                        "height": "420px",
                                    },
                                )
                            ],
                            style={
                                "backgroundColor": WHITE,
                                "borderRadius": "14px",
                                "padding": "18px",
                                "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                                "border": f"1px solid {LIGHT_BORDER}",
                            },
                        ),
                    ],
                ),
                # trip duration
                section_title(
                    "Trip Duration",
                    "Explore how long users typically stay on their trips",
                    TEAL,
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            id="trip-duration-chart",
                            config={
                                "displayModeBar": False,
                                "responsive": True,
                            },
                            style={
                                "height": "450px",
                            },
                        )
                    ],
                    style={
                        "backgroundColor": WHITE,
                        "borderRadius": "14px",
                        "padding": "18px",
                        "boxShadow": "0 3px 12px rgba(20, 33, 61, 0.07)",
                        "border": f"1px solid {LIGHT_BORDER}",
                    },
                ),
            ],
        ),
    ],
)
# callback
@app.callback(
    Output("kpi-container", "children"),
    Output("user-type-chart", "figure"),
    Output("gender-chart", "figure"),
    Output("age-group-chart", "figure"),
    Output("start-stations-chart", "figure"),
    Output("end-stations-chart", "figure"),
    Output("trip-duration-chart", "figure"),
    Input("user-type-filter", "value"),
    Input("gender-filter", "value"),
    Input("age-group-filter", "value"),
)
def update_dashboard(
    user_type,
    genders,
    age_groups,
):
    # apply filters
    filtered_df = filter_df(
        df,
        user_type,
        genders,
        age_groups,
    )
    # empty data check
    if filtered_df.empty:
        empty_fig = px.scatter(
            title="No data available",
        )
        empty_fig.update_layout(
            paper_bgcolor=WHITE,
            plot_bgcolor=WHITE,
            font={
                "family": "Inter, sans-serif",
                "color": MUTED,
            },
        )
        kpis = [
            kpi_card(
                "Total Trips",
                "0",
                AMBER,
            ),
            kpi_card(
                "Avg Duration (min)",
                "0",
                TEAL,
            ),
            kpi_card(
                "Unique Bikes Used",
                "0",
                CORAL,
            ),
            kpi_card(
                "Most Popular Station",
                "N/A",
                NAVY,
            ),
        ]
        return (
            kpis,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
        )
    # kpi calculations
    total_trips = len(filtered_df)
    # average duration
    if "duration_min" in filtered_df.columns:
        avg_duration = filtered_df[
            "duration_min"
        ].mean()
    elif "duration_sec" in filtered_df.columns:
        avg_duration = (
            filtered_df["duration_sec"].mean() / 60
        )
    else:
        avg_duration = 0
    # unique bikes
    if "bike_id" in filtered_df.columns:
        unique_bikes = filtered_df[
            "bike_id"
        ].nunique()
    else:
        unique_bikes = 0
    # most popular station
    if "start_station_name" in filtered_df.columns:
        station_counts = (
            filtered_df["start_station_name"]
            .dropna()
            .value_counts()
        )
        if not station_counts.empty:
            popular_station = station_counts.index[0]
        else:
            popular_station = "N/A"
    else:
        popular_station = "N/A"
    # kpi cards
    kpis = [
        kpi_card(
            "Total Trips",
            f"{total_trips:,}",
            AMBER,
        ),
        kpi_card(
            "Avg Duration (min)",
            f"{avg_duration:.1f}",
            TEAL,
        ),
        kpi_card(
            "Unique Bikes Used",
            f"{unique_bikes:,}",
            CORAL,
        ),
        kpi_card(
            "Most Popular Station",
            str(popular_station),
            NAVY,
        ),
    ]
    # user type chart
    if "user_type" in filtered_df.columns:
        user_type_data = (
            filtered_df["user_type"]
            .value_counts()
            .reset_index()
        )
        user_type_data.columns = [
            "user_type",
            "count",
        ]
        user_type_fig = px.pie(
            user_type_data,
            names="user_type",
            values="count",
            hole=0.55,
            title="Trips by User Type",
        )
        user_type_fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Trips: %{value:,}<br>"
                "Share: %{percent}<extra></extra>"
            ),
        )
        user_type_fig.update_layout(
            colorway=[
                NAVY,
                AMBER,
                TEAL,
                CORAL,
            ],
        )
        user_type_fig = style_figure(
            user_type_fig
        )
    else:
        user_type_fig = px.scatter(
            title="User Type data unavailable"
        )
        user_type_fig = style_figure(
            user_type_fig
        )
    # gender chart
    if "member_gender" in filtered_df.columns:
        gender_data = (
            filtered_df["member_gender"]
            .dropna()
            .value_counts()
            .reset_index()
        )
        gender_data.columns = [
            "gender",
            "count",
        ]
        gender_fig = px.bar(
            gender_data,
            x="gender",
            y="count",
            title="Trips by Gender",
            text="count",
        )
        gender_fig.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
        )
        gender_fig.update_layout(
            showlegend=False,
        )
        gender_fig = style_figure(
            gender_fig
        )
    else:
        gender_fig = px.scatter(
            title="Gender data unavailable"
        )
        gender_fig = style_figure(
            gender_fig
        )
    # age group chart
    if "age_group" in filtered_df.columns:
        age_data = (
            filtered_df["age_group"]
            .dropna()
            .value_counts()
            .reset_index()
        )
        age_data.columns = [
            "age_group",
            "count",
        ]
        age_fig = px.bar(
            age_data,
            x="age_group",
            y="count",
            title="Trips by Age Group",
            text="count",
        )
        age_fig.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
        )
        age_fig.update_layout(
            showlegend=False,
        )
        age_fig = style_figure(
            age_fig
        )
    else:
        age_fig = px.scatter(
            title="Age Group data unavailable"
        )
        age_fig = style_figure(
            age_fig
        )
    # top start stations
    if "start_station_name" in filtered_df.columns:
        start_station_data = (
            filtered_df["start_station_name"]
            .dropna()
            .value_counts()
            .head(10)
            .sort_values()
            .reset_index()
        )
        start_station_data.columns = [
            "station",
            "count",
        ]
        stations_fig = px.bar(
            start_station_data,
            x="count",
            y="station",
            orientation="h",
            title="Top 10 Start Stations",
            text="count",
        )
        stations_fig.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
        )
        stations_fig.update_layout(
            showlegend=False,
        )
        stations_fig = style_figure(
            stations_fig
        )
    else:
        stations_fig = px.scatter(
            title="Start Station data unavailable"
        )
        stations_fig = style_figure(
            stations_fig
        )
    # top end stations
    if "end_station_name" in filtered_df.columns:
        end_station_data = (
            filtered_df["end_station_name"]
            .dropna()
            .value_counts()
            .head(10)
            .sort_values()
            .reset_index()
        )
        end_station_data.columns = [
            "station",
            "count",
        ]
        end_stations_fig = px.bar(
            end_station_data,
            x="count",
            y="station",
            orientation="h",
            title="Top 10 End Stations",
            text="count",
        )
        end_stations_fig.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
        )
        end_stations_fig.update_layout(
            showlegend=False,
        )
        end_stations_fig = style_figure(
            end_stations_fig
        )
    else:
        end_stations_fig = px.scatter(
            title="End Station data unavailable"
        )
        end_stations_fig = style_figure(
            end_stations_fig
        )
    # trip duration histogram
    if "duration_min" in filtered_df.columns:
        duration_column = "duration_min"
    elif "duration_sec" in filtered_df.columns:
        filtered_df = filtered_df.copy()
        filtered_df["duration_min"] = (
            filtered_df["duration_sec"] / 60
        )
        duration_column = "duration_min"
    else:
        duration_column = None
    if duration_column:
        duration_fig = px.histogram(
            filtered_df,
            x=duration_column,
            nbins=40,
            title="Trip Duration Distribution",
        )
        duration_fig.update_layout(
            xaxis_title="Trip Duration (minutes)",
            yaxis_title="Number of Trips",
            showlegend=False,
        )
        duration_fig = style_figure(
            duration_fig
        )
    else:
        duration_fig = px.scatter(
            title="Trip Duration data unavailable"
        )
        duration_fig = style_figure(
            duration_fig
        )
    # return all dashboard components
    return (
        kpis,
        user_type_fig,
        gender_fig,
        age_fig,
        stations_fig,
        end_stations_fig,
        duration_fig,
    )
# run app
if __name__ == "__main__":
    app.run(
        debug=True
    )