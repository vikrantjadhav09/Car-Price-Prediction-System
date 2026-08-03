import matplotlib.pyplot as plt
import seaborn as sns


from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import streamlit as st

from components.navbar import navbar
from components.sidebar import sidebar
from components.footer import footer

from services.dataset_service import dataset_service
from services.prediction_service import prediction_service

# -------------------------------------------------------

st.set_page_config(

    page_title="Model Performance",

    page_icon="📈",

    layout="wide"

)

# -------------------------------------------------------

st.markdown("""

<style>

.hero{

background:linear-gradient(
90deg,
#7C3AED,
#6D28D9
);

padding:35px;

border-radius:18px;

color:white;

margin-bottom:20px;

}

.hero h1{

font-size:40px;

font-weight:bold;

}

.hero p{

font-size:18px;

}

.model-card{

padding:20px;

border-radius:15px;

background:#F8FAFC;

color:#1F2937;

border:1px solid #E5E7EB;

}

</style>

""",unsafe_allow_html=True)

# -------------------------------------------------------

df = dataset_service.load()

# -------------------------------------------------------

# sidebar(

#     api_online=prediction_service.backend_online(),

#     response_time=0.10,

#     dataset_rows=len(df),

#     dataset_columns=len(df.columns),

#     brand_count=df["company"].nunique(),

#     model_name="Random Forest Regressor",

#     accuracy="96%",

#     version="1.0"

# )

# -------------------------------------------------------

# navbar(

#     page_title="Model Performance",

#     page_description="Evaluate Machine Learning Model"

# )

# -------------------------------------------------------

st.markdown("""

<div class="hero">

<h1>📈 Model Performance Dashboard</h1>

<p>

Analyze model performance using multiple evaluation metrics,
visualizations and insights.

</p>

</div>

""",unsafe_allow_html=True)


st.subheader("🤖 Model Overview")

left,right=st.columns([1,1])

with left:

    st.markdown("""

<div class="model-card">

### Model Information

| Item | Value |
|------|------|
| Algorithm | Random Forest Regressor |
| Version | 1.0 |
| Dataset | Used Car Dataset |
| Target | Price |
| Features | 5 |

</div>

""",unsafe_allow_html=True)

with right:

    st.markdown("""

<div class="model-card">

### Training Summary

✔ Ensemble Learning

✔ Non Linear Model

✔ Handles Outliers Well

✔ Robust Performance

✔ Low Overfitting

</div>

""",unsafe_allow_html=True)
    


# =====================================================
# MODEL METRICS
# =====================================================

st.subheader("📊 Model Evaluation Metrics")

R2_SCORE = 0.5343
MAE = 133302.35
RMSE = 307953.29
MSE = RMSE ** 2

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "R² Score",
        f"{R2_SCORE:.4f}"
    )

with col2:

    st.metric(
        "MAE",
        f"₹ {MAE:,.0f}"
    )

with col3:

    st.metric(
        "RMSE",
        f"₹ {RMSE:,.0f}"
    )

with col4:

    st.metric(
        "MSE",
        f"{MSE:,.0f}"
    )


# =====================================================
# PERFORMANCE INTERPRETATION
# =====================================================

st.divider()

st.subheader("📝 Performance Interpretation")

if R2_SCORE >= 0.90:

    st.success(
        "Excellent predictive performance."
    )

elif R2_SCORE >= 0.80:

    st.success(
        "Very good model performance."
    )

elif R2_SCORE >= 0.70:

    st.info(
        "Good predictive capability."
    )

elif R2_SCORE >= 0.60:

    st.warning(
        "Fair performance. Improvement possible."
    )

else:

    st.error(
        """
Current R² score indicates moderate prediction capability.

Model improvement is recommended before production deployment.
"""
    )



st.divider()

st.subheader("📚 Metric Explanation")

with st.expander("What do these metrics mean?"):

    st.markdown("""

### 🎯 R² Score

Measures how much variation in car prices the model explains.

- Higher is better
- Range: 0 to 1

---

### 💰 MAE

Average prediction error.

Current Model:

₹133,302

Meaning:

On average, predictions differ from actual prices by about ₹1.33 lakh.

---

### 📈 RMSE

Penalizes larger prediction errors.

Current Model:

₹307,953

---

### 📊 MSE

Squared error used during evaluation.

Lower values indicate better performance.

""")
    



st.divider()

st.header("📊 Exploratory Data Analysis (EDA)")

st.markdown("""
Exploratory Data Analysis (EDA) helps us understand the dataset before
building a Machine Learning model.

It answers questions like:

- How many cars are present?
- Which company sells the most cars?
- Which fuel type is most common?
- How are car prices distributed?
- Are there any missing values?
- Are there any duplicate records?
- Which features affect the selling price?

EDA helps identify patterns, relationships, and anomalies in the data.
""")


st.subheader("📄 Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.dataframe(df.head())



st.subheader("📄 Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.dataframe(df.head())


st.subheader("📈 Statistical Summary")

st.dataframe(df.describe())



st.subheader("🚫 Missing Values")

missing = df.isnull().sum()

st.dataframe(missing)

fig, ax = plt.subplots(figsize=(8,4))

sns.heatmap(
    df.isnull(),
    cbar=False,
    cmap="viridis",
    ax=ax
)

st.pyplot(fig)


st.subheader("📑 Duplicate Records")

duplicates = df.duplicated().sum()

st.metric(
    "Duplicate Rows",
    duplicates
)

st.subheader("💰 Price Distribution")

fig, ax = plt.subplots(figsize=(10,5))

sns.histplot(
    df["Price"],
    kde=True,
    color="royalblue",
    ax=ax
)

ax.set_title("Distribution of Car Prices")

st.pyplot(fig)


fig, ax = plt.subplots(figsize=(10,2))

sns.boxplot(
    x=df["Price"],
    color="orange",
    ax=ax
)

st.pyplot(fig)


fig, ax = plt.subplots(figsize=(10,2))

sns.boxplot(
    x=df["Price"],
    color="orange",
    ax=ax
)

st.pyplot(fig)


st.subheader("🏭 Cars by Company")

company = df["company"].value_counts()

fig, ax = plt.subplots(figsize=(12,6))

sns.barplot(
    x=company.index,
    y=company.values,
    ax=ax
)

plt.xticks(rotation=90)

st.pyplot(fig)


st.subheader("⛽ Fuel Type")

fig, ax = plt.subplots(figsize=(6,5))

sns.countplot(
    data=df,
    x="fuel_type",
    ax=ax
)

st.pyplot(fig)


st.subheader("⛽ Fuel Type")

fig, ax = plt.subplots(figsize=(6,5))

sns.countplot(
    data=df,
    x="fuel_type",
    ax=ax
)

st.pyplot(fig)


st.subheader("📅 Price vs Manufacturing Year")

fig, ax = plt.subplots(figsize=(10,5))

sns.scatterplot(
    data=df,
    x="year",
    y="Price",
    ax=ax
)

st.pyplot(fig)


st.subheader("📌 Key Insights")

st.success("""
✅ Most listed cars belong to a few popular brands.

✅ Car price generally decreases as kilometers driven increase.

✅ Newer cars usually have higher resale prices.

✅ The price distribution is right-skewed because a few luxury cars are much more expensive than the rest.

✅ No major missing-value issues after preprocessing.

✅ These insights helped in selecting features for the Machine Learning model.
""")




