import pandas as pd

# 1. Create a mock dataset related to car features and prices
car_data = {
    'Car_Name': ['Maruti Swift', 'Hyundai i20', 'Tata Altroz', 'Honda City', 'Toyota Fortuner'],
    'Engine_CC': [1200, 1200, 1500, 1500, 2800],
    'Price_Lakhs': [8, 9, 10, 15, 45],
    'Mileage_Kmpl': [22, 20, 19, 18, 12]
}

# 2. Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(car_data)

print("=========================================")
# 3. Display the first 3 rows of the dataset using head()
print("First 3 rows of the dataset:")
print(df.head(3))
print("=========================================")

# 4. Display dataset structural information using info()
print("\nDataset Information:")
print(df.info())
print("=========================================")

# 5. Display statistical summary of numerical columns using describe()
print("\nStatistical Summary:")
print(df.describe())
print("=========================================")

# 6. Keep the terminal window open until User presses Enter
input("\nPress Enter to exit...")