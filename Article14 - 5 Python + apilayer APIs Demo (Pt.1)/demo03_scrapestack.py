import requests

params = {
  'access_key': 'YOUR_ACCESS_KEY',
  'url': 'https://pythongui.org'
}

api_result = requests.get('http://api.scrapestack.com/scrape', params)
website_content = api_result.content

print(website_content)