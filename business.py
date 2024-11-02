import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
from database import LocalDatabase
import pandas as pd
import plotly.express as px

class Model:
  def __init__(
    self,
    model_name = "india_gdp_forecasting_model.pkl",
    db = LocalDatabase()
  ):
    self.model = joblib.load(model_name)
    self.db = db
    
  def makeForecast(self, years):
    # This is GDP for 2023, so that we can start predicting from 2024 to the given number of years
    gdp = 3_353_470_000_000
    corresponding_year = 2023
    
    # To keep predicted GDPs and their corresponding years
    predicted_gdps = []
    corresponding_years = []

    for year in years:
      # Prepare data
      X = np.array([[gdp]])

      # Make prediction and update the corresponding year and gdp
      predicted_gdp = self.model.predict(X)
      corresponding_year = corresponding_year + 1
      gdp = predicted_gdp[0]
      
      # Add predicted_gdp and corresponding_year to predicted_gdps and corresponding_years lists
      predicted_gdps.append(predicted_gdp)
      corresponding_years.append(corresponding_year)

    data = {
      "Year" : corresponding_years,
      "GDP" : predicted_gdps
    }
    df = pd.DataFrame(data)
    df["Year"] = df["Year"].astype(int)
    df["GDP"] = df["GDP"].astype(float)
    
    return df

  def predict(self):
    # Prepare data
    #db = LocalDatabase()
    df = self.db.loadData(lag=True)

    # Split
    feature = ["GDP_L1"]
    X = df[feature]
    
    # Result
    result = pd.DataFrame(
      {
        "GDP" : df["GDP"],
        "GDP_L1" : df["GDP_L1"],
        "Predicted GDP" : self.model.predict(X)
      }
    )
    return result

  def gdpGrowth(self):
    df = self.db.loadData()
    # Reset the index to make 'Year' a column
    df = df.reset_index()
    fig = px.line(df, x="Year", y="GDP", title="Actual vs Predicted GDP Over Time")
    st.plotly_chart(fig)
  
    
  
