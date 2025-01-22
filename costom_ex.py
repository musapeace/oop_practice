class OutOfStockError(Exception):
    def __init__ (self, item_name):
        self.item_name = item_name

    def __str__ (self):
        return f"sorry, the item '{self.item_name}' is out of stock. "

# sample product_inventory 
product_inventory = {
    "apple" : 10,
    "banana" : 5,
    "orange" : 0, 
    "grapes" : 3
}
def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity

    except KeyError:
        print("sorry, '{item}' is not available in our inventory.")
                
try:
    purchase_item("apple", 3)
    purchase_item("orage", 1)
    purchase_item("watermelon", 1)
except OutOfStockError as e:
    print (e)