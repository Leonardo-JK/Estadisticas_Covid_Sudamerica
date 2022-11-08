import scraping_functions as scr
import mysql_functions as mysql
import pandas as pd
import time
import threading as th

bar = True
keep_bar = True

country_list = []
contry_data = []

print('Comenzando la recopilacion de datos:', end='\n\n')
print('Obteniendo lista de paises')

def barra():
    global bar
    count = 0
    while bar:
        print('.'*count, end='\r')
        time.sleep(0.5)
        count = count + 1
        bar = keep_bar
    print()  

def get_country_list():    
    def data():
        global country_list
        global keep_bar
        
        country_list_urls = scr.get_countries('urls')
        country_list_names = scr.get_countries('names')
        
        for i in range(len(country_list_urls)):
            country_list.append({
                'name': country_list_names[i],
                'url': country_list_urls[i]
            })
        
        keep_bar = False
        print('Lista de paises obtenida ✓')
        print(pd.DataFrame(country_list))
        
    get_country_thread = th.Thread(target=data)
    get_country_thread.start()
    
    barra()
    

def get_contry_data():
    def data():
        global country_list
        global contry_data
        global keep_bar
        
        for i in range(len(country_list)):
            d = scr.get_countries_data(country_list[i]['url'])
            d['name'] = country_list[i]['name']
            
            contry_data.append(d)
            
        keep_bar = False   
        print('Datos de paises obtenidos ✓')
        print(pd.DataFrame(contry_data))
        
    get_country_thread = th.Thread(target=data)
    get_country_thread.start()
    
    barra()

get_country_list()

print('Obteniendo datos de paises.')

get_contry_data()

