import numpy as np
import datetime

Given_P = 0.05
n_greater_50= 55 

expected_mean = n_greater_50* Given_P
q = 1 - Given_P  
expected_std_dev = (n_greater_50 * Given_P * q) ** 0.5

np.random.seed(0)  
simulation_data = np.random.binomial(n_greater_50, Given_P, 10000) 

sample_mean = np.mean(simulation_data)
sample_std_dev = np.std(simulation_data)

print("Date:" , datetime.datetime.today())
print(f'The value of expected mean is {round(expected_mean,4)} and sample mean is {round(sample_mean,4)}')
print(f'The value of standard deviation  is {round(expected_std_dev,4)} and sample standard deviation  is {round(sample_std_dev,4)}')