import urllib.request

with urllib.request.urlopen('http://embarcadero.com/') as f:
    print(f.read(300))