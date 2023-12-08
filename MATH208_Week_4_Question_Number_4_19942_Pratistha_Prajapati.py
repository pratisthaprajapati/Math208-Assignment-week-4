from scipy.stats import binom, norm
import numpy as np
import matplotlib.pyplot as plt
import datetime


num_of_trials = 50  
prob_success = 0.5  
prob_failure= 1 - prob_success  

num_of_successes= 25  
binomial_prob = binom.pmf(num_of_successes, num_of_trials, prob_success)

mean = num_of_trials* prob_success  
stdev= np.sqrt(num_of_trials * prob_success * prob_failure) 

normal_prob = norm.cdf(num_of_successes+ 0.5, mean, stdev) - norm.cdf(num_of_successes - 0.5, mean, stdev)


print("Date:" , datetime.datetime.today())
print(f"binomial probability {binomial_prob}, and normal probability {normal_prob}")

data = binom.rvs(num_of_trials, prob_success, size=1000)


plt.hist(data, bins=np.arange(num_of_trials + 1) - 0.5, density=True, alpha=0.7, color='blue', edgecolor='black')


plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution Histogram')


plt.show()

