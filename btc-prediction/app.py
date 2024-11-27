import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import joblib
import yfinance as yf
import ta

app = Flask(__name__)

# load the model
model = joblib.load('Midterm/btc-prediction/xgb_model.pkl')

# selected indicators
selected_features = ['rsi_7_oversold', 'macd_below', 'sma_100', 'rsi_14', 'ema_100', 'cci_14_high', 'rsi_7_overbought', 'macd_above', 'cci_14_low', 'rsi_14_oversold']

@app.route('/')
def index():
    # fetching btcusd data from yahoo finance
    btc = yf.download('BTC-USD', period='max', interval='1d')

    btc.columns = btc.columns.droplevel(1)
    btc = btc[['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']]
    btc.columns.name = None
    btc.columns = btc.columns.str.lower()
    btc.rename_axis('date', inplace=True)
    btc.index = btc.index.date
    btc.index.name = 'date' 
    
    # calculate technical indicators
    btc['rsi_7'] = ta.momentum.RSIIndicator(btc['close'], window=7).rsi()
    btc['rsi_14'] = ta.momentum.RSIIndicator(btc['close'], window=14).rsi()
    btc['rsi_14_overbought'] = (btc['rsi_14'] >= 70).astype(int)
    btc['rsi_14_oversold'] = (btc['rsi_14'] <= 30).astype(int)
    btc['rsi_7_overbought'] = (btc['rsi_7'] >= 70).astype(int)
    btc['rsi_7_oversold'] = (btc['rsi_7'] <= 30).astype(int)
    
    macd = ta.trend.MACD(btc['close'], window_slow=26, window_fast=12, window_sign=9)
    btc['macd'] = macd.macd()
    btc['macd_signal'] = macd.macd_signal()
    btc['macd_diff'] = macd.macd_diff()
    btc['macd_above'] = (btc['macd_diff'] > 0).astype(int)
    btc['macd_below'] = (btc['macd_diff'] < 0).astype(int)
    
    btc['sma_100'] = ta.trend.SMAIndicator(btc['close'], window=100).sma_indicator()
    btc['ema_100'] = ta.trend.EMAIndicator(btc['close'], window=100).ema_indicator()
    
    btc['cci_14'] = ta.trend.CCIIndicator(btc['high'], btc['low'], btc['close'], window=14).cci()
    btc['cci_14_high'] = (btc['cci_14'] >= 100).astype(int)
    btc['cci_14_low'] = (btc['cci_14'] <= -100).astype(int)
    
    # calculate hours left before the next day in UTC
    now_utc = pd.Timestamp.now(tz='UTC')
    next_day = (now_utc + pd.Timedelta(days=1)).normalize()
    hours_left = (next_day - now_utc).total_seconds() / 3600  
    next_ytd_close = f"{hours_left:.2f} hours"
    
    # get the latest candle data
    latest_data = btc.iloc[-1][selected_features].to_dict()

    # calculate the signal based on the latest data
    input_data = pd.DataFrame([latest_data])
    prediction = model.predict_proba(input_data)
    probability = prediction[0][1]

    # get the candle data before the latest candle data
    prevday_data = btc.iloc[-2][selected_features].to_dict()
    previnput_data = pd.DataFrame([prevday_data])
    prevprediction = model.predict_proba(previnput_data)
    prevprobability = prevprediction[0][1]

    # calculate the signal based on the probability
    signal = 0
    if ((probability > 0.014) & (probability <= 0.0398)) | \
       ((probability > 0.0762) & (probability <= 0.168)) | \
       (probability > 0.512) & (probability <= 0.884):
        signal = 1
    
    return render_template('index.html', chart_data=btc.to_json(orient='index'), latest_data=latest_data, prevday_data=prevday_data, signal=signal, probability=probability, prevprobability=prevprobability, next_ytd_close=next_ytd_close)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)
