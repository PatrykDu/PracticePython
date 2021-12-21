import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sampledata_x_2.txt') * 2
pd.DataFrame.to_csv(df, 'sampledata2', index=False)

df.plot(x='x', y='y', kind='scatter')
plt.show()
