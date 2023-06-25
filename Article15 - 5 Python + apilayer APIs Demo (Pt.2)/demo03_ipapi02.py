import requests

r = requests.get("http://api.ipapi.com/36.80.244.42?access_key=YOUR_ACCESS_KEY")

responses = r.json()

print(responses['ip'])
print(responses['type'])
print(responses['continent_code'])
print(responses['continent_name'])
print(responses['country_code'])
print(responses['country_name'])
print(responses['region_code'])
print(responses['region_name'])
print(responses['city'])
print(responses['zip'])
print(responses['latitude'])
print(responses['longitude'])
print(responses['location'])