import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('restaurant_data.csv')

# Step 1: Check key columns
print("🧾 Columns:\n", df.columns)
print("\n🔍 Missing values:\n", df[['Longitude', 'Latitude', 'City', 'Locality']].isnull().sum())

# Step 2: Drop rows with missing location data
df.dropna(subset=['Longitude', 'Latitude', 'City', 'Locality'], inplace=True)

# Step 3: Count of restaurants per city
city_counts = df['City'].value_counts().head(10)
print("\n🏙️ Top 10 Cities with most restaurants:\n", city_counts)

# Step 4: Plot distribution on a map (scatter)
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Longitude', y='Latitude', hue='City', legend=False, alpha=0.6)
plt.title("Restaurant Locations (Top Cities Colored)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

# --- Average rating and cost per city ---
city_stats = df.groupby('City')[['Aggregate rating', 'Average Cost for two']].mean().sort_values(by='Aggregate rating', ascending=False).head(10)
print("\n⭐ Top 10 cities by average rating:\n", city_stats)

# --- Visualize top-rated cities ---
city_stats.plot(kind='bar', figsize=(12, 6), title='Top Cities by Avg Rating and Cost')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()
