"""
Introduction to programming in Python for plotting and data manipulation.


"""

##################program

#get our data
data_file = "Test Data/car_data.csv"

open_file = open(data_file,"r") #open the data file

raw_data = [] #initialise empty array to put data into

'''
example = "string_1,string_2"
split_example = example.split(",")

print(example.split(","))
#example.split = ["string_1","string_2"]
'''


for line in open_file: #loop over the lines of open_file
    
    raw_data.append(line.split("\n")[0].split(",")) #append the line, split by "/n" (enter) and "," and append to raw_data

open_file.close() #close the data file

print(raw_data[0:5])