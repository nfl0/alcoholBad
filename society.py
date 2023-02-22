import pandas as pd
import time

# Define the dataset
data = {
    "Country": ["USA", "UK", "Australia", "Canada", "Russia", "France", "Germany", "China"],
    "Population": [328.2, 67.1, 25.7, 38.0, 144.5, 66.9, 83.2, 1400.0],
    "Per capita alcohol consumption (liters)": [9.3, 9.6, 10.1, 8.2, 11.7, 11.4, 11.4, 7.2],
    "Alcohol-attributable deaths": [88, 20, 6, 10, 146, 35, 32, 29],
    "Alcohol-related crime rate": [3.3, 1.9, 1.1, 1.2, 4.5, 2.4, 1.7, 0.4],
    "Total economic cost (billions of USD)": [250, 18, 4, 8, 33, 24, 23, 10],
    "Alcohol tax revenue (billions of USD)": [16.2, 3.7, 1.2, 1.4, 1.8, 3.4, 4.5, 0.4]
}

# Create a Pandas DataFrame from the dataset
df = pd.DataFrame(data)

# Define the factors that impact the net impact of alcohol on society
cost_factors = ["Alcohol-attributable deaths", "Alcohol-related crime rate", "Total economic cost (billions of USD)"]
benefit_factors = ["Alcohol tax revenue (billions of USD)"]

# Calculate the total cost and benefit for each country
df["Total cost (billions of USD)"] = df[cost_factors].sum(axis=1)
df["Total benefit (billions of USD)"] = df[benefit_factors].sum(axis=1)

# Calculate the net impact of alcohol on society for each country
df["Net impact (billions of USD)"] = df["Total benefit (billions of USD)"] - df["Total cost (billions of USD)"]

# Loop through each country and print the results
for i, row in df.iterrows():
    print(f"""
    Analyzing data for {row['Country']}...
    Population: {row['Population']} million
    Per capita alcohol consumption: {row['Per capita alcohol consumption (liters)']} liters
    Alcohol-attributable deaths: {row['Alcohol-attributable deaths']}
    Alcohol-related crime rate: {row['Alcohol-related crime rate']} %
    Total economic cost: {row['Total economic cost (billions of USD)']} billion USD
    Alcohol tax revenue: {row['Alcohol tax revenue (billions of USD)']} billion USD
    Total cost: {row['Total cost (billions of USD)']} billion USD
    Total benefit: {row['Total benefit (billions of USD)']} billion USD
    Net impact: {row['Net impact (billions of USD)']} billion USD
    ===================================
    """)
    time.sleep(1)
