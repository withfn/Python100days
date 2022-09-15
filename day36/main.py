import requests
from datetime import date, timedelta
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_percentage():
    return round(float(yesterday_stock) - float(before_yesterday_stock) / float(before_yesterday_stock) * 100)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_key = 'FKSP3LMVKSPCEBZP'
alphavantage_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': alphavantage_key
}
tesla = requests.get(url="https://www.alphavantage.co/query", params=alphavantage_parameters)
print(tesla.status_code)
tesla_data = tesla.json()

today = date.today()
yesterday_date = (today - timedelta(days=1))
before_yesterday = (today - timedelta(days=2))
yesterday_stock = tesla_data["Time Series (Daily)"][str(yesterday_date)]["4. close"]
before_yesterday_stock = tesla_data["Time Series (Daily)"][str(before_yesterday)]["4. close"]

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
newsapi = NewsApiClient(api_key="e4d15516139f4a0e91f1520391f7a26f")
all_articles = newsapi.get_everything(q='tesla',
                                    sources='bbc-news',
                                    language='en',
                                    country='us')

print(all_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

