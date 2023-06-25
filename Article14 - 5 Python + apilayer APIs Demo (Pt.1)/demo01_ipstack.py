import requests

r = requests.get("http://api.ipstack.com/134.201.250.155?access_key=YOUR_ACCESS_KEY")

responses = r.json()
print(responses)