from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta
from telex_settings import integration_bp
from apscheduler.schedulers.background import BackgroundScheduler
from fetch_stock_price import fetch_mtn_stock_price
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Adjust origins as needed
app.register_blueprint(integration_bp)

@app.route("/check_stock", methods=["GET","POST"])
def send_stock_price():
    """Fetch MTN stock price and send it to Telex periodically."""
    with app.app_context():
        stock_price = fetch_mtn_stock_price()
        print(stock_price)
        if stock_price is None:
            print("Error: Could not fetch stock price.")
        
        if isinstance(stock_price, requests.Response):  
            stock_price = stock_price.json()

        message = f"📈 MTN Stock Update!\nCurrent Price: ${stock_price}"
        telex_format = {
            "message": message,
            "username": "MTN Stock Monitor",
            "event_name": "Daily Stock Update",
            "status": "success"
        }

        headers = {"Content-Type": "application/json"}
        webhook_url = os.getenv("MY_WEBHOOK")

        if not webhook_url:
            print("Error: MY_WEBHOOK is not set in environment variables.")
            return

        try:
            response = requests.post(webhook_url, json=telex_format, headers=headers)
            response.raise_for_status()  # Raises an error for non-200 status codes

            print(response)
            return jsonify({"status": "success", "stock_price": stock_price}), 200
        except requests.exceptions.RequestException as e:
            print(f"Error sending to Telex: {e}")
            return jsonify({"status": "error", "message": "Failed to send to Telex"}), 500


# Schedule the job to run every 24 hours
scheduler = BackgroundScheduler()
scheduler.add_job(send_stock_price, "interval", hours=24)
scheduler.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
