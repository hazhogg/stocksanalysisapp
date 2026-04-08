# 📈 Stock Market Dashboard

An interactive stock market dashboard built with Streamlit. Enter any stock ticker and date range to instantly visualise price history, trading volume, moving averages, returns distribution, and more — all in your browser.

---

## Features

- **Live stock data** fetched via Yahoo Finance
- **Key metrics** — current price, 52-week high, and 52-week low
- **Closing price chart** — interactive line chart of historical close prices
- **Trading volume** — bar chart of daily volume over the selected period
- **Candlestick chart** — OHLC candlestick view for detailed price action
- **Moving averages** — 20-day and 50-day MAs overlaid on the closing price
- **Daily returns distribution** — histogram of percentage returns
- **Correlation heatmap** — heatmap of relationships between OHLC and volume columns

---

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## Usage

Use the **sidebar** to configure the dashboard:

- **Stock Ticker** — enter any valid Yahoo Finance ticker (e.g. `AAPL`, `TSLA`, `GOOGL`)
- **Start Date** — beginning of the date range
- **End Date** — end of the date range (defaults to today)

All charts update instantly when settings change.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Web app framework |
| `yfinance` | Yahoo Finance data fetching |
| `pandas` | Data manipulation |
| `plotly` | Interactive charts |

Install all dependencies with:

```bash
pip install streamlit yfinance pandas plotly
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
streamlit
yfinance
pandas
plotly
```

---

## Project Structure

```
.
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Screenshots

> Add screenshots of the dashboard here once deployed.

---

## Contributing

Pull requests are welcome! Potential additions — multi-ticker comparison, RSI/MACD indicators, portfolio tracking, or export to CSV — feel free to open an issue.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)
