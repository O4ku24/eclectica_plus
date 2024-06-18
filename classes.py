

class ProductsPAKS:
    def __init__(self,
                 product_name:str,
                 product_preview_name:str,
                 size:str,
                 img:str,
                 price:str,
                 url_kategory:str) -> None:
        self.product_name = product_name
        self.product_preview_name = product_preview_name
        self.size = size
        self.img = img
        self.price = price
        self.url_kategory = url_kategory

