"""
Introduction to programming in Python for plotting and data manipulation.


"""

##################imports

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##################program

#get our data
data_file = "Test Data/car_data.csv"

open_file = open(data_file,"r") #open the data file

raw_data = [] #initialise empty array to put data into

for line in open_file: #loop over the lines of open_file
    
    raw_data.append(line.split("\n")[0].split(",")) #append the line, split by "/n" (enter) and "," and append to raw_data

open_file.close() #close the data file

data = np.array(raw_data) #trun raw data into numpy array

print(data[0]) #inspect 1st line (column labels)

print(data[1]) #inspect 2nd line (1st row of data)

