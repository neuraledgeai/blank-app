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
    #fig = px.line(df, x="Year", y="GDP", title=f"GDP Forecast Over the Next {years-1} Years")
    #st.plotly_chart(fig)
    # Create the line plot with customized settings
    fig = px.line(
        df, 
        x="Year", 
        y="GDP", 
        #title=f"GDP Forecast Over the Next {years-1} Years",
        markers=True  # Adds markers to each data point for better visibility
    )
    
    # Customize layout for improved appearance
    fig.update_layout(
        title={
            'text': f"GDP Forecast Over the Next {years-1} Years",
            'y':0.1,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        template="plotly_white",  # Use a clean white theme
        xaxis=dict(
            tickmode='linear',  # Ensure every year is shown
            tickangle=45,
        )
    )
    
    # Update line style and markers for better visibility
    fig.update_traces(
        line=dict(color='royalblue', width=3),  # Set line color and width
        marker=dict(size=8, color='red')        # Make markers larger and red for emphasis
    )
    
    # Display the improved chart in Streamlit
    st.plotly_chart(fig)
