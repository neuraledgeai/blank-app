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
    st.write(f"The Bar Chart provides a visual representation of India’s projected GDP growth over the next {years} years. Each bar represents a specific year's forecasted GDP value, displayed in trillions of US dollars.")
    st.markdown(''':blue-background[Highlight] : India is expected to touch 5 trillion in GDP at current prices by 2030.''')
    st.markdown("""
    <div style="text-align: center; font-size: 0.8em; color: grey;">
    The model is trained on data only up to 2023, so predictions may vary due to future uncertainties. Please verify important information independently.
    </div>
    """, unsafe_allow_html=True)
