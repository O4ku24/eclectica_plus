
from app.src.db import session_paks, session_titan
from app.src.parsing import pars_titan_product_name

session_paks.clear_db('Системы_хранения_paks')

session_titan.clear_db('ГОТОВЫЕ_РЕШЕНИЯ')

pars_titan_product_name(url_kategoru='https://titangs.ru/product-category/otdelnye-elementi/gotovye-sistemy/',
                        name_table='ГОТОВЫЕ_РЕШЕНИЯ',

                        teg_name='div',
                        class_name='parts-catalog_details', 

                        teg_status='div',
                        class_status='label-stock in',

                        teg_price='bdi',
                        class_price='',

                        teg_img='div',
                        class_img='parts-catalog-img')


