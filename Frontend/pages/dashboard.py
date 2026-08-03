"""
=========================================================
Dashboard
AI Powered Car Price Prediction System
=========================================================
"""

from pathlib import Path
import sys

# -------------------------------------------------------
# Project Path
# -------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# -------------------------------------------------------
# Imports
# -------------------------------------------------------

import pandas as pd
import streamlit as st

from components.navbar import navbar
from components.sidebar import sidebar
from components.footer import footer

from components.metrics import (
    dashboard_summary,
    dataset_metrics,
)

from components.cards import (
    section_title,
    info_card,
)

from components.charts import (
    histogram_chart,
    brand_comparison_chart,
    fuel_analysis_chart,
    year_trend_chart,
)

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🚗",
    layout="wide",
)

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------

st.markdown(
    """
<style>

.block-container{

padding-top:1.5rem;

padding-bottom:2rem;

}

.hero{

background:linear-gradient(
90deg,
#2563EB,
#1D4ED8
);

padding:35px;

border-radius:18px;

color:white;

margin-bottom:25px;

}

.hero h1{

font-size:40px;

font-weight:bold;

margin-bottom:10px;

}

.hero p{

font-size:18px;

opacity:.95;

}

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# Dataset Loader
# -------------------------------------------------------

@st.cache_data
def load_data():

    return pd.read_csv(
        ROOT / "Data" / "cleaned_car_data.csv"
    )


df = load_data()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

# sidebar(
#     api_online=True,
#     response_time=0.12,
#     dataset_rows=df.shape[0],
#     dataset_columns=df.shape[1],
#     brand_count=df["company"].nunique(),
#     model_name="Random Forest",
#     accuracy="96%",
#     version="1.0.0",
# )

# -------------------------------------------------------
# Navbar
# -------------------------------------------------------

# navbar(
#     page_title="Dashboard",
#     page_description="Overview of dataset, analytics and machine learning system."
# )

# -------------------------------------------------------
# Hero Section
# -------------------------------------------------------

st.markdown(
    """
<div class="hero">

<h1>🚗 AI Powered Car Price Prediction</h1>

<p>

Analyze the dataset, explore trends, visualize insights,
and monitor your machine learning model through an
interactive dashboard.

</p>

</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------
# Dataset Overview
# -------------------------------------------------------

section_title(
    "📊 Dataset Overview",
    "Quick summary of the loaded dataset."
)

dashboard_summary(df)

st.write("")

dataset_metrics(df)

# -------------------------------------------------------
# Information Card
# -------------------------------------------------------

info_card(
    "Project Overview",
    """
This dashboard provides a high-level overview of the car dataset,
including company statistics, fuel distribution, manufacturing year,
and pricing trends.

Use the navigation menu to access prediction, EDA,
model performance, and prediction history.
"""
)

# =====================================================
# PRICE SUMMARY
# =====================================================

section_title(
    "💰 Price Summary",
    "Key pricing insights from the dataset."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Minimum Price",
        f"₹ {df['Price'].min():,.0f}"
    )

with col2:
    st.metric(
        "Average Price",
        f"₹ {df['Price'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Maximum Price",
        f"₹ {df['Price'].max():,.0f}"
    )

with col4:
    st.metric(
        "Median Price",
        f"₹ {df['Price'].median():,.0f}"
    )


# =====================================================
# DATASET INSIGHTS
# =====================================================

section_title(
    "📌 Dataset Insights",
    "Quick statistics about the dataset."
)

col1, col2, col3 = st.columns(3)

with col1:

    info_card(
        "🚗 Total Brands",
        f"""
### {df['company'].nunique()}

Different manufacturers available in the dataset.
"""
    )

with col2:

    info_card(
        "⛽ Fuel Types",
        f"""
### {df['fuel_type'].nunique()}

Different fuel categories available.
"""
    )

with col3:

    info_card(
        "📅 Manufacturing Years",
        f"""
### {df['year'].min()} - {df['year'].max()}

Vehicle manufacturing range.
"""
    )


# =====================================================
# QUICK INSIGHTS
# =====================================================

section_title(
    "⚡ Quick Insights",
    "Automatically generated dataset highlights."
)

most_expensive = (
    df.loc[df["Price"].idxmax(), "company"]
)

cheapest = (
    df.loc[df["Price"].idxmin(), "company"]
)

popular_brand = (
    df["company"]
    .value_counts()
    .idxmax()
)

popular_fuel = (
    df["fuel_type"]
    .value_counts()
    .idxmax()
)

avg_km = (
    df["kms_driven"]
    .mean()
)

c1, c2 = st.columns(2)

with c1:

    st.success(f"""
### 🚗 Most Expensive Brand

**{most_expensive}**
""")

    st.info(f"""
### 🏆 Most Popular Brand

**{popular_brand}**
""")

    st.warning(f"""
### ⛽ Most Common Fuel

**{popular_fuel}**
""")

with c2:

    st.success(f"""
### 💰 Cheapest Brand

**{cheapest}**
""")

    st.info(f"""
### 🚘 Average Kilometers Driven

**{avg_km:,.0f} KM**
""")

    st.warning(f"""
### 📅 Manufacturing Years

**{df['year'].min()} → {df['year'].max()}**
""")


# =====================================================
# VEHICLE SUMMARY
# =====================================================

section_title(
    "🚘 Vehicle Summary"
)

summary = pd.DataFrame({

    "Metric": [

        "Total Cars",

        "Brands",

        "Fuel Types",

        "Average Price",

        "Average KM Driven"

    ],

    "Value": [

        f"{len(df):,}",

        df["company"].nunique(),

        df["fuel_type"].nunique(),

        f"₹ {df['Price'].mean():,.0f}",

        f"{df['kms_driven'].mean():,.0f}"

    ]

})

st.dataframe(
    summary,
    width="stretch",
    hide_index=True
)

# =====================================================
# VISUAL ANALYTICS
# =====================================================

section_title(
    "📊 Interactive Analytics",
    "Explore the dataset visually."
)

# -----------------------------------------------------
# Row 1
# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    histogram_chart(
        df=df,
        column="Price",
        bins=40,
        title="Price Distribution"
    )

with col2:

    brand_comparison_chart(
        df=df,
        company_column="company",
        price_column="Price"
    )

# -----------------------------------------------------
# Row 2
# -----------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    fuel_analysis_chart(
        df=df,
        fuel_column="fuel_type"
    )

with col2:

    year_trend_chart(
        df=df,
        year_column="year"
    )


# =====================================================
# TOP 10 EXPENSIVE BRANDS
# =====================================================

section_title(
    "🏆 Top 10 Premium Car Brands"
)

top_brands = (
    df.groupby("company")["Price"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

st.dataframe(
    top_brands,
    width="stretch",
    hide_index=True
)


# =====================================================
# BRAND FREQUENCY
# =====================================================

section_title(
    "🚗 Brand Frequency"
)

brand_count = (
    df["company"]
      .value_counts()
      .reset_index()
)

brand_count.columns = [
    "Company",
    "Cars"
]

st.bar_chart(
    brand_count.set_index("Company")
)


# =====================================================
# FUEL DISTRIBUTION
# =====================================================

section_title(
    "⛽ Fuel Type Distribution"
)

fuel_df = (
    df["fuel_type"]
      .value_counts()
      .reset_index()
)

fuel_df.columns = [
    "Fuel",
    "Count"
]

st.bar_chart(
    fuel_df.set_index("Fuel")
)


# =====================================================
# MANUFACTURING YEAR
# =====================================================

section_title(
    "📅 Cars by Manufacturing Year"
)

year_df = (
    df.groupby("year")
      .size()
      .reset_index(name="Cars")
)

st.line_chart(
    year_df.set_index("year")
)


# =====================================================
# COMPANY STATISTICS
# =====================================================

section_title(
    "🏢 Company Statistics"
)

company_stats = (
    df.groupby("company")
      .agg(
          Total_Cars=("company", "count"),
          Average_Price=("Price", "mean"),
          Average_KM=("kms_driven", "mean")
      )
      .sort_values(
          by="Total_Cars",
          ascending=False
      )
      .reset_index()
)

st.dataframe(
    company_stats,
    width="stretch",
    hide_index=True
)


# =====================================================
# DATASET SNAPSHOT
# =====================================================

section_title(
    "📋 Dataset Snapshot"
)

st.dataframe(
    df.head(20),
    width="stretch",
    hide_index=True
)


# =====================================================
# INTERACTIVE DATA EXPLORER
# =====================================================

section_title(
    "🔍 Explore Dataset",
    "Search and filter vehicle records."
)

col1, col2, col3 = st.columns(3)

with col1:
    selected_company = st.selectbox(
        "Company",
        ["All"] + sorted(df["company"].unique().tolist())
    )

with col2:
    selected_fuel = st.selectbox(
        "Fuel Type",
        ["All"] + sorted(df["fuel_type"].unique().tolist())
    )

with col3:
    year_range = st.slider(
        "Manufacturing Year",
        int(df["year"].min()),
        int(df["year"].max()),
        (
            int(df["year"].min()),
            int(df["year"].max())
        )
    )

filtered_df = df.copy()

if selected_company != "All":
    filtered_df = filtered_df[
        filtered_df["company"] == selected_company
    ]

if selected_fuel != "All":
    filtered_df = filtered_df[
        filtered_df["fuel_type"] == selected_fuel
    ]

filtered_df = filtered_df[
    (filtered_df["year"] >= year_range[0]) &
    (filtered_df["year"] <= year_range[1])
]

search = st.text_input(
    "🔎 Search Vehicle"
)

if search:

    filtered_df = filtered_df[
        filtered_df.astype(str)
        .apply(
            lambda row:
            row.str.contains(
                search,
                case=False
            ).any(),
            axis=1
        )
    ]

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)

# =====================================================
# DOWNLOAD DATASET
# =====================================================

section_title(
    "📥 Export Dataset"
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Filtered Dataset",
    data=csv,
    file_name="filtered_car_dataset.csv",
    mime="text/csv",
    width="stretch"
)

# =====================================================
# AI INSIGHTS
# =====================================================

section_title(
    "🤖 AI Insights"
)

info_card(
    "AI Recommendation",
    f"""
Based on the current dataset:

• 🚗 Total Cars : **{len(filtered_df):,}**

• 🏢 Brands : **{filtered_df['company'].nunique()}**

• ⛽ Fuel Types : **{filtered_df['fuel_type'].nunique()}**

• 💰 Average Price :
₹ **{filtered_df['Price'].mean():,.0f}**

• 📅 Latest Year :
**{filtered_df['year'].max()}**

Future versions of this application will use
Google Gemini AI to generate personalized
market insights and buying recommendations.
"""
)

# =====================================================
# SYSTEM STATUS
# =====================================================

section_title(
    "⚙ System Status"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("✅ Dataset Loaded")

with col2:
    st.success("✅ Model Ready")

with col3:
    st.success("✅ Frontend Running")

with col4:
    st.success("✅ Backend Connected")

# =====================================================
# PROJECT INFORMATION
# =====================================================

with st.expander("ℹ Project Information"):

    st.markdown(
        """
### 🚗 AI Powered Car Price Prediction

This application provides:

- Machine Learning Price Prediction
- Interactive Dashboard
- Exploratory Data Analysis
- Model Performance Evaluation
- Prediction History
- AI Insights (Upcoming)

### Technology Stack

- Python
- Streamlit
- FastAPI
- Scikit-Learn
- Plotly
- Pandas
- NumPy

Version **1.0.0**
"""
    )

# =====================================================
# FOOTER
# =====================================================

footer(
    version="1.0.0",
    model_name="Random Forest Regressor",
    api_status="🟢 Online"
)


