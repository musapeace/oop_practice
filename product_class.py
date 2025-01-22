class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculating_total_value(self):
        return self.price * self.quantity


# Create an empty list to store product objects
products = []

while True:
    name = input("Enter product name (or 'done' to finish): ")
    if name.lower() == 'done':
        break  # Exit the loop if the user is done adding products

    price = int(input("Enter price amount: "))
    quantity = int(input("Enter quantity of product: "))

    # Create a Product object and add it to the products list
    product_instance = Product(name, price, quantity)
    products.append(product_instance)  # Append to the list, not the object

# Display the list of products
print("\nList of all products:")
for i, product in enumerate(products, start=1):
    print(f"{i}. {product.name} - Price: {product.price}, Quantity: {product.quantity}, Total Value: {product.calculating_total_value()}")

# Allow the user to select a product for more details
product_index = int(input("\nEnter the product number to view details: ")) - 1
if 0 <= product_index < len(products):
    selected_product = products[product_index]
    print(f"You selected: {selected_product.name}")
    print(f"Price: {selected_product.price}")
    print(f"Quantity: {selected_product.quantity}")
    print(f"Total Value: {selected_product.calculating_total_value()}")
else:
    print("Invalid product number!")
