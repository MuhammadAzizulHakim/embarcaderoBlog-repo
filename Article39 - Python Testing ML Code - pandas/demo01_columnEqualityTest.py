import pandas as pd
 
def startswith_s(df, input_col, output_col):
    df[output_col] = df[input_col].str.startswith("s")
 
df = pd.DataFrame({"col1": ["sap", "hi"], "col2": [3, 4]})

startswith_s(df, "col1", "col1_startswith_s")
expected = pd.Series([True, False], name="col1_startswith_s")
pd.testing.assert_series_equal(df["col1_startswith_s"], expected)