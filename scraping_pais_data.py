import requests
import pymysql

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
baseURL = 'https://datosmacro.expansion.com/paises/'

paises = ['argentina', 'chile','brasil', 'uruguay', 'paraguay', 'bolivia', 'peru', 'ecuador', 'colombia', 'venezuela', 'guyana', 'surinam']

# ['argentina', 'chile','brasil', 'uruguay', 'paraguay', 'bolivia', 'peru', 'ecuador', 'colombia', 'venezuela', 'guyana', 'surinam']

data = {}

for pais in paises:
    url = baseURL + pais
    r = requests.get(url, headers=headers, timeout=5).text
    soup = BeautifulSoup(r, 'lxml')
        
    cuadros = soup.find_all('div', class_='cuadro')
    info = soup.find('div', itemprop='articleBody')
        
    continente = info.p.text.split(',')[1][11:]
    poblacion = ''
    superficie = ''
    
    for li in cuadros[1].ul:        
        if li.span.text == 'Población':
            poblacion = int(''.join(li.text.split(": ")[1].split('.')))
            
        if li.span.text == 'Superficie':
            superficie = int(''.join(li.text.split(" ")[1].split('.')))
        
    
    print(f'{pais.capitalize()}:')
    print(f'{" ":5}{"Población: ":10}{poblacion:20}', f'{" ":5}{"Superficie: ":10}{superficie:20}', f'{" ":5}{"Continente: ":10}{continente:20}', sep=f'{" ":5}')

    data[pais] = {
        'nombre': pais.capitalize(),
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    
try:
    conexion = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='estadisticas_vacunas')
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO paises(nombre, poblacion, superficie, continente) VALUES (%s, %s, %s, %s);"
            
            for pais in data:
                cursor.execute(consulta, (data[pais]['nombre'], data[pais]['poblacion'], data[pais]['superficie'], data[pais]['continente']))
                
        conexion.commit()
    finally:
        conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

    