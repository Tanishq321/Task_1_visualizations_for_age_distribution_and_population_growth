import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load World Bank dataset (place CSV file inside same folder or give path)
data = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_607417.csv", skiprows=4)

# Filter for India only
india_data = data[data["Country Name"] == "India"].T

# Keep only year rows (numeric indexes)
india_data = india_data[india_data.index.str.isnumeric()]

# Rename columns
india_data.columns = ["Population"]
india_data.index.name = "Year"
india_data.reset_index(inplace=True)

# Convert columns
india_data["Year"] = india_data["Year"].astype(int)
india_data["Population"] = india_data["Population"].astype(float) / 1e9  # Convert to Billions

# ✅ Plot with UI/UX Design
sns.set_theme(style="whitegrid")

plt.figure(figsize=(14,7))
sns.barplot(x="Year", y="Population", data=india_data, palette="viridis", alpha=0.9)

# Titles & Labels
plt.title("India's Population Growth (1960 - 2023)", fontsize=20, fontweight="bold", color="#2C3E50")
plt.xlabel("Year", fontsize=14, color="#34495E")
plt.ylabel("Population (Billions)", fontsize=14, color="#34495E")

# Rotate x-axis labels for clarity
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize=12)

# Remove extra borders
sns.despine()

# Annotate last bar with value
last_year = india_data.iloc[-1]
plt.text(last_year["Year"], last_year["Population"]+0.05,
         f"{last_year['Population']:.2f} B",
         ha="center", fontsize=12, fontweight="bold", color="darkred")

plt.tight_layout()
plt.savefig("india_population_growth.png", dpi=300)  # Save image
plt.show()