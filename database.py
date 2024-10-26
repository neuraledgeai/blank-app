import pandas as pd

class LocalDatabase:
  
  def __init__(
    self,
    file_name = "gdp_india_1960-2023.csv"
  ):
    self.df = pd.read_csv(file_name)
    
  def getDataFrame(self):
    dataFrame = pd.melt(
        self.df,
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],  # Columns to keep as identifiers
        var_name='Year',      # The name of the new column for the years
        value_name='GDP'      # The name of the new column for the GDP values
    )
    # Setting the 'Year' column as the index and dropping unnecessary columns
    dataFrame = dataFrame.set_index("Year").drop(columns=["Country Name", "Country Code", "Indicator Name", "Indicator Code"])
    # Adding a new feature for GDP_L1
    dataFrame['GDP_L1'] = dataFrame['GDP'].shift(1)
    dataFrame = dataFrame.dropna()  # Drop rows with NaN values resulting from the shift

    return dataFrame
  
