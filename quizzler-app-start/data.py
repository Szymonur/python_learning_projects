import requests

params = {
    "amount": 10,
    "type": "boolean"
}
result = requests.get("https://opentdb.com/api.php", params=params)
question_data = result.json()["results"]
