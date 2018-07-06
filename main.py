import pandas as pd
import matplotlib
import numpy

prices = [[70,71,73],[80,56,44],[54,56,85],[32,25,13],[10,98,75],[56,31,75],[44,22,55],[86,57,12]]

months= ['jan', 'feb', 'march']

simple_frame = pd.DataFrame(prices,columns=months)

pd.DataFrame(simple_frame).to_csv("output.csv")

# print('My simple data frame is \n', simple_frame)

# header_frame = pd.DataFrame(prices, columns=['jan', 'feb', 'march'])

# print('My data frame with headers \n',header_frame)

# print("value is \n", header_frame['jan'][0])

# print("First Five rows are")
#
# print(simple_frame.head())
#
# print('Last five rows')
#
# print(simple_frame.tail())