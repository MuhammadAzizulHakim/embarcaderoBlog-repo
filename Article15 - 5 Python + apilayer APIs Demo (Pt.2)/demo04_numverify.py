import requests
 
params = {
    'access_key': '8658b541cf1a5f34c1c77aca0bbca190',
    'number': '14158586273'
}
 
api_result = requests.get('http://apilayer.net/api/validate?', params)
 
api_response = api_result.json()

print(api_response)
