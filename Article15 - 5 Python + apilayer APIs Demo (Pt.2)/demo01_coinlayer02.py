import requests
 
r = requests.get("http://api.coinlayer.com/api/live?access_key=YOUR_ACCESS_KEY")
 
responses = r.json()
 
print(responses['rates']['BTC'])