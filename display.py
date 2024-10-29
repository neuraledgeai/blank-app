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
    forecasted_df =  self.model.makeForecast(years = range(1, years))
    
    # Plot India's GDP
    fig = px.line(forecasted_df.reset_index(), x='Year', y='GDP', 
                   title="India's GDP from 1961 to 2023",
                   labels={'GDP': 'GDP (in Trillions of USD)', 'Year': 'Year'},
                   markers=True
                  )
    # Show the plot
    #st.plotly_chart(fig)
    return fig


