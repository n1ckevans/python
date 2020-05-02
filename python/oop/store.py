from product import Product

class Store:
    def __init__(self, name, product_list=[]):
        self.name = name
        self.product_list = product_list
        self.products = Product(name="", price=0, category="")
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id):
        self.product_list -= product_list[id]
        print(product_list[id])
        return self

    def inflation(self, percent_increase):
        Store.products.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        Store.products.category = category
        Store.products.update_price(percent_discount, False) 
        return self