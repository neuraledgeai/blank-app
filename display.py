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

  def forecast_bar_chart(self,years):
    # Get dataframe
    df =  self.model.makeForecast(years = range(1, years))

    # Plot figure
    fig = px.bar(df, x="Year", y="GDP", title=f"GDP Forecast Over the Next {years-1} Years")
    st.plotly_chart(fig)

  def forecast_line_chart(self, years):
    # Get dataframe
    df =  self.model.makeForecast(years = range(1, years))

    # Plot figure
    fig = px.line(
        df, 
        x="Year", 
        y="GDP", 
        title=f"GDP Forecast Over the Next {years-1} Years",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        template="plotly_white",
        xaxis=dict(
            tickmode="linear",
            tickangle=45,
        )
    )
    fig.update_traces(
        line=dict(color="royalblue", width=3),  
        marker=dict(size=8, color="darkblue")
    )
    st.plotly_chart(fig)
