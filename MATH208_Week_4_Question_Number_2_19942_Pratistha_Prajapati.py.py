import datetime
mean_X = 10  
stdev_X = 3  
mean_Y = 15  
stdev_Y = 8  

meanXplusY = mean_X + mean_Y
stdevXplusY = (stdev_X**2 + stdev_Y**2)**0.5


meanXSubtY = mean_X - mean_Y
StdevXSubtY = (stdev_X**2 + stdev_Y**2)**0.5


mean_3X = 3 * mean_X
stdev_3X = 3 * stdev_X


mean4Xplus5Y = 4 * mean_X + 5 * mean_Y
stdev4Xplus5Y = ((4 * stdev_X)**2 + (5 * stdev_Y)**2)**0.5

print("Date:" , datetime.datetime.today())
print(f"Mean and Standard Deviation for X + Y:  , mean :{meanXplusY}  , standard deviation:{stdevXplusY}")
print(f"Mean and Standard Deviation for X - Y:  , mean:{meanXSubtY}   , standard deviation {StdevXSubtY }")
print(f"Mean and Standard Deviation for 3X:     mean{ mean_3X }   , standard_deviation {stdev_3X}")
print(f"Mean and Standard Deviation for 4X + 5Y:, mean: {mean4Xplus5Y}  , standard deviation:{stdev4Xplus5Y}")

