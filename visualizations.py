
# Correlation heatmap
import seaborn as sns

plt.figure(figsize=(50,30))
sns.heatmap(data.corr(),cmap='coolwarm',annot=True)
