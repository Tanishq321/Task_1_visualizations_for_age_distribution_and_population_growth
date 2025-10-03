import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load World Bank CSV
# =========================
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_607417.csv"  # update filename
df = pd.read_csv(file_path, skiprows=4)

# =========================
# Extract India's Population Data
# =========================
india_data = df[df['Country Name'] == "India"]
latest_year = india_data.columns[-2]  # last column before metadata
total_population = india_data[latest_year].values[0]

# =========================
# Age distribution (%)
# Replace with actual values if available
age_groups = ["0-14", "15-64", "65+"]
percentages = [26.6, 67.1, 6.3]  # Example for 2022

# Convert % to population in millions
populations = [(p/100) * total_population / 1e6 for p in percentages]

df_age = pd.DataFrame({
    "Age Group": age_groups,
    "Population (Millions)": populations,
    "Percentage": percentages
})

# =========================
# Plotting
# =========================
plt.figure(figsize=(9, 6))
bars = plt.bar(df_age["Age Group"], df_age["Population (Millions)"], 
               color=["#F4D03F", "#1ABC9C", "#E74C3C"], width=0.6, edgecolor="black", linewidth=1.2)

# Title
plt.title(f"India's Population Distribution by Age ({latest_year})", 
          fontsize=16, fontweight="bold", color="#2C3E50", pad=25)

# Axis Labels
plt.xlabel("Age Groups", fontsize=13, fontweight="bold", color="#2C3E50", labelpad=15)
plt.ylabel("Population (in Millions)", fontsize=13, fontweight="bold", color="#2C3E50")

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# =========================
# Annotate Bars (Inside)
# =========================
for bar, pop, perc in zip(bars, df_age["Population (Millions)"], df_age["Percentage"]):
    plt.text(bar.get_x() + bar.get_width()/2, 
             bar.get_height() - (bar.get_height()*0.1),  # inside bar
             f"{int(pop):,}M\n({perc:.1f}%)", 
             ha='center', va='top', fontsize=11, fontweight="bold", color="white")

# =========================
# Footer Caption
# =========================
total_pop_millions = total_population / 1e6
plt.figtext(0.5, 0.01, f"Total Population: {total_pop_millions:,.1f}M", 
            ha="center", fontsize=13, color="#2C3E50", fontweight="bold")

# Age Group Explanation
plt.figtext(0.5, -0.05, "0-14 = Children & Adolescents | 15-64 = Working Age | 65+ = Elderly", 
            ha="center", fontsize=11, color="#555555")

# =========================
# Final Touches
# =========================
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout(rect=[0, 0.08, 1, 1])  # extra space for footer
plt.show()
