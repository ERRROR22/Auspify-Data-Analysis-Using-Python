import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_cleaned.csv")
sns.set_theme(style="whitegrid")
fig = plt.figure(figsize=(16, 11))
fig.suptitle("Netflix Business Intelligence Executive Dashboard", fontsize=18, fontweight='bold', y=0.98)

ax1 = plt.subplot(2, 2, 1)
df['type'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#E50914', '#333333'], ax=ax1, startangle=140)
ax1.set_title("Catalog Composition", fontweight='bold')
ax1.set_ylabel("")

ax2 = plt.subplot(2, 2, 2)
df['country'].value_counts().head(5).plot(kind='bar', color='#E50914', ax=ax2)
ax2.set_title("Top 5 Content Producing Countries", fontweight='bold')
ax2.tick_params(axis='x', rotation=20)

ax3 = plt.subplot(2, 2, 3)
recent_releases = df[df['release_year'] >= 2010]['release_year'].value_counts().sort_index()
recent_releases.plot(kind='line', marker='o', color='#E50914', ax=ax3, linewidth=2)
ax3.set_title("Content Volume Growth (2010 - Present)", fontweight='bold')

ax4 = plt.subplot(2, 2, 4)
top_ratings = df['rating'].value_counts().head(6).index
sns.countplot(data=df[df['rating'].isin(top_ratings)], x='rating', order=top_ratings, palette="dark:salmon_r", ax=ax4)
ax4.set_title("Top 6 Content Ratings", fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("executive_bi_dashboard.png", dpi=300)
print("Task 6 complete.")
