from matplotlib import pyplot as plt
from math import exp

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x+y for x,y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)] 

# plt.plot can be called multiple times. 
# Useful for showing multiple items on the same chart.

plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line

# Because we've assigned labels to each series -> free legend 
# They were referring to the label='thing' part of plt.plot(...) 
# loc=9 means "top center"

plt.legend(loc=9)
plt.xlabel("Model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show() 


