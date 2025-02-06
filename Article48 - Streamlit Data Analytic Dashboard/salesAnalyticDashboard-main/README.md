# A sales analytic dashboard app

This is a modification from [Trigger a full-script rerun from inside a fragment](https://docs.streamlit.io/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment).

I add the following additional data analytic features to the dashboard:
1. Sales trends analysis:
<br>Add line charts to visualize sales trends for individual products over time.

2. Comparison of products:
<br>Allow users to select multiple products and compare their sales trends side-by-side.

3. Monthly aggregate analysis:
<br>Add an aggregated table for monthly sales totals and average sales per product.

4. Outlier detection:
<br>Highlight dates where sales significantly deviate from the average.

5. Download option:
<br>Allow users to download filtered or full sales data as a CSV file.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://salesanalyticdashboard.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
