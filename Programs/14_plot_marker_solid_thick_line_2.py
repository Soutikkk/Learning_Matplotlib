# Cell 15

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])

plt.plot(x, y1, marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black", linestyle = "solid", linewidth=3, color="green")
plt.plot(x, y2, marker="o", markersize=8, markerfacecolor="blue", markeredgecolor="black", linestyle = "solid", linewidth=3, color="blue")
plt.show()
