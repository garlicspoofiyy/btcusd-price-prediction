# BTCUSD Daily Price Prediction

This project is a web application that predicts the daily price movement of Bitcoin (BTC) against the US Dollar (USD) using XGBoostClassifier and technical indicators. The application is built using Flask and displays predictions on a web interface with a candlestick chart.

## Project Structure

- `btc-prediction/`: Main project directory
  - `app.py`: Flask web application
  - `templates/`: HTML templates for the web application
    - `index.html`: Main page template displaying the BTCUSD chart and predictions
  - `xgb_model.pkl`: Pre-trained XGBoost model
- `midterm.ipynb`: Jupyter Notebook containing the data analysis and model training code
- `Pipfile`: Pipenv file specifying project dependencies
- `Pipfile.lock`: Pipenv lock file with pinned dependency versions
- `Dockerfile`: Dockerfile for containerizing the application

### Data Source

The data used for training the model and making predictions is sourced from the Kaggle dataset [Bitcoin Price Trends with Indicators (8 Years)](https://www.kaggle.com/datasets/aspillai/bitcoin-price-trends-with-indicators-8-years).

## Features

- Fetches BTC-USD data from Yahoo Finance.
- Calculates various technical indicators such as RSI, MACD, SMA, EMA, and CCI.
- Uses a pre-trained XGBoost model to predict the probability of price movement.
- Displays the prediction results (Bullish or Bearish for the next day candle) and a candlestick chart on a web page.

## Setup

1. Install Pipenv:

   ```
   pip install pipenv
   ```

2. Install project dependencies:

   ```
   pipenv install
   ```

3. Activate the virtual environment:

   ```
   pipenv shell
   ```

4. Run the Flask application:

   ```
   python btc-prediction/app.py
   ```

5. Access the web application at `http://localhost:9696`.

## Docker

To run the application using Docker:

1. Build the Docker image:

   ```
   docker build -t btc-prediction .
   ```

2. Run the Docker container:

   ```
   docker run -p 9696:9696 btc-prediction
   ```

3. Access the web application at `http://localhost:9696`.

## Usage

- The web application displays a candlestick chart of BTCUSD historical data.
- The "Next Daily Close in UTC" shows the time remaining until the next daily candle close.
- The prediction of the model relies on the data of the current candle.
- The final prediction is based after the current candle closes.
- The "Current Day Signal" indicates the predicted price movement for the current day (Bullish or Bearish).
- The "Previous Day Signal" shows the predicted price movement for the previous day.

## Model Training

The Jupyter Notebook `btc-prediction-notebook.ipynb` contains the code for data analysis, feature engineering, and model training. It demonstrates the process of fetching historical data, calculating technical indicators, splitting the data into training and testing sets, and training an XGBoost classifier model.

The trained model is saved as `btc-prediction/xgb_model.pkl` and is used by the Flask application for making predictions.
