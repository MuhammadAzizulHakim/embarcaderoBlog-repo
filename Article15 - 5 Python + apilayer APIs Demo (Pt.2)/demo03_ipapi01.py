import requests
 
r = requests.get("http://api.ipapi.com/36.80.244.42?access_key=YOUR_ACCESS_KEY")
 
responses = r.json()
 
print(responses)