import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


plt.style.use(style="ggplot")

df = pd.read_csv('train.csv', index_col=0)
df.head()

df.plot.scatter(x='GarageArea', y='SalePrice')


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

index = df[(df['GarageArea'] >= 1000)|(df['GarageArea'] <= 180)].index
df.drop(index, inplace=True)
df['GarageArea'].describe()

df_out = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_out.shape)

plt.show()