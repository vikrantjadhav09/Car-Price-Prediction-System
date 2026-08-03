"""
=========================================================
Reusable Navigation Bar
AI Powered Car Price Prediction System
=========================================================
"""

from __future__ import annotations

from datetime import datetime
import streamlit as st


# =====================================================
# NAVBAR CSS
# =====================================================

def load_navbar_css():
    """
    Load navbar styles.
    """

    st.markdown(
        """
<style>

/* ==========================================
Navbar
========================================== */

.navbar{

background:linear-gradient(90deg,#0F766E,#115E59);

color:#white;

padding:18px 28px;

margin-bottom:25px;

}

.nav-title{

font-size:28px;

font-weight:700;

color:white;

}

.nav-subtitle{

font-size:14px;

color:white;

margin-top:5px;

}

.page-title{

font-size:34px;

font-weight:bold;

margin-top:10px;

}

.page-description{

color:white;

font-size:15px;

margin-top:6px;

}

/* Breadcrumb */

.breadcrumb{

color:#9CA3AF;

font-size:14px;

margin-top:8px;

}

/* Divider */

.nav-divider{

border-top:1px solid #E5E7EB;

margin-top:18px;

margin-bottom:18px;

}

</style>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# NAVBAR
# =====================================================

def navbar(
    page_title: str,
    page_description: str = "",
):
    """
    Reusable top navigation.
    """

    load_navbar_css()

    today = datetime.now()

    st.markdown(
        f"""
<div class="navbar">

<div class="nav-title">

🚗 AI Car Price Prediction

</div>

<div class="nav-subtitle">

End-to-End Machine Learning Platform

</div>

<div class="nav-divider"></div>

<div class="breadcrumb">

🏠 Home / {page_title}

</div>

<div class="page-title">

{page_title}

</div>

<div class="page-description">

{page_description}

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([2, 1, 1])

    with c1:

        st.caption(
            f"📅 {today.strftime('%d %B %Y')}"
        )

    with c2:

        st.caption(
            f"🕒 {today.strftime('%I:%M %p')}"
        )

    with c3:

        st.caption(
            "🟢 System Online"
        )


# =====================================================
# PAGE HEADER
# =====================================================

def page_header(
    title,
    subtitle=""
):
    """
    Section header.
    """

    st.markdown(f"# {title}")

    if subtitle:

        st.caption(subtitle)

    st.divider()


# =====================================================
# QUICK ACTIONS
# =====================================================

def quick_actions():
    """
    Common action buttons.
    """

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.button(
            "🚗 New Prediction",
            width="stretch"
        )

    with col2:

        st.button(
            "📊 Dashboard",
            width="stretch"
        )

    with col3:

        st.button(
            "📈 Analytics",
            width="stretch"
        )

    with col4:

        st.button(
            "⚙ Settings",
            width="stretch"
        )

    st.write("")


# =====================================================
# SEARCH BAR
# =====================================================

def search_bar(
    placeholder="Search..."
):
    """
    Global search box.
    """

    return st.search_input(
        placeholder
    )


# =====================================================
# API STATUS
# =====================================================

def api_status(
    online=True,
    response_time=0.18
):
    """
    API status indicator.
    """

    col1, col2 = st.columns([2, 1])

    with col1:

        if online:

            st.success(
                "🟢 FastAPI Server Online"
            )

        else:

            st.error(
                "🔴 FastAPI Server Offline"
            )

    with col2:

        st.metric(
            "Response",
            f"{response_time:.2f}s"
        )


# =====================================================
# USER PROFILE
# =====================================================

def user_profile(
    name="Guest",
    role="ML Engineer"
):
    """
    User information card.
    """

    with st.container(border=True):

        st.markdown("### 👤 User")

        st.write(f"**Name:** {name}")

        st.write(f"**Role:** {role}")

        st.write(
            f"**Login:** {datetime.now().strftime('%d-%m-%Y')}"
        )


# =====================================================
# NOTIFICATION PANEL
# =====================================================

def notifications():
    """
    Recent notifications.
    """

    with st.expander("🔔 Notifications"):

        st.success(
            "Model Loaded Successfully"
        )

        st.info(
            "Dataset Ready"
        )

        st.success(
            "Backend Connected"
        )

        st.warning(
            "Gemini AI Integration Pending"
        )


# =====================================================
# DASHBOARD TOOLS
# =====================================================

def dashboard_tools():
    """
    Utility actions.
    """

    col1, col2, col3 = st.columns(3)

    with col1:

        refresh = st.button(
            "🔄 Refresh",
            width="stretch"
        )

    with col2:

        export = st.button(
            "📥 Export",
            width="stretch"
        )

    with col3:

        settings = st.button(
            "⚙ Settings",
            width="stretch"
        )

    return {
        "refresh": refresh,
        "export": export,
        "settings": settings
    }


# =====================================================
# NAVIGATION PILLS
# =====================================================

def navigation_tabs():
    """
    Top navigation selector.
    """

    return st.radio(

        "Navigation",

        [

            "🏠 Dashboard",

            "🚗 Prediction",

            "📊 Analytics",

            "ℹ About"

        ],

        horizontal=True,

        label_visibility="collapsed"

    )


# =====================================================
# PAGE BREADCRUMB
# =====================================================

def breadcrumb(*items):
    """
    Display breadcrumb navigation.
    """

    text = " / ".join(items)

    st.caption(f"📍 {text}")


# =====================================================
# APP STATUS
# =====================================================

def application_status():
    """
    Complete application status.
    """

    st.info(
        """
Application Status

✅ Streamlit Running

✅ FastAPI Connected

✅ ML Model Loaded

✅ Dataset Ready

🟡 Gemini AI Coming Soon
"""
    )


# =====================================================
# SYSTEM INFO
# =====================================================

def system_information():
    """
    Runtime information.
    """

    import platform
    import sys

    with st.expander("💻 System Information"):

        st.write(
            f"**Python:** {platform.python_version()}"
        )

        st.write(
            f"**Operating System:** {platform.system()}"
        )

        st.write(
            f"**Streamlit:** {st.__version__}"
        )

        st.write(
            f"**Architecture:** {platform.machine()}"
        )


# =====================================================
# PAGE ACTIONS
# =====================================================

def page_actions():
    """
    Standard page buttons.
    """

    c1, c2, c3 = st.columns(3)

    with c1:

        st.button(
            "⬅ Back",
            width="stretch"
        )

    with c2:

        st.button(
            "🏠 Home",
            width="stretch"
        )

    with c3:

        st.button(
            "➡ Next",
            width="stretch"
        )

