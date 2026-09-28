import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds_tips = sns.load_dataset('tips')

#Selecionando as colunas que quero indentificar uma correlacao
corr = ds_tips[['total_bill', 'tip', 'size']].corr()

#tracando o heatmap
sns.heatmap(
    corr,
    annot = True,
    fmt = '.2f',
)
plt.show()