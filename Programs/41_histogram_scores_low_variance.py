# Cell 48

scores = np.random.normal (loc= 80, scale = 1, size = 1000)

plt.hist(scores, bins=30, color='blue', alpha=0.7)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Scores")
plt.show()
