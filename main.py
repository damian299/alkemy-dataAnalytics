
import requests
import os
import shutil

from datetime import date

fechaActual = date.today().strftime('%B - %Y')
nombre_fecha= date.today().strftime('%d-%m-%Y')

# obtencion de archivos

url_museos = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos.csv"
url_cines  = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
url_bibliotecas = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
    
archivo_museos = requests.get(url_museos)
archivo_cines = requests.get(url_cines)
arhivo_bibliotecas = requests.get(url_bibliotecas)

#descarga y guardado con fecha actual

if not os.path.exists('C:/Users/Public/Documents/datasets/museos' and 'C:/Users/Public/Documents/datasets/cines' and 'C:/Users/Public/Documents/datasets/bibliotecas' ):
    
    os.makedirs('C:/Users/Public/Documents/datasets/museos/'+ fechaActual)
    os.makedirs('C:/Users/Public/Documents/datasets/cines/'+ fechaActual)
    os.makedirs('C:/Users/Public/Documents/datasets/bibliotecas/'+ fechaActual)
    
    
    

    open('C:/Users/Public/Documents/datasets/museos/'+fechaActual+'/'+'museos-'+nombre_fecha+'.csv', 'wb').write(archivo_museos.content)
    open('C:/Users/Public/Documents/datasets/cines/'+fechaActual+'/'+'cines-'+nombre_fecha+'.csv', 'wb').write(archivo_cines.content)
    open('C:/Users/Public/Documents/datasets/bibliotecas/'+fechaActual+'/'+'bibliotecas-'+nombre_fecha+'.csv', 'wb').write(arhivo_bibliotecas.content)

if os.path.exists('C:/Users/Public/Documents/datasets/museos' and 'C:/Users/Public/Documents/datasets/cines' and 'C:/Users/Public/Documents/datasets/bibliotecas' ):
    
    directorio = 'C:/Users/Public/Documents/datasets'

    shutil.rmtree(directorio)
    

   
    os.makedirs('C:/Users/Public/Documents/datasets/museos/'+ fechaActual)
   
    os.makedirs('C:/Users/Public/Documents/datasets/cines/'+ fechaActual)
    os.makedirs('C:/Users/Public/Documents/datasets/bibliotecas/'+ fechaActual)
   
    open('C:/Users/Public/Documents/datasets/museos/'+fechaActual+'/'+'museos-'+nombre_fecha+'.csv', 'wb').write(archivo_museos.content)
    open('C:/Users/Public/Documents/datasets/cines/'+fechaActual+'/'+'cines-'+nombre_fecha+'.csv', 'wb').write(archivo_cines.content)
    open('C:/Users/Public/Documents/datasets/bibliotecas/'+fechaActual+'/'+'bibliotecas-'+nombre_fecha+'.csv', 'wb').write(arhivo_bibliotecas.content)
    
    