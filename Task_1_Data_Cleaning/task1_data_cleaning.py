import pandas as pd

# Step 1: Load Dataset
df = pd.read_csv("Dataset.csv")
print("Original Shape:", df.shape)

# Step 2: Clean whitespaces & handle missing/duplicate records
string_cols = ['type', 'title', 'director', 'country', 'rating', 'duration', 'listed_in']
for col in string_cols:
    df[col] = df[col].astype(str).str.strip()

df = df.drop_duplicates()

# Step 3 & 4: Standardize columns
df['type'] = df['type'].replace({'movie': 'Movie', 'tv show': 'TV Show', 'Tv Show': 'TV Show'})
df['rating'] = df['rating'].str.upper()
df['director'] = df['director'].replace({'': 'Not Given', 'nan': 'Not Given'})
df['country'] = df['country'].replace({'': 'Unknown', 'nan': 'Unknown'})
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_unit'] = df['duration'].str.extract(r'([a-zA-Z]+)')

# Step 5: Export cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
print("Data Cleaning Complete. Saved as netflix_cleaned.csv")
