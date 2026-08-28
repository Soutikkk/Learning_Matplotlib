# Cell 61

import numpy as np
import matplotlib.pyplot as plt

figure, axes = plt.subplots(2, 2)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

axes[0, 0].plot(x, x*2, color= "red")
axes[0,0].set_title("x * 2 ")

axes[0,1].plot(x, x**2, color= "blue")
axes[0,1].set_title("x ** 2 ")

axes[1,0].plot(x, x**3, color= "green")
axes[1,0].set_title("x ** 3 ")

axes[1,1].plot(x, np.sqrt(x), color= "orange")
axes[1,1].set_title("sqrt(x) ")

plt.tight_layout()  # Adjusts the spacing between subplots for better visibility

plt.show()
