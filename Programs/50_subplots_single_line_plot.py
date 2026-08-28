# Cell 58

import numpy as np
import matplotlib.pyplot as plt

figure, axes = plt.subplots(2, 2)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

axes[0, 0].plot(x, x*2, color= "red")
axes[0,0].set_title("x * 2 ")

plt.show()
