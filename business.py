import joblib

def class DataServer:
  def __init__(
    model_name = "india_gdp_forecasting_model.pkl"
  ):
    self.model = joblib.load(model_name)
def make_forecast(self):
  return self.model
