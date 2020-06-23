import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sb


plt.style.use(style="ggplot")

df = pd.read_csv('winequality-red.csv', index_col=0)
df.head()

pearsoncorr = df.corr(method='pearson')
print(pearsoncorr)

sb.heatmap(pearsoncorr,
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

print(df['quality'].isnull().sum())


df.plot.scatter(x='quality', y='density')
plt.show()

