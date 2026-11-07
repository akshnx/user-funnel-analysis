"""FunnelLens – e-commerce funnel analytics for REES46-style event data.

Run with:  streamlit run app.py
"""
from pathlib import Path

import streamlit as st

import config
from ui import components as c
from ui import layout
from ui.theme import inject_css

ROOT = Path(__file__).parent

st.set_page_config(page_title=config.APP_NAME, page_icon=str(ROOT / "assets" / "icon.svg"),
                   layout="wide", initial_sidebar_state="collapsed")
inject_css()
st.logo(str(ROOT / "assets" / "logo.svg"), size="large", icon_image=str(ROOT / "assets" / "icon.svg"))

pages = [
    st.Page("views/overview.py", title="Overview", url_path="overview", default=True),
    st.Page("views/funnel.py", title="Funnel", url_path="funnel"),
    st.Page("views/segmentation.py", title="Segmentation", url_path="segmentation"),
    st.Page("views/time_analysis.py", title="Time Analysis", url_path="time"),
    st.Page("views/insights.py", title="Insights", url_path="insights"),
    st.Page("views/data.py", title="Data", url_path="data"),
]
pg = st.navigation(pages, position="top")
c.user_chip(config.USER_NAME)

# `?demo` in the URL loads the sample data straight away (handy for demos)
if "df" not in st.session_state and "demo" in st.query_params:
    layout.load_sample()

st.session_state["_ctx"] = layout.render_header(pg.title, show_filters=pg.title != "Data")
pg.run()
c.count_up_script()
