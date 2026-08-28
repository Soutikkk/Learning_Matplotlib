# Cell 50

scores = np.random.normal (loc= 80, scale = 10, size = 1000)
scores = np.clip(scores, 0 , 100)

plt.hist(scores, bins=30, color='blue', alpha=0.7)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Scores")
plt.show()
