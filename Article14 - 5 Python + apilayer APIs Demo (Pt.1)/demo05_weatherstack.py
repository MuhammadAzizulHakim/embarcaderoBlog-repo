# coding: utf-8
import requests

params = {
  'access_key': 'YOUR_ACCESS_KEY',
  'query': 'New York'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
#print(api_response)
