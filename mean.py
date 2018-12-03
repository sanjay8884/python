# import library 
import pandas as pd

# Provide file location
source_data = "D:/Python Code/mean_data.xlsx"
# read the excel file
read_file= pd.read_excel(source_data)

# print mean of the selected column.
print ("Average of the column 1 is ",  read_file["Data 1"].mean())

# print mean of all the columns.
print (read_file.mean())