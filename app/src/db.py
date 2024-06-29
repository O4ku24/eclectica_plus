import sqlite3

class Session:
    def __init__(self, name:str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self}'
    
        
    def add_product_in_kategory(self, name_table:str, 
                                product_name:str, 
                                status:str, 
                                price:str, 
                                url_img:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        
        cursor.execute(f'INSERT INTO {name_table} (product_name, status, price, url_img) VALUES (?,?,?,?)', 
                       (product_name, status, price, url_img))
        connect.commit()
        connect.close()



    def clear_db(self, name_table:str):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name_table} (
                       id INTEGER PRIMARY KEY,
                       product_name TEXT,
                       status TEXT,
                       price TEXT,
                       url_img TEXT
        )
        ''')
        
    def get_table_data(self, name_table:str) -> list[str]:
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute(f'SELECT * FROM {name_table}')
        data = cursor.fetchall()
        connect.close()
        return data
        
session_paks = Session('paksmet.sqlite3')
session_titan = Session('titan.sqlite3')

