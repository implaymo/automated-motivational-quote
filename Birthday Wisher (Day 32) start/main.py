import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

my_email = os.getenv("my_email")
password = os.getenv("password")

now = dt.datetime.now()
day = now.weekday()


with open("quotes.txt") as file:
    list_of_quotes = [line.rstrip() for line in file]
    random_quote = random.choice(list_of_quotes)

if day == day:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Motivational quote of the day\n\n{random_quote}")

