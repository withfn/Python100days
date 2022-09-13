import smtplib
from random import choice
import datetime as dt

with open("quotes.txt", 'r') as file:
    quotes = file.readlines()
    quotes = [quote.replace("\n", "") for quote in quotes]

my_email = "withfnas@gmail.com"
password = "vbddeofxkejhbgnb"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        message= choice(quotes)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="thiagowfn@yahoo.com", 
                            msg=f"Subject:Motivacional Quote\n\n{message}")

