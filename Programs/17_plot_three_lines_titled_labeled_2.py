# Cell 19

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3= np.array([10, 20, 35, 40])

plt.title("Class Size of Students in Different Years", fontsize=14, fontweight="bold", color="purple")
plt.xlabel("Years", fontsize=8, fontweight="bold", color="blue")
plt.ylabel("Number of Students", fontsize=8, fontweight="bold", color="blue")

plt.plot(x, y1, marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black", linestyle = "solid", linewidth=3, color="green")
plt.plot(x, y2, marker="o", markersize=8, markerfacecolor="blue", markeredgecolor="black", linestyle = "solid", linewidth=3, color="blue")
plt.plot(x, y3, marker="o", markersize=8, markerfacecolor="orange", markeredgecolor="black", linestyle = "solid", linewidth=3, color="orange")

plt.show()
