# read sale record from file
file = open ("sales_data.txt","r")
sales =[]
for line in file:
    sales.append(int(line.strip()))
file.close()

# calculate total, highest, lowest and average sales
total_sales = sum(sales)
highest_sales=max(sales)
lowest_sales=min(sales)
average_sales=total_sales/len(sales)

# print sale summary
print("-------Sale Summary-------")
print("Total Sales:", total_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Average Sales:", average_sales)