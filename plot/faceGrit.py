import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
print(tips.head())

tips['Tips Percentage'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row='sex', col='time', margin_titles=True)
grid.map(plt.hist, "Tips Percentage", bins=np.linspace(0,40,15))

