prices = {"Mouse" : 500,"Keyboard" : 800 ,"Monitor" : 7000,"Pendrive" : 400,"Camera" : 5000}
discount = float(input("Enter discount percentage: "))
file = open("discount_report.txt", "w")
print("Product  |  Original Price  |  Discounted Price")
print("-----------------------------------------------")
total = 0
count = 0
for product, price in prices.items():
    discounted_price = price - (price * discount / 100)
    file.write(f"{product},{price},{discounted_price}\n")
    print(f"{product}  |  {price}  |  {discounted_price}")
    total += discounted_price
    count += 1
average = total / count
print("-----------------------------------------------")
print(f"Total Items: {count}")
print(f"Average Discounted Price: {average}")   
file.close()