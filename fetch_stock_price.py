from flask import Flask,  request, jsonify
import requests

#api_key1 ="OAFZGP7EHNP5LQDQ"
api_key ="OBkPvEPxGEbqIhjnSMk9idsIln5HF98b"
TELEX_URL = "https://telex.im"
symble= "MTN"

def fetch_mtn_stock_price():
    url = f"https://financialmodelingprep.com/api/v3/quote/{symble}?apikey={api_key}"
    try:
     
     
     response = requests.get(url)
     data = response.json()
     if data:
        stock_price = data[0]["price"]
        return(stock_price)
     else:
        return("Error fetching stock price.")

    except Exception as e:
     return jsonify({"error": str(e)}), 500