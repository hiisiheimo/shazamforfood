import requests
from bs4 import BeautifulSoup

page = requests.get('https://yhteishyva.fi/reseptit/oopperakellarin-silakat/4ViyaOijC5SAxUbW5bNvAE')
soup = BeautifulSoup(page.content, 'html.parser')
recipe = soup.find_all('div', class_='recipe__ingredients')

print(recipe)
