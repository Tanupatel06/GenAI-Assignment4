# write a program to read file content if file exists
import os
filename = input("Enter File Name: ")
if os.path.exists(filename):
    file = open(filename, "r")
    print("\n File Content:\n")
    for line in file:
        print(line, end =" ")         
    file.close()
else:
    print("Please check the file names")