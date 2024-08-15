import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import yfinance as yf
import datetime
import Capm_functions
import matplotlib.pyplot as plt

# ... rest of your code
from CAPM_return import stocks_list, stocks_daily_return


def calculate_beta_page():
    st.title("Calculate Beta")

    # Select stock
    stock = st.selectbox("Choose a stock", stocks_list)

    # Calculate beta
    beta_value = Capm_functions.calculate_beta(stocks_daily_return, stock)[0]

    # Display beta
    st.write(f"Beta for {stock}: {beta_value:.2f}")

    # Visualize beta
    plt.figure(figsize=(8, 6))
    plt.scatter(stocks_daily_return['SP500'], stocks_daily_return[stock])
    plt.xlabel('S&P 500 Returns')
    plt.ylabel(f'{stock} Returns')
    plt.title(f'Beta for {stock}: {beta_value:.2f}')
    plt.grid(True)
    st.pyplot(plt)

# Add a new page to the app
page_names = ["CAPM", "Calculate Beta"]
page = st.sidebar.selectbox("Select Page", page_names)

if page == "CAPM":
    st.title("CAPM")
    st.write("This page will explain the Capital Asset Pricing Model (CAPM).")

    # Add more content here about CAPM
elif page == "Calculate Beta":
    calculate_beta_page()
