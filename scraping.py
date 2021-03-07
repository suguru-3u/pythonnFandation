import requests
from bs4 import BeautifulSoup

site = requests.get(‘https://www.google.com’)
print(site.text)