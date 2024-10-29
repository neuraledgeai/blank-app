from business import Model
import streamlit as st
import plotly.express as px

class IndiaGDPApp:
  def __init__(
    model = Model()
  ):
    self.model = model

  def forecast(self, years):
    forcast_data =  self.model.makeForecast(years = range(1, 11))
    
    # Plot India's GDP
    fig = px.line(df.reset_index(), x='Year', y='GDP', 
                   title="India's GDP from 1961 to 2023",
                   labels={'GDP': 'GDP (in Trillions of USD)', 'Year': 'Year'},
                   markers=True
                  )
    # Show the plot
    #st.plotly_chart(fig)
    return fig


