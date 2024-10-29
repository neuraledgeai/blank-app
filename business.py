import joblib

class Model:
  def __init__(
    self,
    model_name = "india_gdp_forecasting_model.pkl"
  ):
    self.model = joblib.load(model_name)
    
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

      # Make prediction and update the corresponding year 
      predicted_gdp = model.predict(X)
      corresponding_year = corresponding_year + 1
      
      # Add predicted_gdp and corresponding_year to predicted_gdps and corresponding_years lists
      predicted_gdps.append(predicted_gdp)
      corresponding_years.append(corresponding_year)

    data = {
      "Year" : corresponding_years,
      "GDP" : predicted_gdps
    }
    df = pd.DataFrame(data)
    
    return df
