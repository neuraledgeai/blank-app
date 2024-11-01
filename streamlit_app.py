import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

pc = PresentationComponents()
#years = st.slider("Forecast Horizon", 0, 20, 5)
#pc.forecast_line_chart(years = years+1)
#pc.forecast_bar_chart(years = years+1)
#pc.downloadData(years = years+1)

st.sidebar.header("Navigate the Dashboard")
navigation = st.sidebar.radio(
    "What's your favorite movie genre",
    ["GDP Forecast :blue[Bar Chart]", "GDP Forecast :blue[Line Chart]", "Download Forecast Data"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
# Home section
if navigation == "GDP Forecast :blue[Bar Chart]":
    st.subheader("GDP Forecast :blue[Bar Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 5)
    pc.forecast_bar_chart(years = years+1)
    st.write("The GDP Forecast Bar Chart provides a visual representation of India’s projected GDP growth over the selected number of years. Each bar represents a specific year's forecasted GDP value, displayed in trillions of US dollars.")
