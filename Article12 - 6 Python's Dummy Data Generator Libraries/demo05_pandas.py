import pandas as pd
 
# Create dummy data
pandasDummy = pd.util.testing.makeDataFrame()
# Export the data to .CSV file
pandasDummy.to_csv('pandasExample.csv')