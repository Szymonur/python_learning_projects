import random
import smtplib

my_email = "steam88828@gmail.com"
password = "" #enter password here
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="steam88828mail@wp.pl",
#         msg="Subject:Hello Szymon!\n\nThis is the body of email"
#     )

import datetime as dt

#
# now = dt.datetime.now()
# year = now.year
# month = now.month
#
# date_of_birth = dt.datetime(year=2003, month=6, day=16, hour=5)

with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()
    random_quote = random.choice(quotes_list).strip()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivation quote for today.\n\n{random_quote}"
        )
