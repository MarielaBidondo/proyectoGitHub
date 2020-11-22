# importar libreria Beautiful soup para trabajar con html
import re
# importamos libreria time
import time

# paquete request
import requests
from bs4 import BeautifulSoup

# variable url donde esta el producto a evaluar

#URL = 'https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5SVNZB/' \
#      'ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G4CC972YL84I&dchild' \
#      '=1&keywords=iphone+12&qid=1604707287&quartzVehicle=93-1814&' \
#      'replacementKeywords=iphone&sprefix=iphon%2Caps%2C215&sr=8-1-spons&psc=1&spLa=' \
#      'ZW5jcnlwdGVkUXVhbGlmaWVyPUExMDlBT08wTElTNE5LJmVuY3J5cHRlZElkPUEwOTcxMzYySDRYOFlQM' \
#      'TBXRlYwJmVuY3J5cHRlZEFkSWQ9QTA0NjgyNDkxNVBJTjhJT1VOWTkxJndpZGdldE5hbWU9c3BfYXRmJmF' \
#      'jdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

#URL=' https://www.amazon.fr/dp/B084DWG2VQ/ref=s9_acss_bw_pg_WFpfn19f_1_t?pf_rd_m=A1X6FK5RDHNB96&pf_rd_s=merchandised-search-1&pf_rd_r=YMX058ER8MC634ND0P2Z&pf_rd_t=101&pf_rd_p=8a42b39e-007c-4951-a9e4-b74c249d44d7&pf_rd_i=15601482031'


URL = 'https://www.ebay.es/itm/Apple-iPhone-12-5G-64GB-NUOVO-Originale-Smartphone-iOS-14-Black/133571359505?hash=item1f19793311:g:6AEAAOSwsgtfmasC'
URL2 = 'https://www.ebay.es/itm/Apple-Retina-MacBook-Pro-15-mid-2014-i7-16-512-GB-AZERTY-FR-Fully-working/274584725021?hash=item3fee86661d:g:3ScAAOSwB65ftjCH'

# Error     titulo = soup.find(id = 'productTitle' ).get_text()
# AttributeError: 'NoneType' object has no attribute 'get_text'
# Esto significa que no esta devolviendo las etiquetas que buscamos, puede ser por estructura de la pagina o que Amazon ha bloqueado request
# Informacion de error y posibles soluciones, las he probado todas sin resultado :(
# https://stackoverflow.com/questions/60139616/attributeerror-nonetype-object-has-no-attribute-get-text-python-web-scrapin
# https://blog.datahut.co/challenges-that-make-amazon-data-scraping-so-painful/
# Para probar el programa he usado otra pagina de ejemplo

# Tipo de explorador en el que vamos a abrir la url mencionada
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#          '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
# my user agent es un poco diferente:
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


# Función que comprueba el precio de un producto
def comprobar_precio():
    # Requerimos la pagina con url y header previamanete definido
    page = requests.get(URL, headers=headers)
    # Con el paquete de Beautiful soup usamos el metodo content donde podemos acceder a el contenido de nuestra pagina
    # contenido pareseado des html lo guardaos en la variable soup
    soup = BeautifulSoup(page.content, 'html.parser')
    # Usamos metodo find pasandole como parametro el identificador o etiqueta donde esta el titulo, precio de producto buscado
    # Amazon example
    # titulo = soup.find(id='productTitle').get_text().strip()
    # precio = soup.find(id='priceblock_ourprice').get_text().strip()
    # eBay example
    # Metodo get_Text() nos quita las etiquetas html y con metodo strip() removemos espacios en blanco
    titulo = soup.find(id='itemTitle').get_text().strip()
    precio = soup.find(id='prcIsum').get_text().strip()
    # Cadena de texto lo pasamos a float con slice, Removemos simbolo de euros y decimales
    # Amazon
    # precio = float(precio[:-5])
    # Ebay
    precio = float(precio[:-7])

    # Comparamos nuestro precio con un valor limite
    if precio < 300:
        # Si el precio baja a 900/300 enviaremos un email avisando de esto
    #    enviar_email()
    # print(titulo)
      print(precio)

    # Accederemos a todos los links de la pagina web
    # Funcion que crea un bucle donde encuentra las etiquetas "a" que estan asociadas a un url
    # enlaces = soup.find_all('a')
    # print(enlaces)

    # Creamos una lista vacia para agregar las urls
    lista = []
    lista_final = []
    # imprimimos titulo del articulo y precio
    print(titulo + "  " + "\n", precio)

    # Ebay  'mfe-reco-link' es el nombre de las div pero enlaces no tienen nombre especifico enlaces a iphone/product
    for link in soup.find_all('a', attrs={"class": "mfe-reco-link"}):
        # A cada uno de estos enlaces los agregamos a lista lista[]
        # Tenemos enlaces de productos y enlces de la pagina en el caso de ebay ya son
        # clickeables entonce no necesitamos otro bucle
        lista.append(str(link.get('href')))

    #Amazon
    # Accedemos a todos los links en la pagina con la etiqueta "a" y extraemos url de ellas
    # for link in soup.find_all('a'):
    # A cada uno de estos enlaces los agregamos a lista lista[]
    # Tenemos enlaces de productos y enlces de la pagina
    #    lista.append(str(link.get('href')))

    print(lista)
    # Debemos almacenar solo los enlaces de interes
    #for elemento in lista:
        # En Amazon ^/dp es el nombre de los (src)enlaces a iphone/product
        #  if re.findall('^/dp', elemento):
    #   lista_final.append('https://amazon.es/'+ elemento)

    #print(lista_final)

    # Bucle While que hara activo nuestro programa


#1 Editar la función comprobar_precio() para que reciba el html ya parseado
#de una página web como parámetro. La función debe devolver el título y el precio del producto que se le ha enviado.


def comprobar_precio2(s):
    tituloh1 = s.find('h1', attrs={'class': 'it-ttl'})
    # Metodo get_Text() nos quita las etiquetas html y con method strip() removemos espacios en blanco
    titulo = tituloh1.text.strip()
    percioid = s.find(id = "prcIsum")
    precio = percioid.text.strip()
    # Devolver imprimimos titulo y precio
    return (titulo, precio)



page2 = requests.get(URL2, headers=headers)
    # Con el paquete de Beautiful soup usamos el metodo content donde podemos acceder a el contenido de nuestra pagina
    # contenido pareseado de html lo guardamos en la variable soup2
soup2 = BeautifulSoup(page2.content, 'html.parser')
    #print(soup2)

print(comprobar_precio2(soup2))


#2º Crear una función que se encargue de hacer request a urls y devuelva un objeto soap con el html ya parseado.
#Como parámetro de entrada pordrá recibir una o más urls (decidir si como parametro variable (*args) o como lista).
##Tendrá que comprobar si recibe una o varias de manera que tendrá que devolver uno o varios objetos soap (objeto con el html parseado) en una lista.


def requestUrl(urlLista):
    #Lista vacia donde alamcenaremos los objetos soap
    ListaDeSOAP=[]
    # recorremos elementos url de la lista
    for url in urlLista:
        #por cada url en la lista
        req = requests.get(url)
        status_code = req.status_code
        #The request was fulfilled code 200 verificamos que urls sean validas
        if status_code == 200:
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            # Requerimos la pagina de cada url con header previamanete definido
            page = requests.get(url, headers=headers)
            # Con el paquete de Beautiful soup usamos el metodo content donde podemos acceder a el contenido de nuestra pagina
            soap = BeautifulSoup(page.content, 'html.parser')
            #Obtenemos contenido pareseado de cada url y la almacenamos en la variable soap
            #Agregamos las variables a la lista
            ListaDeSOAP.append(soap)
            #print(soap)
         #En caso que el status no es ok, devolvemos el staus como resutado
        else: ListaDeSOAP.append(status_code)
    # Devolemos la lista de equipos sin repetir valores
    return ListaDeSOAP

url1 = "https://www.apple.com/es/"
url2 = "http://www.jose.com/"
url3 = "https://www.leboncoin.fr/"
# Realizamos la petición a la web

urlLista = [url1,url2,url3]

print(requestUrl(urlLista))

while True:
    # Llamamos a nuestra funcion
    # comprobar_precio()
    # Frecuencia con la que queremos que esta funcion despierte y se ejecute en segundos
    time.sleep(100000)
