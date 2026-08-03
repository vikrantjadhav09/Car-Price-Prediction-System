"""
=========================================================
Reusable Card Components
AI Powered Car Price Prediction System
=========================================================
"""

from __future__ import annotations

import streamlit as st


# =====================================================
# LOAD CSS
# =====================================================

def load_card_css():
    """Load reusable card styles."""

    st.markdown(
        """
<style>

/* ---------- Metric Card ---------- */

.metric-card{
    background:#FFFFFF;
    border:1px solid #E5E7EB;
    border-radius:18px;
    padding:22px;
    text-align:center;
    box-shadow:0 4px 15px rgba(0,0,0,.06);
    transition:0.25s;
}

.metric-card:hover{
    transform:translateY(-5px);
    box-shadow:0 10px 25px rgba(37,99,235,.15);
}

.metric-icon{
    font-size:38px;
}

.metric-title{
    font-size:15px;
    color:#6B7280;
    margin-top:8px;
}

.metric-value{
    font-size:30px;
    font-weight:bold;
    color:#2563EB;
}

/* ---------- Info Card ---------- */

.info-card{
    background:#F8FAFC;
    border-radius:18px;
    padding:22px;
    border-left:5px solid #2563EB;
    border:1px solid #E5E7EB;
    margin-bottom:15px;
    box-shadow:0 3px 10px rgba(0,0,0,.05);
}

.info-title{
    font-size:20px;
    font-weight:600;
    margin-bottom:8px;
}

.info-content{
    color:#4B5563;
    line-height:1.7;
}

/* ---------- Status Card ---------- */

.status-card{

    background:#F8FAFC;

    padding:18px;

    border-radius:15px;

    border:1px solid #E5E7EB;

    box-shadow:0 3px 12px rgba(0,0,0,.05);

    margin-bottom:12px;

}

/* ---------- Result Card ---------- */

.result-card{

    background:linear-gradient(
        135deg,
        #2563EB,
        #1E3A8A
    );

    color:white;

    border-radius:18px;

    padding:30px;

    text-align:center;

}

.result-price{

    font-size:42px;

    font-weight:bold;

}

.result-label{

    font-size:18px;

    opacity:.9;

}

/* ---------- AI Card ---------- */

.ai-card{

    background:#EFF6FF;

    border-radius:18px;

    border-left:6px solid #2563EB;

    padding:22px;

    margin-top:10px;

}

/* ---------- Warning ---------- */

.warning-card{

    background:#FEF3C7;

    border-left:5px solid #F59E0B;

    padding:20px;

    border-radius:15px;

    margin-top:10px;

}

/* ---------- Success ---------- */

.success-card{

    background:#ECFDF5;

    border-left:5px solid #10B981;

    padding:20px;

    border-radius:15px;

    margin-top:10px;

}

</style>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# METRIC CARD
# =====================================================

def metric_card(
    title: str,
    value,
    icon: str = "📊",
):
    """Beautiful KPI card."""

    load_card_css()

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-icon">{icon}</div>

<div class="metric-value">{value}</div>

<div class="metric-title">{title}</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# INFO CARD
# =====================================================

def info_card(
    title: str,
    content: str,
):
    """Information card."""

    load_card_css()

    st.markdown(
        f"""
<div class="info-card">

<div class="info-title">
{title}
</div>

<div class="info-content">
{content}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# STATUS CARD
# =====================================================

def status_card(
    title: str,
    status: str,
):
    """Status card."""

    load_card_css()

    st.markdown(
        f"""
<div class="status-card">

<b>{title}</b>

<br><br>

{status}

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# RESULT CARD
# =====================================================

def prediction_card(
    price,
    confidence=96,
):
    """Prediction result card."""

    load_card_css()

    st.markdown(
        f"""
<div class="result-card">

<div class="result-label">

Estimated Price

</div>

<div class="result-price">

₹ {price:,.0f}

</div>

<br>

Confidence

<b>{confidence}%</b>

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# AI SUMMARY CARD
# =====================================================

def ai_summary_card(
    summary: str,
):
    """AI generated summary."""

    load_card_css()

    st.markdown(
        f"""
<div class="ai-card">

<h3>🤖 AI Analysis</h3>

<p>{summary}</p>

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# SUCCESS CARD
# =====================================================

def success_card(message: str):
    """Success card."""

    load_card_css()

    st.markdown(
        f"""
<div class="success-card">

✅ {message}

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# WARNING CARD
# =====================================================

def warning_card(message: str):
    """Warning card."""

    load_card_css()

    st.markdown(
        f"""
<div class="warning-card">

⚠️ {message}

</div>
""",
        unsafe_allow_html=True,
    )


# =====================================================
# SECTION TITLE
# =====================================================

def section_title(
    title: str,
    subtitle: str = "",
):
    """Beautiful section header."""

    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)

    st.divider()


# =====================================================
# EMPTY STATE
# =====================================================

def empty_state(
    title="No Data Found",
    description="Nothing to display."
):
    """Empty state component."""

    st.info(f"""
### 📭 {title}

{description}
""")


# =====================================================
# LOADING CARD
# =====================================================

def loading_card(
    text="Loading..."
):
    """Loading placeholder."""

    with st.spinner(text):
        pass