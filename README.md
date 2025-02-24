📡 HNG12 Telex Integration (Flask API with CORS Support)

🚀 Overview

A simple public integration built with Flask, handling CORS, and returning responses in JSON format. This API provides stock price updates and integration details.

📌 Features

✅ RESTful API with JSON responses✅ CORS-enabled for cross-origin requests✅ Scheduled stock price updates using APScheduler✅ Environment variable support via dotenv✅ Error handling for API requests

📂 Project Structure

/HNG12_TELEX_INTEGRATION
├── main.py # Main Flask application
├── telex_settings.py # Telex integration settings
├── fetch_stock_price.py # Function to fetch stock prices
├── requirements.txt # Dependencies list
└── README.md # Project documentation

🛠 Technologies Used

Backend: Flask (Python), Flask-CORS

Deployment: Gunicorn, Render

Scheduler: APScheduler (for periodic stock updates)

🚀 API Endpoints

1️⃣ Get Stock Price

Endpoint: GET /check_stockDescription: Fetches the latest MTN stock price and returns it in JSON format.

2️⃣ Get Integration Details

Endpoint: GET /integrationDescription: Provides details about the API integration.

📤 Response Example

Stock Price Response

{
"status": "success",
"stock_price": 200.5
}

Integration Details Response

{
"email": "marcelinusilonuba21@gmail.com",
"current_time": "2025-01-30T12:34:56Z",
"github_repo": "https://github.com/Meskana/HNG12-task0.git"
}

🚀 Running the Project Locally

1️⃣ Clone the Repository

git clone https://github.com/Meskana/HNG12_TELEX_INTEGRATION.git
cd HNG12_TELEX_INTEGRATION

2️⃣ Create a Virtual Environment

python -m venv env
source env/bin/activate # On Windows, use: env\Scripts\activate

3️⃣ Install Required Packages

Ensure requirements.txt is in the project directory, then run:

pip install -r requirements.txt

4️⃣ Run the Application

python main.py

The API will be accessible at:

http://127.0.0.1:5000/integration

http://127.0.0.1:5000/check_stock

🌎 Deployment

For deployment, use Gunicorn or Render:

gunicorn -w 4 -b 0.0.0.0:5000 main:app

🔗 License

This project is open-source and available under the MIT License.
