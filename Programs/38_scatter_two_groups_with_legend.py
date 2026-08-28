# Cell 44

x1 = np.array([0, 1 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])
y1 = np.array([55, 60, 65, 70, 75, 80, 85, 90, 95, 96, 95, 100])

x2 = np.array([0, 1 , 2 , 2 , 2 , 4 , 5 , 5 , 7 , 8 , 9 , 10])
y2 = np.array([55, 60, 65, 70, 65, 20, 75, 90, 85, 96, 95, 100])


plt.scatter(x1, y1, color="blue", alpha = 0.5, s = 100, label="Group 1")
plt.scatter(x2, y2, color="red", alpha = 0.5, s = 100, label="Group 2")

plt.xlabel("Hours Studied")
plt.ylabel("Scores Obtained")
plt.title("Relationship between Hours Studied and Scores Obtained")

plt.legend()
plt.show()
