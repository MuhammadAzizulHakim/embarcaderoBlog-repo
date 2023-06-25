import requests

r = requests.get("http://api.currencylayer.com/live?access_key=YOUR_ACCESS_KEY")

responses = r.json()

# USD to Bitcoin
print(responses['quotes']['USDBTC'])
# USD to British Pound Sterling
print(responses['quotes']['USDGBP'])
# USD to Australian Dollar
print(responses['quotes']['USDAUD'])
# USD to Chinese Yuan
print(responses['quotes']['USDCNY'])
# USD to Japanese Yen
print(responses['quotes']['USDJPY'])