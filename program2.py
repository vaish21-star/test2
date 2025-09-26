
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('mtcars.csv')
print(df.head(10))

# Create a figure with 2 rows & 2 columns for 4 plots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1. Histogram of mpg
axs[0, 0].hist(df['mpg'], color='skyblue', edgecolor='black')
axs[0, 0].set_title('Histogram of MPG')
axs[0, 0].set_xlabel('MPG')
axs[0, 0].set_ylabel('Frequency')

# 2. Scatter plot of wt vs mpg
scatter = axs[0, 1].scatter(df['wt'], df['mpg'], color='green')
axs[0, 1].set_title('Scatter Plot: Weight vs MPG')
axs[0, 1].set_xlabel('Weight')
axs[0, 1].set_ylabel('MPG')
print(scatter)  # Will print <matplotlib.collections.PathCollection>

# 3. Bar plot of transmission type
bar = df['am'].value_counts().sort_index().plot(kind='bar', ax=axs[1, 0], color=['orange', 'cyan'])
axs[1, 0].set_title('Transmission Type')
axs[1, 0].set_xlabel('AM (0 = Auto, 1 = Manual)')
axs[1, 0].set_ylabel('Count')
print(bar)  # Will print <AxesSubplot>

# 4. Boxplot of mpg
box = sns.boxplot(ax=axs[1, 1], y=df['mpg'], color='violet')
axs[1, 1].set_title('Boxplot of MPG')
print(box)  # Will print <AxesSubplot>

# Adjust layout and show all plots together
plt.tight_layout()
plt.show()

# Five-number summary
print("Minimum MPG:", df['mpg'].min())
print("Maximum MPG:", df['mpg'].max())
print("Quantiles:\n", df['mpg'].quantile([0.10, 0.25, 0.5, 0.75]))
