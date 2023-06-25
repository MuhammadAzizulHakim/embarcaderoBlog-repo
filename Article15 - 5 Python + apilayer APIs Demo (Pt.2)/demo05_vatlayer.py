import requests
 
params = {
    'access_key': 'YOUR_ACCESS_KEY',
    'vat_number': 'LU26375245'
}
 
api_result = requests.get('http://apilayer.net/api/validate?', params)
 
api_response = api_result.json()

print(api_response)
