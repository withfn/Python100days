from bs4 import BeautifulSoup
import requests

clientId = ""
clientSecret = ""

year = input("Which year do you want to travel to? type date in this format YYYY-MM-DD: ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/2001-08-12/{year}").text

print(response)
