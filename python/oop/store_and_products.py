from store import Store
from product import Product


prod1 = Product("Skateboard Deck", 50, "Skate")
prod2 = Product("Skateboard Trucks", 40, "Skate")
prod3 = Product("Skateboard Wheels", 20, "Skate")
store1.add_product(prod1)
print(store1.product_list[0].name)