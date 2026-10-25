import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_cleaned.csv")
yearly_content = df.groupby(['release_year', 'type']).size().unstack(fill_value=0).reset_index()
recent_years = yearly_content[yearly_content['release_year'] >= 2000]

plt.figure(figsize=(13, 6))
plt.plot(recent_years['release_year'], recent_years['Movie'], marker='o', color='#E50914', label='Movies', linewidth=2)
plt.plot(recent_years['release_year'], recent_years['TV Show'], marker='s', color='#221F1F', label='TV Shows', linewidth=2)
plt.title("Netflix Content Production Trend Over the Years (2000 - Present)", fontsize=14, fontweight='bold')
plt.xlabel("Release Year")
plt.ylabel("Number of Titles Released")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title="Content Type")
plt.xticks(range(2000, int(recent_years['release_year'].max()) + 1, 2), rotation=45)
plt.tight_layout()
plt.savefig("yearly_release_trend.png", dpi=300)
print("Task 4 complete.")
