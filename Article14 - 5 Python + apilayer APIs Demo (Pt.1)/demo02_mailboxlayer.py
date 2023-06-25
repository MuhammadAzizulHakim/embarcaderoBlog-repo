import requests
 
params = {
    'access_key': 'YOUR_ACCESS_KEY',
    'email': 'support@apilayer.com'
}
 
api_result = requests.get('http://apilayer.net/api/check?', params)
 
api_response = api_result.json()
print(api_response)