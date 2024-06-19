import sqlite3

class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
    
        
    def add_product_in_kategory(self, kategory:str, product_name:str, product_preview_name:str, size:str, img:str, price:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'INSERT INTO {kategory} (product_name, product_preview_name, size, img, price) VALUES (?,?,?,?,?)', (product_name, product_preview_name, size, img, price))
        connect.commit()
        connect.close()


    def clear_db(self, kategory:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {kategory} (
                       product_name TEXT,
                       product_preview_name TEXT,
                       size TEXT,
                       img TEXT,
                       price TEXT
        )
        ''')

session = Session('paksmet.sqlite3')


