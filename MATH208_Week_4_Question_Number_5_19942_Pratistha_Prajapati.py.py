
import numpy as np
from scipy.stats import binom, norm
import datetime

num_of_trials= 12 
P_getting_heads = 0.5 


mean = num_of_trials * P_getting_heads
stdev = np.sqrt(num_of_trials * P_getting_heads * (1 - P_getting_heads))



normal_prob_getting_6 = norm.cdf(6.5, mean, stdev) - norm.cdf(5.5, mean, stdev)
print("Date: ", datetime.datetime.today())
print(f"The value of Normal Probability of getting exactly 6 heads is,{normal_prob_getting_6}")
