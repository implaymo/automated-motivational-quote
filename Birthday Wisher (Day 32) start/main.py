import smtplib
import datetime as dt
import random

my_email = "pythonuser112@gmail.com"
password = "vuvemheklbeqqahu"

now = dt.datetime.now()
day = now.weekday()

with open("quotes.txt") as file:
    list_of_quotes = [line.rstrip() for line in file]
    random_quote = random.choice(list_of_quotes)

if day == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonuser112@gmail.com",
                            msg=f"Subject:Motivational quote of the day\n\n{random_quote}")

