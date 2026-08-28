# Cell 35

categories = ["Fresher", "Juniors", "Seniors", "Leads", "Managers", "Directors"]

values = np.array([300, 200, 150, 100, 250, 90])

plt.pie(values, labels = categories, autopct='%1.1f%%', startangle=90, shadow=True)

plt.show()
