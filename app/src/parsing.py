import requests
from bs4 import BeautifulSoup
from app.src.db import session_paks, session_titan

def pars_titan(url:str,
               teg:str,
               class_:str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    text = soup.find_all(teg, class_)
    seo_text = []
    for i in text:
        seo_text.append(i.text)

    return seo_text

def pars_titan_product_name(url_kategoru:str,
                            name_table:str,

                            teg_name:str,
                            class_name:str,
                            
                            teg_status:str,
                            class_status:str,
                            
                            teg_price:str,
                            class_price:str,
                            
                            teg_img:str,
                            class_img:str) -> list:
    
    response = requests.get(url_kategoru)
    soup = BeautifulSoup(response.text, 'lxml')



    products_name = soup.find_all(teg_name, class_name)
    products_name_list = []
    for i in products_name:
        
        products_name_list.append(i.text.rsplit('\n', 10)[1])
    
    products_status = soup.find_all(teg_status, class_status)
    products_status_list = []
    for i in products_status:
        products_status_list.append(i.text)

    products_price = soup.find_all(teg_price, class_price)
    products_price_list_1 = []
    for i in products_price:
        products_price_list_1.append(i.text)
    products_price_list_2 = []
    for el in products_price_list_1:
        products_price_list_2.append(el.replace(' ', ''))
    products_price_list = []
    for element in products_price_list_2:
        products_price_list.append(element.replace('\n', ''))

    text_html = soup.find_all(teg_img, class_img)
    text_list = []
    url_img_list = []
    for i in text_html:
        text_list.append(i)
    for i in text_html:
        url_img_list.append(i['style'].replace('background-image:url(', '').replace(');',''))

    

    #print(f'name - {products_name_list}\n\n statys - {products_status_list}\n\n price - {products_price_list_2}\n\n img - {url_img_list}')



    for product_name, product_status, product_price, product_img in zip(products_name_list, products_status_list, products_price_list_2, url_img_list):
        session_titan.add_product_in_kategory(name_table, product_name, product_status, product_price, product_img)
    print('Спиздили')

        
        

    
    
        
        
   