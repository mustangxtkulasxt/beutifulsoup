from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.example.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
