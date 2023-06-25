import requests

params = {
  'access_key': 'YOUR_ACCESS_KEY',
  'query': 'pythongui'
}

api_result = requests.get('http://api.serpstack.com/search', params)

api_response = api_result.json()

print("Total results: ", api_response['search_information']['total_results'])

for number, result in enumerate(api_response['organic_results'], start=1):
    print("%s. %s" % (number, result['title']))
    #print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
