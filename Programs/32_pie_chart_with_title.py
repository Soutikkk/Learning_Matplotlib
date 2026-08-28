# Cell 37

categories = ["Fresher", "Juniors", "Seniors", "Leads", "Managers", "Directors"]

values = np.array([300, 200, 150, 100, 250, 90])

colors = ["#a81313", "#122806", "#5962c8", "#88694a", "#c2c2f0", "#da0c16"]

plt.pie(values, labels = categories, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors)

plt.title("Employee Distribution by Role", fontsize=14, fontweight="bold", color="purple")

plt.show()
