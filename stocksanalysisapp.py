import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Stock Market Dashboard")

# Sidebar inputs
st.sidebar.header("Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch stock data (single ticker only)
df = yf.download(ticker, start=start_date, end=end_date)

# Fix multi-index columns if they appear
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.droplevel(1)

if df.empty:
    st.warning("No data found. Try another ticker or date range.")
else:
    st.subheader(f"Stock Data for {ticker}")
    st.dataframe(df.tail())

    # --- KPIs ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${df['Close'].iloc[-1]:.2f}")
    col2.metric("52W High", f"${df['High'].max():.2f}")
    col3.metric("52W Low", f"${df['Low'].min():.2f}")

    # --- Line chart (closing price) ---
    fig = px.line(df, x=df.index, y="Close", title=f"{ticker} Closing Price")
    st.plotly_chart(fig, use_container_width=True)

    # --- Volume chart ---
    fig_vol = px.bar(df, x=df.index, y="Volume", title="Trading Volume")
    st.plotly_chart(fig_vol, use_container_width=True)

    # --- Candlestick chart ---
    fig_candle = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])
    fig_candle.update_layout(title=f"{ticker} Candlestick Chart", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_candle, use_container_width=True)

    # --- Moving averages ---
    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    fig_ma = px.line(df, x=df.index, y=["Close", "MA20", "MA50"],
                     title=f"{ticker} Closing Price with Moving Averages")
    st.plotly_chart(fig_ma, use_container_width=True)

    # --- Daily Returns Distribution ---
    df["Daily Return"] = df["Close"].pct_change()
    fig_hist = px.histogram(df, x="Daily Return", nbins=50,
                            title=f"{ticker} Daily Returns Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

    # --- Correlation Heatmap ---
    valid_cols = [c for c in ["Open", "High", "Low", "Close", "Adj Close", "Volume"] if c in df.columns]
    corr = df[valid_cols].corr()

    fig_heatmap = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title=f"{ticker} Correlation Heatmap"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)