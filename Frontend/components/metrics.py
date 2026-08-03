"""
=========================================================
Reusable Metric Components
AI Powered Car Price Prediction System
=========================================================
"""

from __future__ import annotations

import streamlit as st


# =====================================================
# CSS
# =====================================================

def load_metric_css():
    """Load metric component styles."""

    st.markdown(
        """
<style>

/* KPI Card */

.metric-box{

    background:#F8FAFC;

    border-radius:18px;

    padding:22px;

    border:1px solid #E5E7EB;

    text-align:center;

    box-shadow:0 4px 12px rgba(0,0,0,.06);

    transition:.25s;

}

.metric-box:hover{

    transform:translateY(-4px);

    box-shadow:0 8px 20px rgba(37,99,235,.15);

}

.metric-icon{

    font-size:34px;

}

.metric-title{

    color:#6B7280;

    font-size:15px;

    margin-top:8px;

}

.metric-value{

    font-size:30px;

    font-weight:bold;

    color:#2563EB;

}

.metric-delta{

    color:#10B981;

    margin-top:5px;

}

/* Status */

.status-online{

    color:#10B981;

    font-weight:bold;

}

.status-warning{

    color:#F59E0B;

    font-weight:bold;

}

.status-offline{

    color:#EF4444;

    font-weight:bold;

}

</style>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# KPI CARD
# =====================================================

def kpi_card(
    title: str,
    value,
    icon="📊",
    delta=None,
):
    """
    Beautiful KPI card.
    """

    load_metric_css()

    delta_html = ""

    if delta is not None:

        delta_html = f"""
<div class="metric-delta">

{delta}

</div>
"""

    st.markdown(
        f"""
<div class="metric-box">

<div class="metric-icon">

{icon}

</div>

<div class="metric-value">

{value}

</div>

<div class="metric-title">

{title}

</div>

{delta_html}

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# STREAMLIT METRIC
# =====================================================

def metric(
    label,
    value,
    delta=None,
):
    """
    Wrapper around st.metric.
    """

    st.metric(
        label,
        value,
        delta
    )


# =====================================================
# CURRENCY METRIC
# =====================================================

def currency_metric(
    label,
    value,
    delta=None,
):
    """
    Currency metric.
    """

    st.metric(

        label,

        f"₹ {value:,.0f}",

        delta

    )


# =====================================================
# PERCENTAGE METRIC
# =====================================================

def percentage_metric(
    label,
    value,
):
    """
    Percentage metric.
    """

    st.metric(

        label,

        f"{value}%"

    )


# =====================================================
# STATUS METRIC
# =====================================================

def status_metric(
    title,
    status
):
    """
    Online / Offline status.
    """

    load_metric_css()

    if status.lower() == "online":

        css = "status-online"

        icon = "🟢"

    elif status.lower() == "warning":

        css = "status-warning"

        icon = "🟡"

    else:

        css = "status-offline"

        icon = "🔴"

    st.markdown(
        f"""
<div class="metric-box">

<h3>{title}</h3>

<div class="{css}">

{icon} {status}

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# MODEL METRIC
# =====================================================

def model_metric(
    algorithm,
    accuracy,
    version
):
    """
    ML model summary.
    """

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Algorithm",
            algorithm
        )

    with c2:

        st.metric(
            "Accuracy",
            accuracy
        )

    with c3:

        st.metric(
            "Version",
            version
        )


# =====================================================
# PRICE METRIC
# =====================================================

def prediction_metric(
    predicted_price,
    confidence=96
):
    """
    Prediction metrics.
    """

    c1, c2 = st.columns(2)

    with c1:

        currency_metric(
            "Estimated Price",
            predicted_price
        )

    with c2:

        percentage_metric(
            "Confidence",
            confidence
        )


# =====================================================
# GRID METRICS
# =====================================================

def metric_grid(metrics):
    """
    Display metrics in a responsive grid.

    metrics = [
        ("Cars", 9200, "🚗"),
        ("Brands", 32, "🏢"),
        ("Accuracy", "96%", "🎯"),
        ("API", "Online", "🟢")
    ]
    """

    cols = st.columns(len(metrics))

    for col, item in zip(cols, metrics):

        title = item[0]
        value = item[1]
        icon = item[2]

        with col:

            kpi_card(
                title,
                value,
                icon
            )


# =====================================================
# DATASET METRICS
# =====================================================

def dataset_metrics(df):
    """
    Display dataset statistics.
    """

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "Rows",
            f"{df.shape[0]:,}",
            "📄"
        )

    with c2:
        kpi_card(
            "Columns",
            df.shape[1],
            "📊"
        )

    with c3:
        kpi_card(
            "Missing Values",
            int(df.isnull().sum().sum()),
            "❗"
        )

    with c4:
        kpi_card(
            "Duplicates",
            int(df.duplicated().sum()),
            "📋"
        )


# =====================================================
# VEHICLE METRICS
# =====================================================

def vehicle_metrics(
    company,
    model,
    year,
    fuel,
):
    """
    Vehicle information cards.
    """

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "Brand",
            company,
            "🚗"
        )

    with c2:
        kpi_card(
            "Model",
            model,
            "🏷️"
        )

    with c3:
        kpi_card(
            "Year",
            year,
            "📅"
        )

    with c4:
        kpi_card(
            "Fuel",
            fuel,
            "⛽"
        )


# =====================================================
# PRICE SUMMARY
# =====================================================

def price_summary(
    minimum,
    average,
    maximum
):
    """
    Price statistics.
    """

    c1, c2, c3 = st.columns(3)

    with c1:
        currency_metric(
            "Minimum Price",
            minimum
        )

    with c2:
        currency_metric(
            "Average Price",
            average
        )

    with c3:
        currency_metric(
            "Maximum Price",
            maximum
        )


# =====================================================
# API METRICS
# =====================================================

def api_metrics(
    status,
    response_time,
):
    """
    API health metrics.
    """

    c1, c2 = st.columns(2)

    with c1:

        status_metric(
            "FastAPI",
            status
        )

    with c2:

        st.metric(
            "Response Time",
            f"{response_time:.2f} sec"
        )


# =====================================================
# SYSTEM METRICS
# =====================================================

def system_metrics():
    """
    System information.
    """

    import platform
    import sys

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Python",
            platform.python_version()
        )

    with c2:

        st.metric(
            "Platform",
            platform.system()
        )


# =====================================================
# COMPARISON METRIC
# =====================================================

def comparison_metric(
    title,
    current,
    previous
):
    """
    Compare current and previous values.
    """

    delta = current - previous

    st.metric(
        title,
        current,
        delta
    )


# =====================================================
# MODEL PERFORMANCE
# =====================================================

def performance_metrics(
    mae,
    mse,
    rmse,
    r2
):
    """
    Regression metrics.
    """

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("MAE", f"{mae:.3f}")

    with c2:
        st.metric("MSE", f"{mse:.3f}")

    with c3:
        st.metric("RMSE", f"{rmse:.3f}")

    with c4:
        st.metric("R² Score", f"{r2:.3f}")


# =====================================================
# DASHBOARD SUMMARY
# =====================================================

def dashboard_summary(df):
    """
    Dashboard overview cards.
    """

    metric_grid([

        (
            "Cars",
            f"{len(df):,}",
            "🚗"
        ),

        (
            "Brands",
            df["company"].nunique(),
            "🏢"
        ),

        (
            "Fuel Types",
            df["fuel_type"].nunique(),
            "⛽"
        ),

        (
            "Years",
            f"{df['year'].min()} - {df['year'].max()}",
            "📅"
        )

    ])


# =====================================================
# HORIZONTAL METRIC ROW
# =====================================================

def metric_row(metrics):
    """
    metrics = [
        ("Cars",100),
        ("Brands",20),
        ("Accuracy","96%"),
    ]
    """

    cols = st.columns(len(metrics))

    for col, item in zip(cols, metrics):

        with col:

            st.metric(
                item[0],
                item[1]
            )


# =====================================================
# SECTION HEADER
# =====================================================

def metric_section(title):
    """
    Beautiful metric section.
    """

    st.divider()

    st.subheader(title)


# =====================================================
# EMPTY METRICS
# =====================================================

def no_metrics():
    """
    Placeholder when metrics unavailable.
    """

    st.info(
        "No metrics available."
    )


# =====================================================
# SUCCESS SUMMARY
# =====================================================

def success_summary():

    st.success(
        """
✅ Dataset Loaded Successfully

✅ ML Model Ready

✅ FastAPI Connected

✅ Streamlit Running
"""
    )


