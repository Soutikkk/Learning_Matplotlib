# Cell 31

categories = np.array(["Grains", "Vegetables", "Fruits", "Dairy", "Meat", "Sweets"])

values = np.array([30, 20, 15, 10, 25, 9])

plt.barh(categories, values, color=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"])


plt.title("Daily Food Consumption", fontsize=14, fontweight="bold", color="purple")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
