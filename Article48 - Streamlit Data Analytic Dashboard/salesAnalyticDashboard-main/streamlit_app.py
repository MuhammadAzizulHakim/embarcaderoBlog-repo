import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import string
import time

@st.cache_data
def get_data():
    """Generate random sales data for Widget A through Widget Z"""
    product_names = ["Widget " + letter for letter in string.ascii_uppercase]
    average_daily_sales = np.random.normal(1_000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))

    data = pd.DataFrame({})
    sales_dates = np.arange(date(2024, 1, 1), date(2025, 1, 1), timedelta(days=1))
    for product, sales in products.items():
        data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
    data.index = sales_dates
    data.index = data.index.date
    return data

@st.fragment
def show_daily_sales(data):
    time.sleep(1)
    with st.container(height=100):
        selected_date = st.date_input(
            "Pick a day ",
            value=date(2024, 1, 1),
            min_value=date(2024, 1, 1),
            max_value=date(2024, 12, 31),
            key="selected_date",
        )

    if "previous_date" not in st.session_state:
        st.session_state.previous_date = selected_date
    previous_date = st.session_state.previous_date
    st.session_state.previous_date = selected_date
    is_new_month = selected_date.replace(day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()

    with st.container(height=510):
        st.header(f"Best sellers, {selected_date:%m/%d/%y}")
        top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(top_ten)
        cols[1].bar_chart(top_ten)

    with st.container(height=510):
        st.header(f"Worst sellers, {selected_date:%m/%d/%y}")
        bottom_ten = data.loc[selected_date].sort_values()[0:10]
        cols = st.columns([1, 4])
        cols[0].dataframe(bottom_ten)
        cols[1].bar_chart(bottom_ten)

def show_monthly_sales(data):
    time.sleep(1)

    # Ensure `selected_date` is initialized in session state
    if "selected_date" not in st.session_state:
        st.session_state.selected_date = date(2024, 1, 1)  # Default value

    selected_date = st.session_state.selected_date
    this_month = selected_date.replace(day=1)
    next_month = (selected_date.replace(day=28) + timedelta(days=4)).replace(day=1)

    st.container(height=100, border=False)
    with st.container(height=510):
        st.header(f"Daily sales for all products, {this_month:%B %Y}")
        monthly_sales = data[(data.index < next_month) & (data.index >= this_month)]
        st.write(monthly_sales)
    with st.container(height=510):
        st.header(f"Total sales for all products, {this_month:%B %Y}")
        st.bar_chart(monthly_sales.sum())

def show_sales_trends(data):
    time.sleep(1)
    with st.container(height=100):
        st.header("Sales Trends by Product")
        selected_products = st.multiselect(
            "Select Products", options=data.columns, default=[data.columns[0]]
        )

    with st.container(height=510):
        st.line_chart(data[selected_products])

def compare_products(data):
    time.sleep(1)
    with st.container(height=100):
        st.header("Compare Products")
        selected_products = st.multiselect(
            "Select Products to Compare", options=data.columns, default=[data.columns[0], data.columns[1]]
        )

    with st.container(height=510):
        st.bar_chart(data[selected_products].sum())

def show_outliers(data):
    time.sleep(1)
    with st.container(height=100):
        st.header("Outlier Detection")

    daily_averages = data.mean()
    daily_std = data.std()
    outliers = data[(data < daily_averages - 2 * daily_std) | (data > daily_averages + 2 * daily_std)].dropna(how="all")

    with st.container(height=510):
        if not outliers.empty:
            st.subheader("Detected Outliers")
            st.dataframe(outliers)
        else:
            st.subheader("No significant outliers detected.")

def download_data(data):
    time.sleep(1)
    with st.container(height=100):
        st.header("Download Data")

    csv = data.to_csv().encode("utf-8")
    st.download_button(
        label="Download full dataset as CSV",
        data=csv,
        file_name="sales_data.csv",
        mime="text/csv",
    )

st.set_page_config(layout="wide")

st.title("Enhanced Sales Analytics Dashboard")
st.markdown("Explore daily and monthly sales data with additional analytics features.")

data = get_data()
daily, monthly, trends, compare, outliers, download = st.tabs([
    "Daily Sales",
    "Monthly Sales",
    "Sales Trends",
    "Compare Products",
    "Outlier Detection",
    "Download Data",
])

with daily:
    show_daily_sales(data)
with monthly:
    show_monthly_sales(data)
with trends:
    show_sales_trends(data)
with compare:
    compare_products(data)
with outliers:
    show_outliers(data)
with download:
    download_data(data)