import requests
from bs4 import BeautifulSoup
from db import session
import uvicorn




""" url_katalog_paks = 'https://paksmet.ru/produktsiya'
response = requests.get(url_katalog_paks)

soup = BeautifulSoup(response.text, 'lxml')
products_html = soup.find_all('span', class_='')

products_list = []
for product in products_html:
    products_list.append(product.text)

for i in range(0, 8):
    products_list.pop(0)

for i in range(13, 15):
    products_list.pop()


for kategory in products_list:
    text = kategory.replace(' ', '_')
    session.clear_db(kategory=text) """



def pars_product_in_kategory(url_kategory:str):
    url = url_kategory
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    products_name_list = []
    products_preview_name_list = []
    sizes__list = []
    imgs_list =[]
    prices_list =[]

    products_name = soup.find_all()
    for product_name in products_name:
        products_name_list.append(product_name.text)
  
    products_preview_name = soup.find_all()
    for product_preview_name in products_preview_name:
        products_preview_name_list.append(product_preview_name.text)

    sizes = soup.find_all()
    for size in sizes:
        sizes__list.append(size.text)

    imgs = soup.find_all()
    for img in imgs:
        imgs_list.append(img.text)

    prices = soup.find_all()
    for price in prices:
        prices_list.append(price.text)




