📊 Stock Market Alert System (Python)
📌 Overview

This is a Python automation project that tracks stock price movements and sends SMS alerts when a stock changes significantly. It also fetches related news headlines and sends them via Twilio SMS.

The project demonstrates API integration, automation, error handling, and secure environment variable management.

🚀 Features
📈 Fetch real-time stock price data
📉 Detect percentage change in stock price
📰 Fetch latest news articles for the stock
📲 Send SMS alerts using Twilio
🔐 Secure API handling using .env file
⚠️ Error handling for invalid stock symbols and API failures
🛠️ Tech Stack
Python 3
Requests
Twilio API (SMS service)
Alpha Vantage API (Stock data)
NewsAPI (News data)
python-dotenv
📁 Project Structure
Stock-Alert-System/
│
├── main.py
├── .env (NOT uploaded)
├── .env.example
├── .gitignore
└── README.md
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/stock-alert-system.git
cd stock-alert-system
2. Install dependencies
pip install requests twilio python-dotenv
3. Create .env file

Create a .env file in the project root and add the following:

STOCK_ENDPOINT=https://www.alphavantage.co/query
NEWS_ENDPOINT=https://newsapi.org/v2/everything

stock_api=your_alpha_vantage_api_key
news_api=your_news_api_key

acc_id=your_twilio_account_sid
api=your_twilio_auth_token

from_="+your_twilio_number"
to="+your_verified_phone_number"
🔑 Get Your API Keys From Here
📊 Alpha Vantage API:
https://www.alphavantage.co/support/#api-key
📰 NewsAPI:
https://newsapi.org/register
📲 Twilio Console:
https://www.twilio.com/console
📄 .env.example

This file shows required variables (no secrets included):

STOCK_ENDPOINT=
NEWS_ENDPOINT=
stock_api=
news_api=
acc_id=
api=
from_=
to=
▶️ Run the Project
python main.py
📊 How It Works
Fetch stock data from Alpha Vantage API
Compare yesterday and previous close price
If price change exceeds threshold (e.g. 5%), trigger alert
Fetch related news using NewsAPI
Send SMS alert via Twilio
⚠️ Error Handling
Handles invalid stock symbols
Handles API errors and rate limits
Prevents program crashes when data is missing
🔒 Security Best Practices
API keys stored in .env file
.env is ignored using .gitignore
.env.example provided for reference
No sensitive data is uploaded to GitHub
🎯 Future Improvements
📊 Add portfolio-based stock tracking
📱 Add Telegram/email notifications
📈 Add Streamlit dashboard UI
💾 Store alerts in database
⏱️ Schedule automatic daily runs
👨‍💻 Author

Ayyaluri Satish Kumar Reddy
Cybersecurity & Python Enthusiast
GitHub: https://github.com/your-username
