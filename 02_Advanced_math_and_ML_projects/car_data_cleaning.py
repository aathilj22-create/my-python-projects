import pandas as pd
import numpy as np

# 1. Updated car dataset with missing (NaN) values for data cleaning
car_data = {
    'Car_Name': ['Maruti Swift', 'Hyundai i20', 'Tata Altroz', 'Honda City', 'Toyota Fortuner', 'Toyota Glanza'],
    'Engine_CC': [1200, np.nan, 1500, 1500, 2800, 1200],
    'Price_Lakhs': [8, 9, np.nan, 15, 45, 7],
    'Mileage_Kmpl': [22, 20, 19, 18, 12, np.nan]
}

# 2. Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(car_data)

print("=========================================")
print("Original Dataset Before Data Cleaning:")
print(df)
print("=========================================")

# 3. Data Cleaning: Handling Missing Values
# Fill missing Engine_CC with the mean (average) value
df['Engine_CC'] = df['Engine_CC'].fillna(df['Engine_CC'].mean())

# Fill missing Mileage_Kmpl with the median value
df['Mileage_Kmpl'] = df['Mileage_Kmpl'].fillna(df['Mileage_Kmpl'].median())

# Drop rows where the critical price information is missing
df_cleaned = df.dropna(subset=['Price_Lakhs'])

print("\n=========================================")
print("Cleaned Dataset After Handling Missing Values:")
print(df_cleaned)
print("=========================================")

# 4. Display statistical summary of the cleaned dataset
print("\nStatistical Summary of Cleaned Data:")
print(df_cleaned.describe())
print("=========================================")

# 5. Data Export: Saving the cleaned data into an Excel file
excel_file_name = "Cleaned_Car_Data.xlsx"
df_cleaned.to_excel(excel_file_name, index=False)
print(f"\nSuccess! Cleaned data exported to '{excel_file_name}'")

# 6. Keep the terminal window open
input("\nPress Enter to exit...")