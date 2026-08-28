# Cell 16

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3= np.array([10, 20, 35, 40])

line_style = dict(marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black", linestyle="solid", linewidth=3)

plt.plot(x, y1, color="green", **line_style)
plt.plot(x, y2, color="blue", **line_style)
plt.plot(x, y3, color="orange", **line_style)
plt.show()
