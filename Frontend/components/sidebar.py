"""
=========================================================
Reusable Sidebar Component
AI Powered Car Price Prediction System
=========================================================
"""

from __future__ import annotations

from datetime import datetime
import streamlit as st

# =====================================================
# CSS
# =====================================================

def load_sidebar_css():
    """
    Sidebar styling.
    """

    st.markdown(
        """
<style>

.sidebar-title{
    font-size:28px;
    font-weight:bold;
    color:#2563EB;
}

.sidebar-subtitle{
    color:#6B7280;
    font-size:14px;
}

.sidebar-section{
    margin-top:15px;
    margin-bottom:15px;
}

.small-text{
    font-size:13px;
    color:#6B7280;
}

</style>
""",
        unsafe_allow_html=True
    )


# =====================================================
# SIDEBAR HEADER
# =====================================================

def sidebar_header():

    load_sidebar_css()

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">🚗 AI Car Price</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="sidebar-subtitle">Production Grade ML Application</div>',
            unsafe_allow_html=True
        )

        st.divider()


# =====================================================
# NAVIGATION
# =====================================================

def sidebar_navigation():

    with st.sidebar:

        page = st.radio(

            "Navigation",

            [

                "🏠 Dashboard",

                "🚗 Prediction",

                "📊 EDA",

                "📈 Model Performance",

                "📜 Prediction History",

                "ℹ About"

            ],

            label_visibility="collapsed"

        )

    return page


# =====================================================
# QUICK ACTIONS
# =====================================================

def sidebar_actions():

    with st.sidebar:

        st.subheader("⚡ Quick Actions")

        predict = st.button(
            "🚗 New Prediction",
            width="stretch"
        )

        analytics = st.button(
            "📊 Analytics",
            width="stretch"
        )

        refresh = st.button(
            "🔄 Refresh",
            width="stretch"
        )

    return {

        "predict": predict,

        "analytics": analytics,

        "refresh": refresh

    }


# =====================================================
# PROJECT INFO
# =====================================================

def project_info():

    with st.sidebar:

        st.divider()

        st.subheader("📌 Project")

        st.write("Version : **1.0.0**")

        st.write("Model : **Random Forest**")

        st.write("Frontend : **Streamlit**")

        st.write("Backend : **FastAPI**")


# =====================================================
# CURRENT DATE
# =====================================================

def current_date():

    with st.sidebar:

        st.divider()

        st.caption(
            f"📅 {datetime.now().strftime('%d %B %Y')}"
        )


# =====================================================
# QUICK LINKS
# =====================================================

def quick_links():

    with st.sidebar:

        st.divider()

        st.subheader("🔗 Resources")

        st.markdown(
            "- 📘 Documentation\n"
            "- 🐍 Python\n"
            "- ⚡ FastAPI\n"
            "- 📊 Streamlit\n"
            "- 🤖 Machine Learning"
        )


# =====================================================
# COMPLETE SIDEBAR
# =====================================================

def sidebar():

    sidebar_header()

    page = sidebar_navigation()

    sidebar_actions()

    project_info()

    current_date()

    quick_links()

    return page


# =====================================================
# API STATUS
# =====================================================

def api_status(
    online=True,
    response_time=0.18
):
    """
    Backend API status.
    """

    with st.sidebar:

        st.divider()

        st.subheader("🌐 Backend Status")

        if online:

            st.success("🟢 FastAPI Online")

        else:

            st.error("🔴 FastAPI Offline")

        st.metric(
            "Response Time",
            f"{response_time:.2f}s"
        )


# =====================================================
# MODEL STATUS
# =====================================================

def model_status(
    model_name="Random Forest",
    accuracy="96.2%",
    version="1.0.0"
):
    """
    Display ML model information.
    """

    with st.sidebar:

        st.divider()

        st.subheader("🤖 ML Model")

        st.metric("Model", model_name)

        st.metric("Accuracy", accuracy)

        st.metric("Version", version)


# =====================================================
# DATASET INFO
# =====================================================

def dataset_info(
    rows=0,
    columns=0,
    brands=0
):
    """
    Dataset summary.
    """

    with st.sidebar:

        st.divider()

        st.subheader("📊 Dataset")

        st.metric("Rows", f"{rows:,}")

        st.metric("Columns", columns)

        st.metric("Brands", brands)


# =====================================================
# USER PROFILE
# =====================================================

def user_profile(
    name="Guest",
    role="AI Engineer"
):
    """
    User information.
    """

    with st.sidebar:

        st.divider()

        st.subheader("👤 User")

        st.write(f"**Name:** {name}")

        st.write(f"**Role:** {role}")


# =====================================================
# THEME
# =====================================================

# def appearance_settings():
#     """
#     UI settings.
#     """

#     with st.sidebar:

#         st.divider()

#         st.subheader("🎨 Appearance")

#         dark_mode = st.toggle(
#             "Dark Mode",
#             value=False
#         )

#         animations = st.toggle(
#             "Animations",
#             value=True
#         )

#     return {

#         "dark_mode": dark_mode,

#         "animations": animations

#     }


# =====================================================
# SYSTEM INFORMATION
# =====================================================

def system_information():

    import platform

    with st.sidebar:

        with st.expander("💻 System Information"):

            st.write(
                f"Python : {platform.python_version()}"
            )

            st.write(
                f"OS : {platform.system()}"
            )

            st.write(
                f"Architecture : {platform.machine()}"
            )


# =====================================================
# SIDEBAR FOOTER
# =====================================================

def sidebar_footer():

    with st.sidebar:

        st.divider()

        st.caption("🚗 AI Car Price Prediction")

        st.caption("Version 1.0.0")

        st.caption("Built with ❤️ using")

        st.caption(
            "Python • Streamlit • FastAPI"
        )


# =====================================================
# COMPLETE SIDEBAR
# =====================================================

def sidebar(
    api_online=True,
    response_time=0.18,
    dataset_rows=0,
    dataset_columns=0,
    brand_count=0,
    model_name="Random Forest",
    accuracy="96%",
    version="1.0.0",
    user_name="Guest",
    role="AI Engineer"
):
    """
    Complete reusable sidebar.
    """

    sidebar_header()

    page = sidebar_navigation()

    sidebar_actions()

    project_info()

    current_date()

    quick_links()

    api_status(
        api_online,
        response_time
    )

    model_status(
        model_name,
        accuracy,
        version
    )

    dataset_info(
        dataset_rows,
        dataset_columns,
        brand_count
    )

    user_profile(
        user_name,
        role
    )

    # appearance_settings()

    # system_information()

    sidebar_footer()

    return page


