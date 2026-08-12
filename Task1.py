# write sale record to a file
sales = [1200,450,980,1500,3000]

# write data to a file
file = open("sales_data.txt","w")
for sale in sales:
    file.write(str(sale) + "\n")
file.close()

#reopen and print the contents of the file
file = open("sales_data.txt","r")
print(file.read())
file.close