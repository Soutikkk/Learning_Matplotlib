# Cell 29

categories = np.array(["Grains", "Vegetables", "Fruits", "Dairy", "Meat", "Sweets"])

values = np.array([30, 20, 15, 10, 25, 9])

plt.bar(categories, values)


plt.title("Daily Food Consumption", fontsize=14, fontweight="bold", color="purple")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
