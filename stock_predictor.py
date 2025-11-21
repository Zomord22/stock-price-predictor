# stock_predictor.py
import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import gradio as gr

# Get stock data
def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1y")
    return data

def predict_stock(symbol, days=7):
    # Get data and prepare features
    data = get_stock_data(symbol)
    data['Prediction'] = data['Close'].shift(-days)
    
    # Simple ML model
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor()
    # ... training code ...
    
    return f"Predicted {symbol} will be ${predicted_price:.2f} in {days} days"

# Gradio interface
demo = gr.Interface(
    fn=predict_stock,
    inputs=[
        gr.Dropdown(["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN"], label="Stock"),
        gr.Slider(1, 30, value=7, label="Days to Predict")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Stock Price Predictor"
)
