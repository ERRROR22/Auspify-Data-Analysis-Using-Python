import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_cleaned.csv")
type_counts = df['type'].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(x=type_counts.index, y=type_counts.values, palette=['#E50914', '#221F1F'], ax=axes[0])
axes[0].set_title("Total Count of Movies vs TV Shows", fontsize=14, fontweight='bold')
axes[0].set_ylabel("Count")
for p in axes[0].patches:
    axes[0].annotate(f"{int(p.get_height())}", (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                     ha='center', va='center', color='white', fontsize=12, fontweight='bold')

axes[1].pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90,
            colors=['#E50914', '#564d4d'], wedgeprops=dict(width=0.4, edgecolor='white'))
axes[1].set_title("Content Distribution Proportions", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("content_type_distribution.png", dpi=300)
print("Task 2 complete.")
