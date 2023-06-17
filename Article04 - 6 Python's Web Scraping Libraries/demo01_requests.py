import requests
 
r = requests.get('https://example.com')
 
print(r.text)
print(r.headers)
print(r.status_code)