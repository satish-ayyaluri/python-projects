from twilio.rest import Client
import requests
from dotenv import load_dotenv
import os
load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"




stock_parms={

    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":os.getenv("stock_api")

}



response=requests.get(os.getenv("STOCK_ENDPOINT"),params=stock_parms)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_price=yesterday_data["4. close"]


#daybefore_yesterday_price
day_before=data_list[1]
day_before_price=day_before["4. close"]


price_differ=abs(float(day_before_price)-float(yesterday_price))
percent=(price_differ/float(yesterday_price)*100)

if percent>1:
    news_parms={
        "apiKey":os.getenv("news_api"),
        "qInTitle":COMPANY_NAME,

    }
    news_response=requests.get(os.getenv("NEWS_ENDPOINT"),news_parms)
    articles=news_response.json()["articles"]

    three_articles=articles[:3]
    format_articles= [f" HeadLine {article['title']} \nBrie:f {article['description']}"for article in three_articles]
    client = Client(os.getenv("acc_id"),os.getenv("api"))
    for article in format_articles:
        message=client.messages.create(
            body=article,
            from_=os.getenv("from_"),  # Your Twilio number
            to=os.getenv("to")
        )



