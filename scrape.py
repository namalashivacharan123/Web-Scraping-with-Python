import requests
from bs4 import BeautifulSoup

import re 


url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

rawText = ''

for p in soup.find_all('p', limit=5):
    rawText += p.text 

print('raw text = ', rawText)

cleanedText = ''

strt = 0
end = len(rawText)

for m in re.finditer(r'\[[0-9]+\]', rawText):
    end = m.start()
    cleanedText += rawText[strt:end]
    strt = m.end()
cleanedText += rawText[strt:]

print('cleaned text = ', cleanedText)