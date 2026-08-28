# Cell 66

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Pokemon.csv")

print (df["Type1"].value_counts())
