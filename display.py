from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd

class PresentationComponents:
  def __init__(
    self,
    model = Model()
  ):
    self.model = model

  def forecast_bar_chart(self, years):
    # Get the data frame
    df =  self.model.makeForecast(years = range(1, years))
    # Header
    st.header("GDP Forecast : blue[Bar Chart]")
    # Slider
    years = st.slider("Number of years to forecast", 0, 20, 5)
    fig = px.bar(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    #fig1 = px.line(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    st.plotly_chart(fig)
    #st.plotly_chart(fig1)

  def forecast_line_chart(self, years):
    df =  self.model.makeForecast(years = range(1, years))
    # Header
    st.header("GDP Forecast : blue[Line Chart]")
    fig = px.bar(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    fig1 = px.line(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
