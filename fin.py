#stock price app

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.header("Stock Price App")

input_ticker = st.text_input("Enter Stock Ticker", value="AAPL")

ticker_data= yf.Ticker(input_ticker) #Ticker is a class in yfinance and ticker_data is object of that class

col1, col2 = st.columns(2)

with col1:
    start_dt = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))

with col2:
    end_dt = st.date_input("End Date", value=pd.to_datetime("2026-01-01"))

ticker_df = ticker_data.history(start=start_dt,
                                end=end_dt) #here we can specify the period we want to analyze

# create a stramlit df 
st.dataframe(ticker_df)

st.line_chart(ticker_df.Close)

st.line_chart(ticker_df.Open)