#pandas testing example: pandas error messages
import pandas as pd

df = pd.DataFrame({"col1": [1041, 1, 8, 5], "col2": [6, 3, 8, 7]})
pd.testing.assert_series_equal(df["col1"], df["col2"])

#beavis testing example: beavis error messages
import beavis
import pandas as pd

df = pd.DataFrame({"col1": [1041, 3, 8, 5], "col2": [6, 3, 8, 7]})
beavis.assert_pd_column_equality(df, "col1", "col2")
