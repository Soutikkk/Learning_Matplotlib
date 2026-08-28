# Cell 68

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Pokemon.csv")

type_count =  (df["Type1"].value_counts())

plt.barh(type_count.index, type_count.values, color='red')


plt.show()
