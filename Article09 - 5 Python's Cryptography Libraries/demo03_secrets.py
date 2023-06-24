import secrets
 
url = 'https://pythongui.org/reset=' + secrets.token_urlsafe()
print(url)