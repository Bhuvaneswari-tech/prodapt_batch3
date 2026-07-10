categories = []
products = []
stocks = []

num_categories = 3
num_products = 2

# Input
for i in range(num_categories):

    category = input(f"Enter Category {i+1}: ")
    categories.append(category)

    product_list = []
    stock_list = []

    for j in range(num_products):

        product = input(f"Enter Product {j+1} for {category}: ")
        quantity = int(input(f"Enter Stock for {product}: "))

        product_list.append(product)
        stock_list.append(quantity)

    products.append(product_list)
    stocks.append(stock_list)

# Display Inventory
print("\n--------- INVENTORY REPORT ---------")

for i in range(num_categories):

    print(f"\nCategory: {categories[i]}")

    for j in range(num_products):
        print(f"{products[i][j]} : {stocks[i][j]} units")