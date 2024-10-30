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

  def forecast(self, years):
    df =  self.model.makeForecast(years = range(1, years))
    
    fig = px.bar(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    fig1 = px.line(df, x="Year", y="GDP", title="GDP Forecast Over the Years")
    st.plotly_chart(fig)
    st.plotly_chart(fig1)
