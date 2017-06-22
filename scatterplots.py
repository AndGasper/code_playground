from matplotlib import pyplot as plt 


friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes) # scatter plot built in method?

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count), # out the label with its point
                 xytext=(5,-5), # Give the text a slight offset
                 textcoords='offset points'
                 )
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("Number of friends (a.u.)")
plt.ylabel("Time spent on site (minutes/day)")
plt.show() 