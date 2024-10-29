from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd

class IndiaGDPApp:
  def __init__(
    self,
    model = Model()
  ):
    self.model = model

  def forecast(self, years):
    fig =  self.model.makeForecast(years = range(1, 11))
    st.pyplot(fig)


