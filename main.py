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
    session.clear_db(kategory=text)



def pars_paks_product_in_kategory(url_kategory:str,
                                  
                             teg_name:str,
                             class_name:str,

                             teg_pre:str,
                             class_pre:str,

                             teg_size:str,
                             class_size:str,

                             teg_img:str,
                             class_img:str,

                             teg_price:str,
                             class_price:str
):
    url = url_kategory
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    products_name_list = []
    products_preview_name_list = []
    sizes_list = []
    imgs_list =[]
    prices_list =[]

    products_name = soup.find_all(teg_name, class_=class_name)
    for product_name in products_name:
        #session.add_product_in_kategory()
        products_name_list.append(product_name.text)
  
    products_preview_name = soup.find_all(teg_pre, class_=class_pre)
    for product_preview_name in products_preview_name:
        products_preview_name_list.append(product_preview_name.text)

    sizes = soup.find_all(teg_size, class_=class_size)
    for size in sizes:
        sizes_list.append(size.text)

    imgs = soup.find_all(teg_img, class_=class_img)
    for img in imgs:
        imgs_list.append(img.text)

    prices = soup.find_all(teg_price, class_=class_price)
    for price in prices:
        prices_list.append(price.text)

    print(f'IMG\n{imgs_list}\nNAME\n{products_name_list}\nPRE\n{len(products_preview_name_list)}\nPRACE\n{len(prices_list)}\nSIZE\n{len(sizes_list)}')
    for i in range(0, len(imgs_list)):
        session.add_product_in_kategory('Сейфы', product_name='123', product_preview_name=products_preview_name_list[i], size=sizes_list[i], img='1', price=prices_list[i])
        i =+ 1

pars_paks_product_in_kategory('https://paksmet.ru/produktsiya/metallicheskie-shkafy-dlya-odezhdy', 'a', '', 'p', 'product-preview-name',  'div', 'size', 'img', '', 'div', 'price') """


url = 'https://paksmet.ru/produktsiya/garderobnye-sistemy'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
price = soup.find_all('div', class_='price')
prod = soup.find_all('p', class_='product-preview-name')
pro_list = []
price_list = []
for i in prod:
    pro_list.append(i.text)
for i in price:
    price_list.append(i.text)


print(f'\n{pro_list}\n')
print(f'\n{price_list}\n')
print(f'len pro_list - {len(pro_list)}\nlen price_list - {len(price_list)}')

    




