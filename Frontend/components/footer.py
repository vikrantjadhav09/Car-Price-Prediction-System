"""
===========================================================
Reusable Footer Component
AI Powered Car Price Prediction System
===========================================================
"""

from datetime import datetime
import streamlit as st


def load_footer_css():
    """
    Inject footer styling.
    """

    st.markdown(
        """
        <style>

        .footer-container{
            margin-top:40px;
            padding:20px;
            border-radius:15px;
            background:#ffffff;
            border:1px solid #E5E7EB;
            box-shadow:0 2px 10px rgba(0,0,0,.06);
        }

        .footer-title{
            font-size:18px;
            font-weight:700;
            color:#2563EB;
            text-align:center;
        }

        .footer-subtitle{
            text-align:center;
            color:#6B7280;
            font-size:14px;
            margin-top:5px;
        }

        .footer-divider{
            margin-top:15px;
            margin-bottom:15px;
            border-top:1px solid #E5E7EB;
        }

        .footer-small{
            text-align:center;
            color:#9CA3AF;
            font-size:13px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def footer(
    version="1.0.0",
    model_name="Random Forest Regressor",
    api_status="🟢 Online",
):
    """
    Display reusable application footer.
    """

    load_footer_css()

    year = datetime.now().year

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Version", version)

    with col2:
        st.metric("ML Model", model_name)

    with col3:
        st.metric("API Status", api_status)

    # st.markdown(
    #     f"""
    #     <div class="footer-container">

    #         <div class="footer-title">
    #             🚗 AI Powered Car Price Prediction System
    #         </div>

    #         <div class="footer-subtitle">
    #             End-to-End Machine Learning • FastAPI • Streamlit • AI
    #         </div>

    #         <div class="footer-divider"></div>

    #         <div class="footer-small">
    #             Built with ❤️ using
    #             <b>Python</b> •
    #             <b>Scikit-Learn</b> •
    #             <b>FastAPI</b> •
    #             <b>Streamlit</b> •
    #             <b>Plotly</b>
    #         </div>

    #         <br>

    #         <div class="footer-small">
    #             © {year} AI Car Price Prediction System
    #         </div>

    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )