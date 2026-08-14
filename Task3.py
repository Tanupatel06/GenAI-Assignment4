# create a new list of sales data
new_sales = [5000,2500,1700]

# append new sales data to the existing file
file = open("sales_data.txt","a")
for sale in new_sales:
    file.write(str(sale) + "\n")
file.close()

# print entire updated file contents
file = open("sales_data.txt","r")
print("Updated sales data:")
print(file.read())
file.close()

# count the total number of sales records in the file
file = open("sales_data.txt","r")
lines = file.readlines()
file.close()
print("Total sales records:", len(lines))
