import streamlit as st
from database import LocalDatabase
from business import Model
from display import PresentationComponents
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="India GDP Forecasting Tool",
    layout="wide",
)

pc = PresentationComponents()

#st.sidebar.header("Navigate the Dashboard")
#navigation = st.sidebar.radio(
    #"Dive into the Data!",
    #["GDP Forecast", "Resilient Economy", "Emperical Results", "Download Forecasted Data"],
    #captions=[
        #"Visual Representation",
        #"Visual Representation",
        #"Visual Representation",
        #"CSV files"
        
    #],
#)
#st.sidebar.header("Neural Edge AI")

with st.sidebar:
    selected = option_menu(
        "GDP-PY", ["Forecast GDP", "Resilient Economy",  "Emperical Results", "Download Forecasted Data"], 
        icons=["bar-chart-fill", "ubuntu", "card-text", "download"],
        #menu_icon="cast",
        default_index=1
    )
    #selected

# Home section
if selected == "GDP Forecast":
    st.subheader("India's $5 Trillion Economy: :blue[A Data-Driven Perspective]")
    years = st.slider("Forecast Horizon (number of years)", 0, 20, 7)
    pc.forecast_primary_chart(years = years+1)
    pc.forecast_bar_chart(years = years+1)
elif selected == "Emperical Results":
    pc.empericalResults()
elif selected == "Download Forecasted Data":
    years = st.slider("Forecast Horizon", 0, 20, 7)
    pc.downloadData(years = years+1)
elif selected == "Resilient Economy":
    #model = Model()
    #intercept = model.intercept()
    #coefficient = model.coef()
    #df, fig = model.regressionChart()
    pc.resilientEconomy()
    #st.subheader("Emperical Results")
    #st.write("The goal of this empirical analysis is to forecast India’s GDP growth trajectory and estimate the specific year in which India is likely to reach a GDP of $5 trillion. To do so, we estimate a linear regression function of the form")
    #st.latex(r"\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 \cdot x_i")
    #st.latex(r"{\text{GDP}_{\text{next year}}} = {\beta}_0 + {\beta}_1 \cdot \text{GDP}_{\text{previous year}}")
    #st.write(f"The independent variable is the GDP value from the previous year, which we use to forecast future values. For example, if you provide the 2023 GDP value as the independent variable, the model will estimate the 2024 GDP based on the estimated intercept *{intercept}* and estimated slope *{coefficient}*.")
    #st.write(f"This is intercept {intercept} and this is coefficient {coefficient[0]}")
    #st.dataframe(df)
    #st.plotly_chart(fig)
    #st.write("Each point represents the GDP of a given year plotted against the GDP of the previous year on the x-axis. The blue line represents the linear regression model fitted to this data.")


   
    
