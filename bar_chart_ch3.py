from matplotlib import pyplot as plt

movies = ["Batman Begins", "The Dark Knight", "The Dark Knight Rises"]
num_jokers = [0, 1, 0] 

# Note: Default bar width = 0.8; Add 0.1 to the left coordinates so that each is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]


# Plot the bars with left x-coordinates (xs) and heights of num_jokers
plt.bar(xs, num_jokers) 

# Label the chart
plt.ylabel("Jokers")
plt.title("Analysis of Joker apperances in the Nolan Batman Franchise")

# label x -axis with movie names at bar centers;
# Had to decrement the i + 0.5 down to i + 0.1 for the movie titles to look right
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

# show the plot
plt.show()

