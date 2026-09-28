import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importando o dataset tips

ds_tips = sns.load_dataset('tips')
#print(ds_tips)

#setando um estilo diferente no grafico
sns.set_style('dark')

#setando uma fonte maior
sns.set_context('notebook')

#tracando um scatterplot
sns.scatterplot(x='total_bill', y='tip', data=ds_tips)
plt.xlabel('Conta total em US$')
plt.ylabel('Gorgetas em US$')
plt.show()
