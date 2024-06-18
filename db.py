import sqlite3

class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
    
        
    def add_product_and_price(self, kategory:str, product:str, price:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {kategory} (
                       product TEXT UNIQUE,
                       price TEXT
        )
        ''')
        cursor.execute('INSERT INTO price_sell (product, price) VALUES (?,?)', (product, price))
        connect.commit()
        connect.close()


    def clear_db(self, kategory:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {kategory} (
                       product_name TEXT UNIQUE,
                       product_preview_name TEXT,
                       size TEXT,
                       img TEXT,
                       price TEXT
        )
        ''')

session = Session('paksmet.sqlite3')


