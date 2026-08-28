# Cell 43

x = [0, 1 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
y = [55, 60, 65, 70, 75, 80, 85, 90, 95, 96, 95, 100]

plt.scatter(x, y, color="blue", alpha = 0.5, s = 100)

plt.xlabel("Hours Studied")
plt.ylabel("Scores Obtained")
plt.title("Relationship between Hours Studied and Scores Obtained")

plt.show()
