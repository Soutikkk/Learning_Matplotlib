# Cell 27

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

plt.grid(axis= "both", linestyle="--", linewidth=1, color="gray", alpha=0.5)
plt.plot(x,y)
plt.show()
