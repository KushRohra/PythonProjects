import yfinance as yf
import streamlit as st
import pandas as pandas

from datetime import date, timedelta

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

days = 365
endDate = date.today()
startDate = str(endDate - timedelta(days=days))
endDate = str(endDate)

tickerDf = tickerData.history(period='1d', start=startDate, end=endDate)

st.write("""**Closing Price**""")
st.line_chart(tickerDf.Close)

st.write("""**Volume**""")
st.line_chart(tickerDf.Volume)
