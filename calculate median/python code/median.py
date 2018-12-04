# import library 
import pandas as pd

# Provide file location
source_data = "D:/Python Code/median_data.xlsx"
# read the excel file
read_file= pd.read_excel(source_data)

# print median of the selected column.
print ("Median of the column 1 is ",  read_file["Data 1"].median())

# print median of all the columns.
print (read_file.median())