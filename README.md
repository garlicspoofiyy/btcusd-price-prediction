# BTCUSD Daily Price Prediction

This project is a web application that predicts the daily price movement of Bitcoin (BTC) against the US Dollar (USD) using XGBoostClassifier and technical indicators. The application is built using Flask and displays predictions on a web interface with a candlestick chart.

## Features

- Fetches BTC-USD data from Yahoo Finance.
- Calculates various technical indicators such as RSI, MACD, SMA, EMA, and CCI.
- Uses a pre-trained XGBoost model to predict the probability of price movement.
- Displays the prediction results (Bullish or Bearish for the next day candle) and a candlestick chart on a web page.

## Requirements

- Python 3.7+
- Flask
- Pandas
- NumPy
- Joblib
- yfinance
- ta (Technical Analysis Library)
- Highcharts (for chart visualization)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/garlicspoofiyy/btcusd-price-prediction.git
   cd btc-prediction
   ```

2. **Install the required packages:**

   You can install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the pre-trained model:**

   Ensure that the `xgb_model.pkl` file is located in the `Midterm/btc-prediction/` directory.

4. **Run the application:**

   Start the Flask application by running:

   ```bash
   python Midterm/btc-prediction/app.py
   ```

   The application will be accessible at `http://0.0.0.0:9696`.

## Usage

- Open a web browser and navigate to `http://localhost:9696`.
- The page will display the BTCUSD daily price prediction, including the next daily close time in UTC, the current and previous day signal, and a candlestick chart of BTCUSD prices.

## File Structure

- `app.py`: The main Flask application file that handles data fetching, processing, and rendering.
- `templates/index.html`: The HTML template for the web interface.
- `xgb_model.pkl`: The pre-trained XGBoost model used for predictions.
