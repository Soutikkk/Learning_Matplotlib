# Cell 13

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y, marker="o", markersize=10, markerfacecolor="red", markeredgecolor="black", linestyle = "dotted")
plt.show()
