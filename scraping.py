import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.google.com')

data = BeautifulSoup(site.text, 'html.parser')

print(data.title)
print(data.title.text)

