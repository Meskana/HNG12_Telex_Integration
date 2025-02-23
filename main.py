from flask import Flask,  request, jsonify
import requests
from datetime import datetime, timedelta
from telex_settings import integration_bp
from apscheduler.schedulers.background import BackgroundScheduler
from fetch_stock_price import fetch_mtn_stock_price
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(integration_bp)

@app.route("/check_stock", methods=["GET"])
def send_mtn_price_to_telex():

    """Fetch MTN stock price and send it to Telex every 24 hours."""

    with app.app_context():
        stock_price = fetch_mtn_stock_price()
        print(stock_price)

        if stock_price is None:
            print("Error: Could not fetch stock price.")
            return

        message = f"📈 MTN Stock Update!\nCurrent Price: ${stock_price}"

        telex_format = {
            "message": message,
            "username": "MTN Stock Monitor",
            "event_name": "Daily Stock Update",
            "status": "success"
        }

        # Send to Telex
    

        headers = {"Content-Type": "application/json"}
        try:
    
            requests.post("https://ping.telex.im/v1/webhooks/01953286-a488-7aa7-9584-2566f38f4a66", json=telex_format,headers = headers)
            return jsonify({"status": "success", "stock_price": stock_price})
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")



   

# Schedule the job to run every 24 hours
scheduler = BackgroundScheduler()
scheduler.add_job(send_mtn_price_to_telex, "interval", minutes=1)
scheduler.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)