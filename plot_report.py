# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset (replace with your actual dataset)
data = {
    'Sales': [120, 150, 180, 200, 210],
    'Profit': [20, 25, 40, 45, 50],
    'Cost': [80, 90, 100, 110, 120],
    'Rating': [3.5, 3.7, 4.0, 4.1, 4.2]
}

df = pd.DataFrame(data)

# -----------------------------
# Create a figure with two subplots
# -----------------------------
fig = plt.figure(figsize=(16, 6))

# Subplot 1: Correlation Heatmap
ax1 = fig.add_subplot(1, 2, 1)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax1)
ax1.set_title('Correlation Heatmap')

# Subplot 2: Pairplot (scatter matrix)
# Note: Pairplot creates its own figure, so we will use a workaround to include it
pairplot_fig = sns.pairplot(df, diag_kind='hist', kind='scatter', corner=False)
pairplot_fig.fig.suptitle('Pairplot / Scatter Matrix', y=1.02)

# Save both separately
fig.tight_layout()
fig.savefig('heatmap_subplot.png')
pairplot_fig.savefig('pairplot_subplot.png')

# Display both
plt.show()
pairplot_fig.show()
