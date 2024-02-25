import requests
from datetime import date

today = date.today()
print("Today's date:", today)
url = 'https://lawiny.topr.pl/viewpdf'
response = requests.get(url)
with open(f"{today}-avalanche.pdf", 'wb') as f:
    f.write(response.content)