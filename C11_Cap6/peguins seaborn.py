import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_penguins = sns.load_dataset('penguins')
print(ds_penguins.columns)

#tracando o histograma

sns.histplot(
    data = ds_penguins, #passando o dataset
    x = 'flipper_length_mm',
    hue = 'species',
    kde = True
)
plt.show()