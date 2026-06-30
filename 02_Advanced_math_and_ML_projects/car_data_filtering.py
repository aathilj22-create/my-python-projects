import pandas as pd

# 1. Create a detailed car dataset
car_market_data = {
    'Car_Name': ['Maruti Swift', 'Hyundai i20', 'Tata Altroz', 'Honda City', 'Toyota Fortuner', 'Mahindra Thar', 'Kia Seltos'],
    'Engine_CC': [1200, 1200, 1500, 1500, 2800, 2000, 1500],
    'Price_Lakhs': [8, 9, 10, 15, 45, 18, 16],
    'Fuel_Type': ['Petrol', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Diesel', 'Petrol']
}

# 2. Convert dictionary into Pandas DataFrame
df = pd.DataFrame(car_market_data)

# Making index start from 1 to 7 instead of 0 to 6
df['S.No'] = range(1, len(df) + 1)
df.set_index('S.No', inplace=True)

print("=========================================")
print("Complete Car Dataset (1 to 7):")
print(df)
print("=========================================")

# 3. Data Filtering - Condition 1: Budget Cars (Price less than or equal to 15 Lakhs)
budget_cars = df[df['Price_Lakhs'] <= 15]

print("\n--- Filtered Data: Budget Cars (<= 15 Lakhs) ---")
print(budget_cars)
print("=========================================")

# 4. Data Filtering - Condition 2: Powerful Diesel Cars (Engine > 1500 CC AND Diesel)
powerful_diesel = df[(df['Engine_CC'] > 1500) & (df['Fuel_Type'] == 'Diesel')]

print("\n--- Filtered Data: Powerful Diesel Cars (> 1500 CC) ---")
print(powerful_diesel)
print("=========================================")

# 5. Keep the terminal window open
input("\nPress Enter to exit...")