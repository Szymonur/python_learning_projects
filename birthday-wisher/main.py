import datetime as dt
import os
import random
import smtplib
import pandas

my_email = "steam88828@gmail.com"
password = "" #enter password here


def get_random_letter(name):
    file_name = random.choice(os.listdir("letter_templates"))
    with open(f"letter_templates/{file_name}") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
        return letter


def send_birthday_wish(name, email):
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy birthday!\n\n{get_random_letter(name)}"
        )


now = dt.datetime.now()

birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row.month == now.month and row.day == now.day:
        send_birthday_wish(row["name"], row["email"])
