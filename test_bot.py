import requests
from bs4 import BeautifulSoup as b

URL = 'https://web.telegram.org/k/#@Average_cypher_main'
r = requests.get(URL)
print(r.status_code)
print(r.text)
soup = b(r.text, 'html.parser')
nicknames = soup.find_all('div',class="c-ripple")

