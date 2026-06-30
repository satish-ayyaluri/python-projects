📊 Stock Market Alert System (Python)
📌 Overview

This project is a Python-based automation system that tracks stock price movements and sends real-time SMS alerts when a stock changes significantly. It uses financial APIs, news APIs, and Twilio SMS service to deliver timely updates.

The system is designed for portfolio tracking and learning purposes in Python automation and API integration.

🚀 Features
📈 Fetches real-time stock price data
📉 Calculates percentage change in stock price
📰 Fetches latest news related to the stock/company
📲 Sends SMS alerts using Twilio
🔐 Secure API key management using .env file
⚠️ Error handling for invalid stock symbols and API failures
🛠️ Tech Stack
Python 3
Requests (HTTP API calls)
Twilio API (SMS service)
Alpha Vantage API (Stock data)
NewsAPI (Latest news)
python-dotenv (Environment variables)
📁 Project Structure
Stock-Alert-System/
│
├── main.py
├── .env (not uploaded)
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

Create a .env file in the project root:

STOCK_ENDPOINT=https://www.alphavantage.co/query
NEWS_ENDPOINT=https://newsapi.org/v2/everything

stock_api=your_alpha_vantage_api_key
news_api=your_news_api_key

acc_id=your_twilio_account_sid
api=your_twilio_auth_token

from_="+your_twilio_number"
to="+your_phone_number"
4. Run the project
python main.py
📊 How It Works
The program fetches stock price data from Alpha Vantage API
It compares yesterday’s and previous day’s closing prices
If the price change exceeds a threshold (e.g., 5%), it triggers an alert
Latest news about the stock is fetched from NewsAPI
An SMS containing stock movement + news headline is sent via Twilio
⚠️ Error Handling
Handles invalid stock symbols
Handles API failures and rate limits
Prevents crashes when data is missing
📌 Example Output SMS
TSLA 📉 -5.23%

Headline: Tesla stock drops amid market pressure
Brief: Tesla shares fell after market-wide selloff...
🔒 Security Note
API keys are stored in .env file
.env is excluded using .gitignore
.env.example provided for reference
🎯 Future Improvements
Add user portfolio input system
Add email + Telegram alerts
Build a web dashboard using Streamlit
Store alerts in database
Add real-time market streaming support
👨‍💻 Author

Ayyaluri Satish Kumar Reddy
Cybersecurity & Python Developer
GitHub: [your-username]
