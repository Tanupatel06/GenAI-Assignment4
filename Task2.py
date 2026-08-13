# Read Entire File
file = open("sales_data.txt","r")
print("Using read:")
print(file.read())
file.close()

# Read Line by Line
file = open("sales_data.txt","r")
print("Using readline:")
print(file.readline().strip())
file.close()

# Read All Lines into a List
file = open("sales_data.txt","r")
lines = file.readlines()
file.close()

# Process the lines to convert them into integers
sales=[int(line.strip()) for line in lines]
print("Using readlines:")
print(sales)