import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 37.9794500
MY_LONG = 23.7162200

MY_EMAIL = "steam88828@gmail.com"
EMAIL_PASSWORD = "" #ENTER PASSWORD HERE


def is_iis_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    global iss_latitude
    global iss_longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunset <= time_now.hour <= sunrise


def send_notification():
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:ISS is above you!\n\n"
                f"Look to the sky! ISS is in your range of view! Exact localisation: {iss_latitude}, {iss_longitude}"
        )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

time_now = datetime.now()

while True:
    if is_night() and is_iis_above_me():
        send_notification()
        print("Email send!")
    else:
        print("Email wasn't send :/")
    time.sleep(60)
