"""
=========================================================
Reusable Plotly Chart Components
AI Powered Car Price Prediction System
=========================================================
"""

from __future__ import annotations

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

# =====================================================
# DEFAULT LAYOUT
# =====================================================

DEFAULT_HEIGHT = 420


def apply_layout(fig, title=None):
    """
    Apply a consistent layout to Plotly charts.
    """
    fig.update_layout(
        template="plotly_white",
        height=DEFAULT_HEIGHT,
        margin=dict(l=20, r=20, t=60, b=20),
        title=title,
        legend_title="",
        font=dict(
            family="Segoe UI",
            size=13
        ),
        hovermode="x unified"
    )

    return fig


# =====================================================
# KPI GAUGE CHART
# =====================================================

def gauge_chart(
    value: float,
    maximum: float,
    title="Estimated Price"
):
    """
    Gauge chart for displaying predicted price.
    """

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,

            number={
                "prefix": "₹ "
            },

            title={
                "text": title
            },

            gauge={

                "axis": {
                    "range": [0, maximum]
                },

                "bar": {
                    "color": "#2563EB"
                },

                "steps": [

                    {
                        "range": [0, maximum*0.25],
                        "color": "#D1FAE5"
                    },

                    {
                        "range": [maximum*0.25, maximum*0.50],
                        "color": "#FEF3C7"
                    },

                    {
                        "range": [maximum*0.50, maximum*0.75],
                        "color": "#FDE68A"
                    },

                    {
                        "range": [maximum*0.75, maximum],
                        "color": "#FECACA"
                    }

                ]
            }
        )
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# CONFIDENCE DONUT
# =====================================================

def confidence_chart(confidence=96):
    """
    Donut chart showing prediction confidence.
    """

    fig = px.pie(

        names=[
            "Confidence",
            "Uncertainty"
        ],

        values=[
            confidence,
            100-confidence
        ],

        hole=.65

    )

    apply_layout(
        fig,
        "Prediction Confidence"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# BAR CHART
# =====================================================

def bar_chart(
    df,
    x,
    y,
    title="Bar Chart",
    color=None
):
    """
    Generic reusable bar chart.
    """

    fig = px.bar(

        df,

        x=x,

        y=y,

        color=color,

        text_auto=True

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# LINE CHART
# =====================================================

def line_chart(
    df,
    x,
    y,
    title="Line Chart"
):
    """
    Generic reusable line chart.
    """

    fig = px.line(

        df,

        x=x,

        y=y,

        markers=True

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# AREA CHART
# =====================================================

def area_chart(
    df,
    x,
    y,
    title="Area Chart"
):
    """
    Area chart.
    """

    fig = px.area(

        df,

        x=x,

        y=y

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# SIMPLE METRIC TREND
# =====================================================

def trend_chart(
    values,
    title="Trend"
):
    """
    Simple trend visualization.
    """

    df = pd.DataFrame({

        "Index": range(len(values)),

        "Value": values

    })

    fig = px.line(

        df,

        x="Index",

        y="Value",

        markers=True

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# DISPLAY DATAFRAME
# =====================================================

def dataframe_view(df):
    """
    Beautiful dataframe viewer.
    """

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

# =====================================================
# HISTOGRAM
# =====================================================

def histogram_chart(
    df,
    column,
    bins=30,
    title="Distribution"
):
    """
    Histogram for numerical feature distribution.
    """

    fig = px.histogram(
        df,
        x=column,
        nbins=bins
    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# PIE CHART
# =====================================================

def pie_chart(
    df,
    names,
    values=None,
    title="Pie Chart"
):
    """
    Generic Pie Chart
    """

    if values:

        fig = px.pie(
            df,
            names=names,
            values=values,
            hole=.55
        )

    else:

        counts = (
            df[names]
            .value_counts()
            .reset_index()
        )

        counts.columns = [
            names,
            "Count"
        ]

        fig = px.pie(
            counts,
            names=names,
            values="Count",
            hole=.55
        )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# SCATTER CHART
# =====================================================

def scatter_chart(
    df,
    x,
    y,
    color=None,
    title="Scatter Plot"
):
    """
    Scatter plot.
    """

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color
    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# BOX PLOT
# =====================================================

def box_chart(
    df,
    x,
    y,
    title="Box Plot"
):
    """
    Box plot for outlier detection.
    """

    fig = px.box(
        df,
        x=x,
        y=y
    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# BRAND COMPARISON
# =====================================================

def brand_comparison_chart(
    df,
    company_column,
    price_column
):
    """
    Average price by company.
    """

    brand_df = (
        df.groupby(company_column)[price_column]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        brand_df,
        x=company_column,
        y=price_column,
        color=price_column,
        text_auto=".2s"
    )

    apply_layout(
        fig,
        "Top 10 Brands by Average Price"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# FUEL ANALYSIS
# =====================================================

def fuel_analysis_chart(
    df,
    fuel_column
):
    """
    Fuel type distribution.
    """

    fuel = (
        df[fuel_column]
        .value_counts()
        .reset_index()
    )

    fuel.columns = [
        fuel_column,
        "Count"
    ]

    fig = px.bar(
        fuel,
        x=fuel_column,
        y="Count",
        color="Count",
        text_auto=True
    )

    apply_layout(
        fig,
        "Fuel Type Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# YEAR TREND
# =====================================================

def year_trend_chart(
    df,
    year_column
):
    """
    Manufacturing year trend.
    """

    year_df = (
        df.groupby(year_column)
        .size()
        .reset_index(name="Cars")
    )

    fig = px.line(
        year_df,
        x=year_column,
        y="Cars",
        markers=True
    )

    apply_layout(
        fig,
        "Manufacturing Year Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# VALUE COUNTS BAR
# =====================================================

def value_count_chart(
    df,
    column,
    top=10
):
    """
    Value count visualization.
    """

    counts = (
        df[column]
        .value_counts()
        .head(top)
        .reset_index()
    )

    counts.columns = [
        column,
        "Count"
    ]

    fig = px.bar(
        counts,
        x=column,
        y="Count",
        text_auto=True
    )

    apply_layout(
        fig,
        f"{column} Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


import numpy as np

# =====================================================
# CORRELATION HEATMAP
# =====================================================

def correlation_heatmap(
    df,
    title="Correlation Heatmap"
):
    """
    Correlation heatmap for numerical features.
    """

    numeric_df = df.select_dtypes(include=np.number)

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="Blues"
    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# FEATURE IMPORTANCE
# =====================================================

def feature_importance_chart(
    features,
    importance,
    title="Feature Importance"
):
    """
    Feature importance visualization.
    """

    data = pd.DataFrame({

        "Feature": features,

        "Importance": importance

    })

    data = data.sort_values(
        "Importance",
        ascending=True
    )

    fig = px.bar(

        data,

        x="Importance",

        y="Feature",

        orientation="h",

        text_auto=".2f"

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# PRICE RANGE DISTRIBUTION
# =====================================================

def price_distribution_chart(
    df,
    price_column,
    title="Price Distribution"
):
    """
    Price histogram.
    """

    fig = px.histogram(

        df,

        x=price_column,

        nbins=40

    )

    apply_layout(fig, title)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# DEPRECIATION TREND
# =====================================================

def depreciation_chart(
    df,
    year_column,
    price_column
):
    """
    Average price by manufacturing year.
    """

    trend = (

        df.groupby(year_column)[price_column]

        .mean()

        .reset_index()

    )

    fig = px.line(

        trend,

        x=year_column,

        y=price_column,

        markers=True

    )

    apply_layout(
        fig,
        "Vehicle Depreciation Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# MODEL COMPARISON
# =====================================================

def model_comparison_chart(
    models,
    scores,
    metric="R² Score"
):
    """
    Compare ML models.
    """

    data = pd.DataFrame({

        "Model": models,

        metric: scores

    })

    fig = px.bar(

        data,

        x="Model",

        y=metric,

        color=metric,

        text_auto=".3f"

    )

    apply_layout(
        fig,
        "Model Performance Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# SCATTER MATRIX
# =====================================================

def scatter_matrix_chart(
    df,
    columns
):
    """
    Scatter matrix for EDA.
    """

    fig = px.scatter_matrix(
        df,
        dimensions=columns
    )

    apply_layout(
        fig,
        "Scatter Matrix"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =====================================================
# KPI CHART
# =====================================================

def kpi_card_chart(
    title,
    value,
    delta=None
):
    """
    Streamlit KPI wrapper.
    """

    st.metric(
        title,
        value,
        delta
    )


# =====================================================
# CHART CONTAINER
# =====================================================

def chart_container(
    title,
    chart_function,
    *args,
    **kwargs
):
    """
    Standard chart container.
    """

    with st.container(border=True):

        st.subheader(title)

        chart_function(
            *args,
            **kwargs
        )


# =====================================================
# EXPORT DATAFRAME
# =====================================================

def download_dataframe(
    df,
    filename="data.csv",
    label="📥 Download CSV"
):
    """
    Download dataframe.
    """

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(

        label,

        csv,

        filename,

        "text/csv",

        use_container_width=True

    )


# =====================================================
# CHART DIVIDER
# =====================================================

def section(title):
    """
    Beautiful section heading.
    """

    st.divider()

    st.subheader(title)



