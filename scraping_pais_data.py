import requests

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
baseURL = 'https://datosmacro.expansion.com/paises/'

paises = ['argentina', 'chile','brasil', 'uruguay', 'paraguay', 'bolivia', 'peru', 'ecuador', 'colombia', 'venezuela', 'guyana', 'surinam']

data = {}

for pais in paises:
    url = baseURL + pais
    r = requests.get(url, headers=headers, timeout=5).text
    soup = BeautifulSoup(r, 'lxml')
        
    cuadros = soup.find_all('div', class_='cuadro')
    
    poblacion = ''
    superficie = ''
    
    for li in cuadros[1].ul:        
        if li.span.text == 'Población':
            poblacion = li.text.split(": ")[1]
            
        if li.span.text == 'Superficie':
            superficie = li.text.split(": ")[1]
        
    
    print(f'{pais.capitalize()}:')
    print(f'{" ":5}{"Población: ":15}{poblacion:20r}', f'{" ":5}{"Superficie: ":15}{superficie:20r}', sep=f'{" ":5}')


    