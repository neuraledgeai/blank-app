from business import Model
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

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
    fig = px.bar(
        df, 
        x="Year", 
        y="GDP", 
        title=f"GDP Forecast Over the Next {years-1} Years",
        text="GDP"
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
        marker_color="dodgerblue",  
        marker_line_color="black",  
        marker_line_width=1.5,
        texttemplate="%{text:.2s}",
        textposition="outside" 
    )
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
      
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
    if(years > 17):
      st.warning("Forecasting too far into the future may reduce accuracy.", icon="⚠️")
      
    st.plotly_chart(fig)

  def modelPerformance(self):
    st.subheader("Hi")
    df = self.model.predict()
    
    # Reset the index to make 'Year' a column
    df = df.reset_index()
    fig = px.line(df, x="Year", y=["GDP", "Predicted GDP"], title="Actual vs Predicted GDP Over Time")

    st.plotly_chart(fig)
