import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

pc = PresentationComponents()
#years = st.slider("Forecast Horizon", 0, 20, 5)
#pc.forecast_line_chart(years = years+1)
#pc.forecast_bar_chart(years = years+1)
#pc.downloadData(years = years+1)

st.sidebar.header("Navigate the Dashboard Yes")
navigation = st.sidebar.radio(
    "Dive into the Data!",
    ["GDP Forecast :blue[Bar Chart]", "GDP Forecast :blue[Line Chart]", "Model Performance", "Download Forecasted Data"],
    captions=[
        "Visual Representation",
        "Visual Representation.",
        "Visual Representation",
        "CSV file"
    ],
)
# Home section
if navigation == "GDP Forecast :blue[Bar Chart]":
    st.subheader("GDP Forecast :blue[Bar Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 5)
    pc.forecast_bar_chart(years = years+1)
elif navigation == "GDP Forecast :blue[Line Chart]":
    st.subheader("GDP Forecast :blue[Line Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 5)
    pc.forecast_line_chart(years = years+1)
elif navigation == "Model Performance":
    pc.modelPerformance()
elif navigation == "Download Forecasted Data":
    #st.subheader("GDP Forecast :blue[Line Chart]")
    years = st.slider("Forecast Horizon", 0, 20, 5)
    pc.downloadData(years = years+1)
