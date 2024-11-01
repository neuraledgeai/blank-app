import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

#pc = PresentationComponents()
#years = st.slider("Forecast Horizon", 0, 20, 5)
#pc.forecast_line_chart(years = years+1)
#pc.forecast_bar_chart(years = years+1)
#pc.downloadData(years = years+1)

st.sidebar.header("Navigate the Dashboard")
navigation = st.sidebar.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
