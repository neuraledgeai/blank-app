from bussiness import Model
import streamlit as st

class IndiaGDPApp:
  def __init__(
    #model = Model()
  ):
    self.model = Model()

  def forecast(self, years):
    forcast_data =  model.makeForecast()
