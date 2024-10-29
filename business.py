import joblib

class Model:
  def __init__(
    self,
    model_name = "india_gdp_forecasting_model.pkl"
  ):
    self.model = joblib.load(model_name)
    
  def makeForecast(self):
    return self.model
