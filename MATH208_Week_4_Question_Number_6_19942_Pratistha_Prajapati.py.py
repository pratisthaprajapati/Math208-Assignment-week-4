import numpy as np
from scipy.stats import  norm
import datetime
total_num_batteries= 150  
defect_rate = 0.06  

mean= total_num_batteries * defect_rate
stdev = np.sqrt(total_num_batteries * defect_rate * (1 - defect_rate))

normal_prob_12_or_more = 1 - norm.cdf(11.5, mean, stdev)

print("Date:" , datetime.datetime.today())
print(f"Probability of 12 or more defective ones is,{normal_prob_12_or_more}")

