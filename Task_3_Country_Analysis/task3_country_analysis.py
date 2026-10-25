import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_cleaned.csv")
country_series = df['country'].dropna().apply(lambda x: [c.strip() for c in str(x).split(',')])
country_df = df.assign(single_country=country_series).explode('single_country')
country_df = country_df[~country_df['single_country'].isin(['Unknown', 'Not Given'])]
top_10_countries = country_df['single_country'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_10_countries.values, y=top_10_countries.index, palette='Reds_r')
plt.title("Top 10 Content Producing Countries on Netflix", fontsize=14, fontweight='bold')
plt.xlabel("Total Titles Available")
plt.ylabel("Country")
for index, value in enumerate(top_10_countries.values):
    plt.text(value + 15, index, str(value), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig("top_10_countries.png", dpi=300)
print("Task 3 complete.")
