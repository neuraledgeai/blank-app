import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

st.set_page_config(
    page_title="India GDP Forecasting Tool",
    layout="wide",
)

pc = PresentationComponents()

st.sidebar.header("Navigate the Dashboard Yes")
navigation = st.sidebar.radio(
    "Dive into the Data!",
    ["GDP Forecast :blue[Bar Chart]", "GDP Forecast :blue[Line Chart]", "Model Performance", "Download Forecasted Data", "GDP Growth"],
    captions=[
        "Visual Representation",
        "Visual Representation.",
        "Visual Representation",
        "CSV file",
        "Visual Representation"
    ],
)
# Home section
if navigation == "GDP Forecast :blue[Bar Chart]":
    st.subheader("GDP Forecast :blue[Bar Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.forecast_bar_chart(years = years+1)
elif navigation == "GDP Forecast :blue[Line Chart]":
    st.subheader("GDP Forecast :blue[Line Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.forecast_line_chart(years = years+1)
elif navigation == "Model Performance":
    pc.modelPerformance()
elif navigation == "Download Forecasted Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif navigation == "GDP Growth":
    pc.resilientEconomy()
    
