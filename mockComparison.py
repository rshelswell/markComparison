import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# data per set
set1 = {'Set 1' : [99,97,92,79,72,96,99,78,78,83,96,93,81,64,87,99,89,80,90,77]}
set2 = {'Set 2' : []}
set3 = {'Set 3' : [31,47,38,37,19,34,63,12,32,32,30,34,39,44,57,32,43,37,57]}

# dataframe for each, then concat to avoid error due to differing column lengths
df1 = pd.DataFrame(data=set1)
df2 = pd.DataFrame(data=set2)
df3 = pd.DataFrame(data=set3)
df = pd.concat([df1, df2, df3], ignore_index=False, axis=1)

# melt data sets together
data_df = df.melt(var_name='Maths Set', value_name='Test %')

# boxplot with black datapoints and jitter
sns.boxplot(x='Maths Set', y='Test %', data=data_df)
sns.stripplot(x='Maths Set', y='Test %', color='black', alpha=0.5, data=data_df)

# output to desktop as hires png
plt.savefig(r"H:\Desktop\maths10Summer.png", dpi=300)
