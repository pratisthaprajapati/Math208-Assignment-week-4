from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
import datetime

deg_of_freedom = 10  
rand_num = t.rvs(deg_of_freedom, size=100)

mean= np.mean(rand_num)
stdev= np.std(rand_num)

num_samples = 30
num_groups = 15
sample_group_means = []
for _ in range(num_groups):
     sample = np.random.choice(rand_num, size=num_samples, replace=False)
     sample_group_means.append(np.mean(sample))


mean_of_means = np.mean(sample_group_means)


stdev_x = np.std(sample_group_means)
expected_stdev_x = stdev/ np.sqrt(num_samples)


print("Date:" , datetime.datetime.today())
print(f"The value of mean is,{mean}") 
print(f"The value of standard deviation is,{stdev}")  
print(f"The value of mean of means is,{mean_of_means}") 
print(f"The value of Second Standard Deviation is,{stdev_x}") 
print(f"The value of expected Standard Deviation is,{expected_stdev_x}") 

plt.hist(sample_group_means, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means')
plt.show()


