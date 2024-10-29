from business import Model
import streamlit as st
import plotly.express as px

class IndiaGDPApp:
  def __init__(
    self,
    model = Model()
  ):
    self.model = model

  def forecast(self, years):
    df =  self.model.makeForecast(years = range(1, 11))
    
    # Plot India's GDP
    fig = px.line(df, x=df.index, y='GDP', title='GDP Over the Years')
    # Show the plot
    #st.plotly_chart(fig)
    return fig


