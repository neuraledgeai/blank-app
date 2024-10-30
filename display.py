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
    #fig = px.bar(df, x="Year", y="GDP", title=f"GDP Forecast Over the Next {years-1} Years")
    #st.plotly_chart(fig)
    # Create the bar plot with customized settings
    fig = px.bar(
        df, 
        x="Year", 
        y="GDP", 
        title=f"GDP Forecast Over the Next {years-1} Years",
        text="GDP"  # Adds GDP values as labels on top of each bar
    )
    
    # Customize layout for improved appearance
    fig.update_layout(
        title={
            'text': f"GDP Forecast Over the Next {years-1} Years",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Year",
        yaxis_title="GDP (in Trillions)",
        template="plotly_white",  # Use a clean white theme
        xaxis=dict(
            tickmode='linear',
            tickangle=45  # Rotate x-axis labels for readability
        ),
        yaxis=dict(
            tickformat=".2f",  # Format y-axis for trillions
            gridcolor="lightgrey"
        )
    )
    
    # Update bar style and text position for better visibility
    fig.update_traces(
        marker_color='dodgerblue',  # Use a visually pleasing blue color for bars
        marker_line_color='black',  # Add a black outline to bars
        marker_line_width=1.5,
        texttemplate='%{text:.2s}',  # Format GDP values on bars
        textposition='outside'  # Place labels outside bars for clarity
    )

# Display the improved bar chart in Streamlit
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
