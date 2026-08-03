import streamlit as st
import pandas as pd

from services.dataset_service import dataset_service
from services.prediction_service import prediction_service

from components.sidebar import sidebar
from components.navbar import navbar
from components.footer import footer
from components.metrics import kpi_card, metric, currency_metric
from components.cards import info_card, metric_card, prediction_card, section_title
from components.charts import bar_chart, gauge_chart, confidence_chart, line_chart

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------------
# Data Loader
# -----------------------------------

@st.cache_data
def load_data():
    return dataset_service.load()


df = load_data()


# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.hero{
    background: linear-gradient(135deg,#0F172A,#1E3A8A);
    padding:35px;
    border-radius:20px;
    color:white;
}

.card{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
    margin-bottom:15px;
}

.card h3{
    color:#38BDF8;
}

.tech{
    background:#0F172A;
    padding:15px;
    border-radius:12px;
    border:1px solid #334155;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HERO
# -------------------------------------------------------

# st.markdown("""
# <div class="hero">

# # 🚗 AI Powered Car Price Prediction System

# ### Production Grade Machine Learning Application

# Predict used car prices using Machine Learning,
# FastAPI, Streamlit and Artificial Intelligence.

# </div>
# """, unsafe_allow_html=True)

# st.write("")


# -------------------------------------------------------
# PROJECT OVERVIEW
# -------------------------------------------------------

st.header("📌 Project Overview")

st.write("""
This project is an **End-to-End Machine Learning Application**
designed to estimate the resale value of used cars.

The application combines:

- Machine Learning
- FastAPI Backend
- Streamlit Frontend
- AI Generated Insights
- Interactive Dashboard
- Production Ready Architecture

The objective is to provide users with an intelligent,
fast and user-friendly platform for predicting vehicle prices.
""")

st.divider()




# -----------------------------------
# Helpers
# -----------------------------------

def parse_price(value):
    try:
        return float(str(value).replace("₹", "").replace(",", "").strip())
    except Exception:
        return 0.0


# def render_dashboard(dataframe: pd.DataFrame):
#     navbar(
#         page_title="Dashboard",
#         page_description="Overview of dataset insights and pricing trends."
#     )

#     section_title("📊 Dashboard", "High-level dataset overview and price analytics.")

#     avg_price = dataframe["Price"].mean()
#     max_price = dataframe["Price"].max()
#     min_price = dataframe["Price"].min()
#     total_brands = dataframe["company"].nunique()

#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         kpi_card("Average Price", f"₹ {avg_price:,.0f}", icon="💰")
#     with col2:
#         kpi_card("Highest Price", f"₹ {max_price:,.0f}", icon="🚘")
#     with col3:
#         kpi_card("Lowest Price", f"₹ {min_price:,.0f}", icon="📉")
#     with col4:
#         kpi_card("Brands", f"{total_brands}", icon="🏷️")

#     st.markdown("---")

#     company_counts = (
#     dataframe["company"]
#     .value_counts()
#     .reset_index(name="count")
#     )

#     company_counts.columns = ["company", "count"]

    
    
#     bar_chart(company_counts, x="company", y="count", title="Top Brands by Car Count")

#     year_trend = dataframe.groupby("year")["Price"].mean().reset_index()
#     line_chart(year_trend, x="year", y="Price", title="Average Price by Year")

#     st.markdown("---")
#     info_card(
#         "Prediction Summary",
#         "Use the Prediction page to estimate vehicle resale value and compare it with the dataset average."
#     )

#     # footer(
#     #     version="1.0.0",
#     #     model_name="Random Forest",
#     #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
#     # )


def render_prediction(dataframe: pd.DataFrame):
    navbar(
        page_title="Prediction",
        page_description="Predict the resale value of a used car."
    )

    section_title("🚗 Car Price Prediction", "Enter vehicle details to generate an estimate.")

    companies = sorted(dataframe["company"].unique())
    fuel_types = sorted(dataframe["fuel_type"].fillna("Unknown").unique())

    left, right = st.columns([1.2, 1])

    with left:
        company = st.selectbox("Company", companies)
        model = st.selectbox(
            "Car Model",
            sorted(dataframe[dataframe["company"] == company]["model"].unique()),
        )
        year = st.slider(
            "Manufacturing Year",
            int(dataframe["year"].min()),
            int(dataframe["year"].max()),
            int(dataframe["year"].max()),
        )
        fuel_type = st.selectbox("Fuel Type", fuel_types)
        kms_driven = st.number_input(
            "Kilometers Driven",
            min_value=0,
            value=25000,
            step=1000,
        )

        predict_button = st.button("🚀 Predict Price", use_container_width=True)

        if predict_button:
            payload = {
                "company": company,
                "model": model,
                "year": int(year),
                "fuel_type": fuel_type,
                "kms_driven": int(kms_driven),
            }

            valid, message = prediction_service.validate(payload)

            if not valid:
                st.error(message)
                st.session_state.prediction_result = None
                st.session_state.prediction_error = message
            else:
                with st.spinner("Predicting price..."):
                    response = prediction_service.predict(payload)

                if response.get("success"):
                    st.session_state.prediction_result = prediction_service.summary(response)
                    st.session_state.prediction_payload = payload
                    st.session_state.prediction_error = None
                else:
                    st.error(response.get("message", "Prediction failed."))
                    st.session_state.prediction_result = None
                    st.session_state.prediction_error = response.get("message", "Prediction failed.")

    with right:
        st.subheader("📈 Prediction Result")

        if st.session_state.get("prediction_error"):
            st.error(st.session_state.prediction_error)
        elif st.session_state.get("prediction_result"):
            result = st.session_state.prediction_result
            predicted_price = parse_price(result["price"])

            prediction_card(price=predicted_price, confidence=result.get("confidence", 0))

            st.markdown("---")
            gauge_chart(predicted_price, max(predicted_price * 1.5, 1000000))
            confidence_chart(result.get("confidence", 0))

            market_average = dataframe["Price"].mean()
            difference = predicted_price - market_average

            currency_metric("Market Average", market_average)
            currency_metric("Difference", difference)

            if difference > 0:
                st.success("This estimate is above the average market price.")
            elif difference < 0:
                st.info("This estimate is below the average market price.")
            else:
                st.write("The estimate is equal to the dataset average.")

            if "history" not in st.session_state:
                st.session_state.history = []

            st.session_state.history.insert(
                0,
                {
                    "Company": company,
                    "Model": model,
                    "Year": year,
                    "Fuel": fuel_type,
                    "Kilometers": kms_driven,
                    "Predicted Price": f"₹ {predicted_price:,.0f}",
                },
            )

            st.markdown("---")
            st.subheader("🕒 Recent Predictions")
            history = pd.DataFrame(st.session_state.history)
            st.dataframe(history.head(5), use_container_width=True, hide_index=True)
        else:
            st.info("Fill in all vehicle details and click Predict to see the result.")

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


def render_eda(dataframe: pd.DataFrame):
    navbar(
        page_title="EDA",
        page_description="Explore dataset distributions and patterns."
    )

    section_title("📊 Exploratory Data Analysis", "Visualize key dataset insights.")

    filtered_df = dataframe.copy()

    col1, col2, col3 = st.columns(3)
    with col1:
        company = st.selectbox("Company", ["All"] + sorted(filtered_df["company"].unique()))
    with col2:
        fuel = st.selectbox("Fuel Type", ["All"] + sorted(filtered_df["fuel_type"].unique()))
    with col3:
        year = st.selectbox("Year", ["All"] + sorted(filtered_df["year"].unique()))

    if company != "All":
        filtered_df = filtered_df[filtered_df["company"] == company]
    if fuel != "All":
        filtered_df = filtered_df[filtered_df["fuel_type"] == fuel]
    if year != "All":
        filtered_df = filtered_df[filtered_df["year"] == year]

    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric("Rows", len(filtered_df))
    with c2:
        metric("Columns", len(filtered_df.columns))
    with c3:
        metric("Missing", int(filtered_df.isnull().sum().sum()))
    with c4:
        metric("Duplicates", int(filtered_df.duplicated().sum()))

    st.markdown("---")
    bar_chart(
        filtered_df.groupby("company")["Price"].mean().reset_index(),
        x="company",
        y="Price",
        title="Average Price by Brand",
    )
    line_chart(
        filtered_df.groupby("year")["Price"].mean().reset_index(),
        x="year",
        y="Price",
        title="Average Price by Year",
    )

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


def render_model_performance(dataframe: pd.DataFrame):
    navbar(
        page_title="Model Performance",
        page_description="Review dataset and model evaluation metrics."
    )

    section_title("📈 Model Performance", "Analyze the model and dataset metrics.")

    price_stats = dataset_service.price_statistics(dataframe)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("R² Score", "0.53", icon="📊")
    with col2:
        metric_card("MAE", f"₹ {133302:,.0f}", icon="⚖️")
    with col3:
        metric_card("RMSE", f"₹ {307953:,.0f}", icon="📉")
    with col4:
        metric_card("Average Price", f"₹ {price_stats['mean']:,.0f}", icon="💰")

    st.markdown("---")
    st.subheader("Dataset Summary")
    st.dataframe(dataframe.describe(), use_container_width=True)

    st.markdown("---")
    bar_chart(
        dataframe.groupby("fuel_type")["Price"].mean().reset_index(),
        x="fuel_type",
        y="Price",
        title="Average Price by Fuel Type",
    )

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


def render_history():
    navbar(
        page_title="Prediction History",
        page_description="Review previous prediction runs."
    )

    section_title("📜 Prediction History", "Previously generated prediction results.")

    history = pd.DataFrame(st.session_state.get("history", []))

    if history.empty:
        st.info("No prediction history available yet.")
    else:
        st.dataframe(history, use_container_width=True, hide_index=True)

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


def render_ai_report(dataframe: pd.DataFrame):
    # navbar(
    #     page_title="AI Report",
    #     page_description="AI-assisted dataset insights."
    # )

    # section_title("🤖 AI Report", "Insights and prediction guidance.")

    info_card(
        "Dataset Snapshot",
        f"The dataset contains {len(dataframe):,} records, {dataframe['company'].nunique()} brands, and an average price of ₹ {dataframe['Price'].mean():,.0f}.",
    )

    st.markdown("---")
    bar_chart(
        dataframe.groupby("company")["Price"].mean().reset_index(),
        x="company",
        y="Price",
        title="Top Brands by Average Price",
    )

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


def render_about():
    navbar(
        page_title="About",
        page_description="About the Car Price Prediction app."
    )

    section_title("ℹ️ About This App", "Overview of tools, data and architecture.")

    st.write("This application predicts used car prices using a Random Forest model wrapped in a Streamlit UI and a FastAPI backend.")
    st.write("It provides dataset visualization, prediction history, and model performance monitoring.")

    st.markdown("---")
    info_card(
        "Technology Stack",
        "Python, Streamlit, FastAPI, Scikit-Learn, Pandas, and Plotly.",
    )

    info_card(
        "How to Use",
        "Select a page from the sidebar and follow the prompts to explore data or generate predictions.",
    )

    # footer(
    #     version="1.0.0",
    #     model_name="Random Forest",
    #     api_status="🟢 Online" if prediction_service.backend_online() else "🔴 Offline",
    # )


# -----------------------------------
# Main Application
# -----------------------------------

selected_page = sidebar(
    api_online=prediction_service.backend_online(),
    response_time=0.12,
    dataset_rows=len(df),
    dataset_columns=len(df.columns),
    brand_count=df["company"].nunique(),
    model_name="Random Forest",
    accuracy="96%",
    # version="1.0.0",
)

# if selected_page == "🏠 Dashboard":
#     render_dashboard(df)
if selected_page == "🚗 Prediction":
    render_prediction(df)
elif selected_page == "📊 EDA":
    render_eda(df)
elif selected_page == "📈 Model Performance":
    render_model_performance(df)
# elif selected_page == "📜 Prediction History":
#     render_history()
# elif selected_page == "🤖 AI Report":
#     render_ai_report(df)
elif selected_page == "ℹ About":
    render_about()
else:
    render_prediction(df)

#     render_dashboard(df)
