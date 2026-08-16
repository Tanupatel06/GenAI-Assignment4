# write in file named products.txt
file = open("products.txt", "w")

# for adding 3 items in the file
for i in range(3):
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    file.write(f"{product_name},{product_price}\n")
file.close()

# Now reading fromthat particular file and displaying the content
file = open("products.txt", "r")
for line in file:
    product_name, product_price = line.strip().split(",")
    print(f"Product Name: {product_name}, Product Price: {product_price}")
file.close()