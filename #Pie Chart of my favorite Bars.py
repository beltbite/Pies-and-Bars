#%%
#Bar Chart of my favorite Pies
import seaborn as sns
import pandas as pd
import matplotlib as mbl
import matplotlib.pyplot as plt
import numpy as np

pie_df = pd.read_csv(r"C:\Users\Reape\OneDrive\Desktop\Pie Ranking.csv")
#print(pie_df)

#labels = pie_df['Pies']
#plt.figure(figsize=(8, 11))
#ax = sns.barplot(x= 'Pies', y='Likeness', data=pie_df, order=pie_df.sort_values('Likeness').Pies, hue="Pies", dodge=False)
#ax.set(xticklabels=[])
#ax.set(xticks=[])
#ax.set(xlabel='')
#plt.title('A Bar Graph of my Favorite Pies')
#plt.show()


bar_df = pd.read_csv(r"C:\Users\Reape\OneDrive\Desktop\Favbars.csv")
print(bar_df)
bars = bar_df['Favorite Bars']
likeness = bar_df['Likeness']
explode=(0,0,0,0,0.1,0)
plt.pie(likeness, labels = bars, explode = explode, autopct='%1.1f%%', startangle=100)
plt.title('A Pie Chart of my Favorite Bars')
plt.show()

# %%
