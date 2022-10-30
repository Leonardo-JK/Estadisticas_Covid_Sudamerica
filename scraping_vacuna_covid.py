import requests

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
baseURL = 'https://datosmacro.expansion.com/otros/coronavirus-vacuna/'

paises = ['argentina', 'chile','brasil', 'uruguay', 'paraguay', 'bolivia', 'peru', 'ecuador', 'colombia', 'venezuela', 'guyana', 'surinam']

data = {}

for pais in paises:
    url = baseURL + pais
    r = requests.get(url, headers=headers, timeout=5).text
    s = BeautifulSoup(r, 'lxml')
        
    table_data = s.find('table', id='tb0')
    tbody = table_data.find_all('tr')

    row_data = []

    for tr in tbody:
        tr_array = []
        for td in tr:
            tr_array.append(td.text)
            
        row_data.append(tr_array)
        
    data[pais] = row_data
    
    print(f'datos de {pais.capitalize()} obtenidos.')

    
# for line in data['surinam']:
#     for value in line:
#         print(f'{value:25}', end=' ')
#     print()