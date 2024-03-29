# First let's import the packages we will use in this project
# You can do this all now or as you need them
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# Now we need to read in the data
df = pd.read_csv('movies.csv')
# 1) print(df)

# Missing data
# We need to see if we have any missing data
# Let's loop through the data and see if there is anything missing

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

# 2) print(df.dtypes)
# df['budget'] = df['budget'].astype('int64')
    
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0).astype(int)
df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(0).astype(int) 

df_ordered_by_gross = df.sort_values(by=['gross'], inplace=False, ascending=False)
# 3) print(df_ordered_by_gross)

# Drop any duplicates
df.drop_duplicates()

# Scatter plot with budget vs gross
""" 4) plt.scatter(x=df['budget'], y=df['gross'])
    plt.show() """

# We see that a few gross values are negative so we'll drop them
df = df[df['gross'] >= 0]

plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross earnings')
plt.xlabel('Budget')
plt.ylabel('Gross earning')
# plt.show()

# Plot budget vs gross using seaborn
sns.regplot(x="budget", y="gross", data=df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})
plt.show()

# Let's look at correlation
df.corr()

# There is a high correlation between budget and gross

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)