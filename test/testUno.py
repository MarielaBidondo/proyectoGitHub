import requests
from bs4 import BeautifulSoup
import re
import time
import io
import pytesseract

URL = 'https://www.amazon.es/Nuevo-Apple-iPhone-12-128-GB/dp/B08L5SVNZB/' \
      'ref=sr_1_1_sspa?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G4CC972YL84I&dchild' \
      '=1&keywords=iphone+12&qid=1604707287&quartzVehicle=93-1814&' \
      'replacementKeywords=iphone&sprefix=iphon%2Caps%2C215&sr=8-1-spons&psc=1&spLa=' \
      'ZW5jcnlwdGVkUXVhbGlmaWVyPUExMDlBT08wTElTNE5LJmVuY3J5cHRlZElkPUEwOTcxMzYySDRYOFlQM' \
      'TBXRlYwJmVuY3J5cHRlZEFkSWQ9QTA0NjgyNDkxNVBJTjhJT1VOWTkxJndpZGdldE5hbWU9c3BfYXRmJmF' \
      'jdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


'''Función que comprueba el precio de un producto'''
def comprobar_precio():
      page = requests.get(URL, headers=headers)

      soup = BeautifulSoup(page.content, 'html.parser')

      titulo = soup.find(id='productTitle').get_text().strip()
      precio = soup.find(id='priceblock_ourprice').get_text().strip()
      precio = float(precio[:-5])

      if precio < 900:
            enviar_email()

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


while True:
      comprobar_precio()
      time.sleep(10)