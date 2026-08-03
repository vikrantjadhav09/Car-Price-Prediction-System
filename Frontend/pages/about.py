import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

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

# -------------------------------------------------------
# FEATURES
# -------------------------------------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ Machine Learning Prediction")

    st.success("✔ FastAPI REST API")

    st.success("✔ Streamlit Dashboard")

    st.success("✔ Responsive UI")

    st.success("✔ Interactive Forms")

    st.success("✔ Real-Time Prediction")

with col2:

    st.success("✔ AI Powered Explanation")

    st.success("✔ Prediction History")

    st.success("✔ PDF Report Generation")

    st.success("✔ Data Visualization")

    st.success("✔ Docker Support")

    st.success("✔ Cloud Deployment Ready")

st.divider()

# -------------------------------------------------------
# TECHNOLOGY STACK
# -------------------------------------------------------

st.header("🛠 Technology Stack")

cols = st.columns(4)

techs = [
    "🐍 Python",
    "⚡ FastAPI",
    "🎨 Streamlit",
    "🤖 Scikit-Learn",
    "📊 Pandas",
    "🔢 NumPy",
    "📈 Plotly",
    "🧠 Gemini AI"
]

for col, tech in zip(cols * 2, techs):
    with col:
        st.markdown(
            f"""
            <div class="tech">
            <h4>{tech}</h4>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# -------------------------------------------------------
# SYSTEM ARCHITECTURE
# -------------------------------------------------------

st.header("🏗 System Architecture")

st.code("""
User
   │
   ▼
Streamlit Frontend
   │
REST API
   │
   ▼
FastAPI Backend
   │
Prediction Request
   │
   ▼
Machine Learning Model
   │
Prediction
   │
   ▼
AI Explanation
   │
   ▼
Result Dashboard
""")

st.divider()

# -------------------------------------------------------
# MACHINE LEARNING
# -------------------------------------------------------

st.header("🧠 Machine Learning Pipeline")

st.write("""
The prediction model follows a complete Machine Learning workflow:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization
8. FastAPI Deployment
9. Streamlit Integration
""")

st.divider()

# -------------------------------------------------------
# UPCOMING AI FEATURES
# -------------------------------------------------------

st.header("🚀 Upcoming AI Features")

st.info("""
🤖 AI Price Explanation

📉 Future Resale Prediction

📄 PDF Report

🎤 Voice Assistant

💬 AI Chatbot

📊 Advanced Analytics

☁ Cloud Deployment

📈 Price Trend Analysis
""")

st.divider()

# -------------------------------------------------------
# VERSION
# -------------------------------------------------------

st.header("📦 Application Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Version", "1.0.0")

with col2:
    st.metric("ML Model", "Production")

with col3:
    st.metric("API", "FastAPI")

st.divider()

# -------------------------------------------------------
# DEVELOPER
# -------------------------------------------------------

st.header("👨‍💻 Developer")

st.write("""
**Project Name**

AI Powered Car Price Prediction System

**Purpose**

Educational + Portfolio Project

**Built Using**

Python • Streamlit • FastAPI • Scikit-Learn

Designed with scalability,
clean architecture and production deployment in mind.
""")

st.divider()

# -------------------------------------------------------
# THANK YOU
# -------------------------------------------------------

st.success("Thank you for using the AI Powered Car Price Prediction System 🚗")

st.markdown("""
<div class="footer">

Made with ❤️ using

Python • Streamlit • FastAPI • Machine Learning

Version 1.0.0

</div>
""", unsafe_allow_html=True)