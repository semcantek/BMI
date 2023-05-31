import requests
from bs4 import BeautifulSoup
url ='http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec3'
res = requests.get(url)
html_page=res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
output = ''
blacklist=['[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script']
for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)