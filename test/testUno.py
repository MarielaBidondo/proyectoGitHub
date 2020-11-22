#importar libreria Beautiful soup para trabajar con html
from bs4 import BeautifulSoup
#paquete request
import requests
import re
#importamos libreria time
import time
import io
import pytesseract


#variable url donde esta el producto a evaluar

#URL = 'https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5SVNZB/' \
#      'ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G4CC972YL84I&dchild' \
#      '=1&keywords=iphone+12&qid=1604707287&quartzVehicle=93-1814&' \
#      'replacementKeywords=iphone&sprefix=iphon%2Caps%2C215&sr=8-1-spons&psc=1&spLa=' \
#      'ZW5jcnlwdGVkUXVhbGlmaWVyPUExMDlBT08wTElTNE5LJmVuY3J5cHRlZElkPUEwOTcxMzYySDRYOFlQM' \
#      'TBXRlYwJmVuY3J5cHRlZEFkSWQ9QTA0NjgyNDkxNVBJTjhJT1VOWTkxJndpZGdldE5hbWU9c3BfYXRmJmF' \
#      'jdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

#URL=' https://www.amazon.fr/dp/B084DWG2VQ/ref=s9_acss_bw_pg_WFpfn19f_1_t?pf_rd_m=A1X6FK5RDHNB96&pf_rd_s=merchandised-search-1&pf_rd_r=YMX058ER8MC634ND0P2Z&pf_rd_t=101&pf_rd_p=8a42b39e-007c-4951-a9e4-b74c249d44d7&pf_rd_i=15601482031'
URL = 'https://www.ebay.es/itm/Apple-iPhone-12-5G-64GB-NUOVO-Originale-Smartphone-iOS-14-Black/133571359505?hash=item1f19793311:g:6AEAAOSwsgtfmasC'

#Error     titulo = soup.find(id = 'productTitle' ).get_text()
#AttributeError: 'NoneType' object has no attribute 'get_text'
#Esto significa que no esta devolviendo las etiquetas que buscamos, puede ser por estructura de la pagina o que Amazon ha bloqueado request
#Informacion de error y posibles soluciones, las he probado todas sin resultado :(
#https://stackoverflow.com/questions/60139616/attributeerror-nonetype-object-has-no-attribute-get-text-python-web-scrapin
#https://blog.datahut.co/challenges-that-make-amazon-data-scraping-so-painful/
#Para probar el programa he usado otra pagina de ejemplo

#Tipo de explorador en el que vamos a abrir la url mencionada
#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#          '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
#my user agent es un poco diferente:
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


#Función que comprueba el precio de un producto
def comprobar_precio():
      #Requerimos la pagina con url y header previamanete definido
      page = requests.get(URL, headers = headers)
      #Con el paquete de Beautiful soup usamos el metodo content donde podemos acceder a el contenido de nuestra pagina
      # contenido pareseado a  html lo guardaos en la variable soup
      soup = BeautifulSoup(page.content, 'html.parser')
      #Usamos metodo find pasandole como parametro el identificador o etiqueta donde esta el titulo, precio de producto buscado
      #Amazon example
      #titulo = soup.find(id='productTitle').get_text().strip()
      #precio = soup.find(id='priceblock_ourprice').get_text().strip()
      #eBay example
      #Metodo get_Text() nos quita las etiquetas html y con metodo strip() removemos espacios en blanco
      titulo = soup.find(id = 'itemTitle' ).get_text().strip()
      precio = soup.find(id ='prcIsum').get_text().strip()
      #Cadena de texto lo pasamos a float con slice, Removemos simbolo de euros y decimales
      #Amazon
      #precio = float(precio[:-5])
      #Ebay
      precio = float(precio[:-7])

      #Comparamos nuestro precio con un valor limite
      if precio < 900:
          #Si el precio baja a 900 enviaremos un email avisando de esto
         # enviar_email()
       #  print(soup)
       # print(titulo)
          print(precio)
#
      enlaces = soup.find_all('a')

      lista = []
      lista_final = []

       print(titulo + "  " + "\n", precio)
       for link in soup.find_all('a'):
          lista.append(str(link.get('href')))

       for elemento in lista:
            if re.findall('^/dp', elemento):
                  lista_final.append('https://amazon.es/'+ elemento)

     print(lista_final)

#Bucle While que hara activo nuestro programa
while True:
      #Llamamos a nuestra funcion
      comprobar_precio()
      #Frecuencia con la que queremos que esta funcion despierte y se ejecute en segunds
      time.sleep(100000)

