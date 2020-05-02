class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= percent_change
        elif is_increased == False:
            self.price /= percent_change
        return self

    def print_info(self):
        print(self.name, self.category, self.price)
        return self