import plotly.express as px
import plotly.graph_objects as go



from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# -------------------------------------------------------
# Imports
# -------------------------------------------------------

import streamlit as st
import pandas as pd

from components.navbar import navbar
from components.sidebar import sidebar
from components.footer import footer

from services.dataset_service import dataset_service
from services.analytics_service import analytics_service

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(

    page_title="EDA",

    page_icon="📊",

    layout="wide"

)

# -------------------------------------------------------
# CSS
# -------------------------------------------------------

st.markdown("""
<style>

.hero{

background:linear-gradient(90deg,#0F766E,#115E59);

padding:35px;

border-radius:18px;

color:white;

margin-bottom:20px;

}

.hero h1{

font-size:38px;

font-weight:bold;

}

.hero p{

font-size:18px;

}

</style>
""",unsafe_allow_html=True)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = dataset_service.load()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

# sidebar(

#     api_online=True,

#     response_time=0.10,

#     dataset_rows=len(df),

#     dataset_columns=len(df.columns),

#     brand_count=df["company"].nunique(),

#     model_name="Random Forest",

#     accuracy="96%",

#     version="1.0"

# )

# -------------------------------------------------------
# Navbar
# -------------------------------------------------------

# navbar(

#     page_title="Exploratory Data Analysis",

#     page_description="Explore and understand the dataset visually."

# )

# -------------------------------------------------------
# Hero
# -------------------------------------------------------

st.markdown("""

<div class="hero">

<h1>📊 Exploratory Data Analysis</h1>

<p>

Analyze the dataset through interactive visualizations,
summary statistics and insights.

</p>

</div>

""",unsafe_allow_html=True)


# -------------------------------------------------------
# FILTERS
# -------------------------------------------------------

st.subheader("🎛 Dataset Filters")

col1,col2,col3=st.columns(3)

with col1:

    company=st.selectbox(

        "Company",

        ["All"]+sorted(df["company"].unique())

    )

with col2:

    fuel=st.selectbox(

        "Fuel Type",

        ["All"]+sorted(df["fuel_type"].unique())

    )

with col3:

    year=st.selectbox(

        "Year",

        ["All"]+sorted(df["year"].unique())

    )

filtered_df=df.copy()

if company!="All":

    filtered_df=filtered_df[

        filtered_df["company"]==company

    ]

if fuel!="All":

    filtered_df=filtered_df[

        filtered_df["fuel_type"]==fuel

    ]

if year!="All":

    filtered_df=filtered_df[

        filtered_df["year"]==year

    ]


# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------

summary=analytics_service.dataset_summary(filtered_df)

st.subheader("📈 Dataset Summary")

c1,c2,c3,c4=st.columns(4)

with c1:

    st.metric(

        "Rows",

        summary["rows"]

    )

with c2:

    st.metric(

        "Columns",

        summary["columns"]

    )

with c3:

    st.metric(

        "Missing Values",

        summary["missing"]

    )

with c4:

    st.metric(

        "Duplicates",

        summary["duplicates"]

    )


# =====================================================
# EDA WORKSPACE
# =====================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📈 Distribution",
        "📊 Categorical",
        "📉 Correlation",
        "🎯 Outliers",
        "📋 Statistics"
    ]
)

# =====================================================
# TAB 1
# DISTRIBUTION ANALYSIS
# =====================================================

with tab1:

    st.subheader("💰 Price Distribution")

    st.bar_chart(
        filtered_df["Price"]
    )

    st.write("### Price Statistics")

    price = analytics_service.price_summary(filtered_df)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Average",
            f"₹ {price['mean']:,.0f}"
        )

    with c2:
        st.metric(
            "Minimum",
            f"₹ {price['min']:,.0f}"
        )

    with c3:
        st.metric(
            "Maximum",
            f"₹ {price['max']:,.0f}"
        )

    st.write("### Kilometers Driven")

    st.bar_chart(
        filtered_df["kms_driven"]
    )

# =====================================================
# TAB 2
# CATEGORICAL ANALYSIS
# =====================================================

with tab2:

    st.subheader("🚗 Company Distribution")

    company_count = (
        filtered_df["company"]
        .value_counts()
    )

    st.bar_chart(company_count)

    st.write("")

    st.subheader("⛽ Fuel Distribution")

    fuel_count = (
        filtered_df["fuel_type"]
        .value_counts()
    )

    st.bar_chart(fuel_count)

    st.write("")

    st.subheader("📅 Manufacturing Year")

    year_count = (
        filtered_df["year"]
        .value_counts()
        .sort_index()
    )

    st.line_chart(year_count)



# =====================================================
# TAB 3
# CORRELATION
# =====================================================

with tab3:

    st.subheader("📉 Correlation Matrix")

    correlation = analytics_service.correlation(
        filtered_df
    )

    st.dataframe(
        correlation,
        width="stretch"
    )

    st.write(
        """
Positive values indicate variables that increase together.

Negative values indicate variables that move in opposite directions.

Values close to **1** or **-1** represent strong relationships.
"""
    )


# =====================================================
# TAB 4
# OUTLIER ANALYSIS
# =====================================================

with tab4:

    st.subheader("🎯 Outlier Detection")

    numeric_columns = list(
        filtered_df.select_dtypes(
            include="number"
        ).columns
    )

    selected_column = st.selectbox(
        "Choose Numeric Column",
        numeric_columns
    )

    outliers = analytics_service.outliers(
        filtered_df,
        selected_column
    )

    st.metric(
        "Outliers Found",
        len(outliers)
    )

    if outliers.empty:

        st.success(
            "No outliers detected."
        )

    else:

        st.dataframe(
            outliers,
            width="stretch"
        )


# =====================================================
# TAB 5
# STATISTICS
# =====================================================

with tab5:

    st.subheader("📋 Statistical Summary")

    description = analytics_service.describe(
        filtered_df
    )

    st.dataframe(
        description,
        width="stretch"
    )

    st.write("")

    st.subheader("Missing Values")

    missing = analytics_service.missing_values(
        filtered_df
    )

    st.dataframe(
        missing,
        width="stretch"
    )


# =====================================================
# TOP BRANDS
# =====================================================

st.divider()

st.subheader("🏆 Top 10 Car Brands")

brand_count = (
    filtered_df["company"]
    .value_counts()
    .head(10)
    .reset_index()
)

brand_count.columns = ["Company", "Cars"]

fig = px.bar(
    brand_count,
    x="Company",
    y="Cars",
    text="Cars",
    color="Cars",
    title="Top 10 Brands by Number of Cars"
)

fig.update_layout(
    xaxis_title="Company",
    yaxis_title="Number of Cars",
    height=500
)

st.plotly_chart(
    fig,
    width="stretch"
)



# =====================================================
# PREMIUM BRANDS
# =====================================================

st.subheader("💎 Average Price by Brand")

premium = (

    filtered_df

    .groupby("company")["Price"]

    .mean()

    .sort_values(ascending=False)

    .head(10)

    .reset_index()

)

premium.columns=["Company","Average Price"]

fig=px.bar(

    premium,

    x="Company",

    y="Average Price",

    color="Average Price",

    text_auto=".2s",

    title="Top Premium Brands"

)

st.plotly_chart(

    fig,

    width="stretch"

)


# =====================================================
# PRICE TREND
# =====================================================

st.subheader("📈 Average Price by Manufacturing Year")

trend=(

    filtered_df

    .groupby("year")["Price"]

    .mean()

    .reset_index()

)

fig=px.line(

    trend,

    x="year",

    y="Price",

    markers=True,

    title="Price Trend"

)

fig.update_traces(

    line_width=3

)

st.plotly_chart(

    fig,

    width="stretch"

)



# =====================================================
# FUEL ANALYSIS
# =====================================================

st.subheader("⛽ Fuel Type Distribution")

fuel=(

    filtered_df

    .groupby("fuel_type")

    .size()

    .reset_index(name="Cars")

)

fig=px.pie(

    fuel,

    names="fuel_type",

    values="Cars",

    hole=.45,

    title="Fuel Distribution"

)

st.plotly_chart(

    fig,

    width="stretch"

)

# =====================================================
# KMS DRIVEN
# =====================================================

st.subheader("🛣 Kilometers Driven")

fig=px.histogram(

    filtered_df,

    x="kms_driven",

    nbins=30,

    title="Distribution of Kilometers Driven"

)

st.plotly_chart(

    fig,

    width="stretch"

)

# =====================================================
# PRICE HISTOGRAM
# =====================================================

st.subheader("💵 Price Distribution")

fig=px.histogram(

    filtered_df,

    x="Price",

    nbins=40,

    marginal="box",

    title="Car Price Distribution"

)

st.plotly_chart(

    fig,

    width="stretch"

)


# =====================================================
# PRICE VS KM
# =====================================================

st.subheader("📉 Price vs Kilometers")

fig=px.scatter(

    filtered_df,

    x="kms_driven",

    y="Price",

    color="fuel_type",

    hover_data=["company","model"],

    title="Price vs Kilometers Driven"

)

st.plotly_chart(

    fig,

    width="stretch"

)


# =====================================================
# BOXPLOT
# =====================================================

st.subheader("📦 Price Distribution by Fuel Type")

fig=px.box(

    filtered_df,

    x="fuel_type",

    y="Price",

    color="fuel_type"

)

st.plotly_chart(

    fig,

    width="stretch"

)


# =====================================================
# DATASET EXPLORER
# =====================================================

st.divider()

st.header("🔍 Dataset Explorer")

search = st.text_input(
    "Search Company / Model / Fuel Type",
    placeholder="e.g. Hyundai, Swift, Petrol..."
)

if search:

    search_df = filtered_df[
        filtered_df.astype(str)
        .apply(
            lambda x: x.str.contains(
                search,
                case=False,
                na=False
            )
        )
        .any(axis=1)
    ]

else:

    search_df = filtered_df.copy()

st.dataframe(
    search_df,
    width="stretch",
    hide_index=True,
    height=500
)

st.caption(
    f"Showing {len(search_df):,} of {len(filtered_df):,} rows"
)



# =====================================================
# DOWNLOAD DATASET
# =====================================================

st.divider()

st.subheader("📥 Export Dataset")

csv = search_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv",
    width="stretch"
)


# =====================================================
# DATASET INSIGHTS
# =====================================================

st.divider()

st.header("📈 Dataset Insights")

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
### 🚗 Brands

**{filtered_df['company'].nunique()}**

Unique Car Companies
""")

    st.info(f"""
### ⛽ Fuel Types

**{filtered_df['fuel_type'].nunique()}**

Different Fuel Categories
""")

with col2:

    st.info(f"""
### 📅 Year Range

{filtered_df['year'].min()} - {filtered_df['year'].max()}
""")

    st.info(f"""
### 💰 Average Price

₹ {filtered_df['Price'].mean():,.0f}
""")


# =====================================================
# AI SUMMARY
# =====================================================

st.divider()

st.header("🤖 AI Dataset Summary")

top_brand = (
    filtered_df["company"]
    .value_counts()
    .idxmax()
)

top_brand_count = (
    filtered_df["company"]
    .value_counts()
    .max()
)

premium_brand = (

    filtered_df

    .groupby("company")["Price"]

    .mean()

    .idxmax()

)

st.success(f"""
### Dataset Highlights

• Total Cars: **{len(filtered_df):,}**

• Most Common Brand: **{top_brand}**
({top_brand_count} Cars)

• Premium Brand:
**{premium_brand}**

• Average Price:
**₹ {filtered_df['Price'].mean():,.0f}**

• Average Kilometers:
**{filtered_df['kms_driven'].mean():,.0f} KM**

• Manufacturing Years:
**{filtered_df['year'].min()} - {filtered_df['year'].max()}**
""")


# =====================================================
# RAW DATA
# =====================================================

with st.expander("📄 View Complete Dataset"):

    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True
    )


# =====================================================
# FOOTER
# =====================================================

footer(
    version="1.0.0",
    model_name="Random Forest Regressor",
    api_status="🟢 Online"
)




