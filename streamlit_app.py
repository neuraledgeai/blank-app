import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents

st.set_page_config(
    page_title="India GDP Forecasting Tool",
    layout="wide",
)

pc = PresentationComponents()

st.sidebar.header("Navigate the Dashboard")
navigation = st.sidebar.radio(
    "Dive into the Data!",
    ["GDP Forecast", "Resilient Economy", "Model Performance", "Download Forecasted Data"],
    captions=[
        "Visual Representation",
        "Visual Representation",
        "Visual Representation",
        "CSV files"
        
    ],
)
st.sidebar.header("Neural Edge AI")

# Home section
if navigation == "GDP Forecast":
    st.subheader("India's $5 Trillion Economy: :blue[A Data-Driven Perspectivejjj]")
    years = st.slider("Forecast Horizon (number of years)", 0, 20, 7)
    pc.forecast_primary_chart(years = years+1)
    pc.forecast_bar_chart(years = years+1)
elif navigation == "Model Performance":
    pc.modelPerformance()
elif navigation == "Download Forecasted Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif navigation == "Resilient Economy":
    pc.resilientEconomy()
    st.latex(r"\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 \cdot x")
    st.latex(r"\hat{y}: \text{ The predicted value of GDP}")
    st.latex(r"\hat{\beta}_0: \text{ The estimated intercept, representing the base level of GDP when } x \text{ is zero}")
    st.latex(r"\hat{\beta}_1: \text{ The estimated coefficient, showing the rate of change in GDP for each unit increase in } x")
    st.latex(r"x: \text{ The predictor variable, such as year or other factors impacting GDP}")

   
    
