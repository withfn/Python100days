import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


#####

alphavantage_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_KEY
}
tesla = requests.get(url="https://www.alphavantage.co/query", params=alphavantage_parameters)
tesla_data = tesla.json()

today = date.today()
yesterday_date = (today - timedelta(days=1))
before_yesterday = (today - timedelta(days=2))
yesterday_stock = tesla_data["Time Series (Daily)"][str(yesterday_date)]["4. close"]
before_yesterday_stock = tesla_data["Time Series (Daily)"][str(before_yesterday)]["4. close"]

difference = float(yesterday_stock) - float(before_yesterday_stock)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_stock)) * 100, 2)
print(difference)
print(diff_percent)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if  abs(diff_percent) > 1: 
    news_params = {
        "apiKey": NEWSAPI_KEY,
        "qInTitle": COMPANY_NAME,
        
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%  Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to="+5511949788910"
        )
    print("salvee")
