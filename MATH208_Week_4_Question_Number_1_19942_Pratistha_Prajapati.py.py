import scipy.stats as stats
import datetime

mean = 10.3  
standard_deviation= 0.65  

length_a = 9
Plesser_9cm = stats.norm.cdf(length_a, mean, standard_deviation)*100


length_b1 = 9.5
length_b2 = 10.6
Pbetn_9_5cm_and_10_6cm = (stats.norm.cdf(length_b2, mean, standard_deviation) - stats.norm.cdf(length_b1, mean, standard_deviation))*100

percentile= 80
minlentop_20percent= stats.norm.ppf(percentile / 100, mean, standard_deviation)

print("Date: ", datetime.datetime.today())
print(f"Probability of American anchovies less than 9cm,{ Plesser_9cm}%") 
print(f"Probability of American anchovies between 9.5 c and 10.6cm,{ Pbetn_9_5cm_and_10_6cm}%") 
print(f"Probability of American anchovies minimum length in the top of 20percent,{ minlentop_20percent}%") 