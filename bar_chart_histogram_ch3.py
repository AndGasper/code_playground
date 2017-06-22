from matplotlib import pyplot as plt 
import collections 


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# decile takes a student's grade and divides it by 100
# histogram = collections.Counter(...) part is where the y-axis gets its values
decile = lambda grade: grade // 10 * 10  # lambda function related to anonymous function? So we're saving the anonymous function to a variable?
# lambda = function -> anonymous function expecting a parameter, here it is grade
histogram = collections.Counter(decile(grade) for grade in grades) # collections.Counter is a container that keeps track of how many times equivalent values are added 

# plt.bar(x-offset, y-values, bar width) ? 
plt.bar( 
        [x-4 for x in histogram.keys()], # Shift each bar to the left by 4 units
        histogram.values(), # Make the bar's height equal to its value
        8 # width of each bar
        )

# [x_min, x_max, y_min, y_max] 
# Had to edit the offset for the bar graph
plt.axis([-10, 105, 0, 5]) 

plt.xticks([10 * i for i in range(11)]) # x-axis tick marks increment by 10 for 11 values 
plt.xlabel("Decile") 
plt.ylabel("Number of students") 
plt.title("Distribution of Exam 1 Grades")
plt.show() 
         
