import requests

r = requests.get("http://api.currencylayer.com/live?access_key=YOUR_ACCESS_KEY")

responses = r.json()

print(responses)