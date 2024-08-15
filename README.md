# Captial Asset Pricing Model Analysis (CAPM)

 Project Overview
This project involved developing a web application to calculate and visualize the Beta value of stocks using the Capital Asset Pricing Model (CAPM). The application leverages Python libraries such as Streamlit, Pandas, Matplotlib, Plotly, and yfinance to fetch stock data, perform calculations, and create interactive visualizations.

Key Features
Stock Selection: Users can select up to four stocks from the S&P 500 index for analysis.
Beta Calculation: The application calculates the Beta value for each selected stock relative to the S&P 500 index.

Data Visualization:
Interactive line charts displaying the historical price and return of selected stocks.
Scatter plot visualizing the relationship between the selected stock's returns and the S&P 500 returns to illustrate the Beta concept.
User Interface: A user-friendly Streamlit interface provides an intuitive experience for interacting with the application.

Technical Implementation

Data Acquisition:
Utilized the yfinance library to fetch historical price data for the selected stocks and the S&P 500 index.
Converted the data into a Pandas DataFrame for further analysis.

Data Preprocessing:
Calculated daily returns for each stock and the market index.
Adjusted for dividends and splits to ensure accurate return calculations.

CAPM Calculation:
Implemented the CAPM formula to compute the Beta value for each selected stock.
Calculated the risk-free rate and market risk premium using appropriate financial data sources.

Visualization:
Employed Matplotlib and Plotly libraries to create static and interactive visualizations respectively.
Generated line charts to display historical stock prices and returns.
Created scatter plots to visualize the relationship between stock returns and market returns.

Web Application Development:
Used Streamlit to build the user interface.
Designed interactive components for stock selection and visualization.
Integrated the CAPM calculation and visualization functions into the Streamlit app.

