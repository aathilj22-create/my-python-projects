import pandas as pd

# 1. Detailed car dataset
car_market_data = {
    'Car_Name': ['Maruti Swift', 'Hyundai i20', 'Tata Altroz', 'Honda City', 'Toyota Fortuner', 'Mahindra Thar', 'Kia Seltos'],
    'Engine_CC': [1200, 1200, 1500, 1500, 2800, 2000, 1500],
    'Price_Lakhs': [8, 9, 10, 15, 45, 18, 16],
    'Fuel_Type': ['Petrol', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol']
}

df = pd.DataFrame(car_market_data)

print("=========================================")
print("Original Car Dataset:")
print(df)
print("=========================================")

# 2. Data Grouping - Group by 'Fuel_Type' and calculate average (mean) price
grouped_fuel = df.groupby('Fuel_Type')['Price_Lakhs'].mean()

print("\n--- Grouped Data: Average Price by Fuel Type ---")
print(grouped_fuel)
print("=========================================")

# 3. Data Grouping - Count how many cars are there in each Fuel Type
car_counts = df.groupby('Fuel_Type')['Car_Name'].count()

print("\n--- Grouped Data: Number of Cars by Fuel Type ---")
print(car_counts)
print("=========================================")

# Keep terminal open
input("\nPress Enter to exit...")