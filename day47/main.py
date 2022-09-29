from bs4 import BeautifulSoup
import requests

url= ""
response = requests.get(url=url).text

soup = BeautifulSoup(response, "html.parser")

print(soup)
# price = soup.find(name="div", class_="priceView-hero-price priceView-customer-price")
# print(price)

