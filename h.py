import requests
import pymysql

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
baseURL = 'https://datosmacro.expansion.com/paises/'

# ['argentina', 'chile','brasil', 'uruguay', 'paraguay', 'bolivia', 'peru', 'ecuador', 'colombia', 'venezuela', 'guyana', 'surinam']

paises_orig = []
paises_url = []

url = baseURL
r = requests.get(url, headers=headers, timeout=5).text
soup = BeautifulSoup(r, 'lxml')

paises_loc = soup.find('div', class_='flags')

for div in paises_loc:
    p = div.h4.a.text
    print(p)
    paises_orig.append(p)
    p = div.find('a')
    print(p.attrs['href'])
    
    # p = p.lower()
    # x = "áéíóú "
    # y = "aeiou-"
    # mytable = p.maketrans(x, y)
    # print(p.translate(mytable))
    # paises.append(p.translate(mytable))


# for pais in paises:
#     url2 = baseURL + pais
#     print(url2)
#     re = requests.get(url2, headers=headers, timeout=5).text
#     soup2 = BeautifulSoup(re, 'lxml')

#     print(soup2.h1.find_all('a')[1].text.split(':')[0])
# Verificar por h1