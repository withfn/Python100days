import smtplib
import pandas as pd
import datetime as dt
from random import randint

#login
my_email = "withfnas@gmail.com"
password = "password"

#date
dt = dt.datetime.today()
day = dt.day
month = dt.month

#open csv birthdays
df = pd.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

#send email if has a birthday today
for person in birthdays:
    if person['day'] == day and person['month'] == month:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt", 'r') as letter:
            sample_letter = letter.read()
            new_letter = sample_letter.replace('[NAME]', person['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person['email'], 
                                msg=f"Subject:Happy birthday!\n\n{letter}")
