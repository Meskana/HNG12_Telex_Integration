from flask import Flask,  request, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()
#api_key1 ="OAFZGP7EHNP5LQDQ"
api_key = os.getenv("MY_SECRET_KEY")
TELEX_URL = "https://telex.im"
symble= "MTN"

def fetch_mtn_stock_price():
    url = f"https://financialmodelingprep.com/api/v3/quote/{symble}?apikey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()

        if data:
            stock_price = data[0].get("price")
            return {"status": "success", "stock_price": stock_price}
        else:
            return {"status": "error", "message": "No stock data found"}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}