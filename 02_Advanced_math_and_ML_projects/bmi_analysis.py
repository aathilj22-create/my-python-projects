import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dataset with missing data
health_data = {
    'Name': ['Rahul', 'Priya', 'Arun', 'Sneha', 'Vikram', 'Divya'],
    'Weight_Kg': [70, 55, np.nan, 62, 85, 52],
    'Height_Cm': [175, 160, 170, np.nan, 180, 155]
}
df = pd.DataFrame(health_data)

# 2. Data Cleaning: Filling missing values
df['Weight_Kg'] = df['Weight_Kg'].fillna(df['Weight_Kg'].mean())
df['Height_Cm'] = df['Height_Cm'].fillna(df['Height_Cm'].mean())

# 3. BMI Calculation: Formula -> Weight / (Height in meters squared)
df['BMI'] = df['Weight_Kg'] / ((df['Height_Cm'] / 100) ** 2)

print("--- Cleaned Dataset with Calculated BMI ---")
print(df)
print("=========================================")

# 4. Matplotlib & Seaborn Magic: Creating the colorful graph
plt.figure(figsize=(8, 5))
sns.barplot(x='Name', y='BMI', data=df, palette='Set2')

# Adding labels and styling
plt.title('BMI Analysis Dashboard', fontsize=14, fontweight='bold')
plt.xlabel('Names', fontsize=12)
plt.ylabel('BMI Value', fontsize=12)
plt.axhline(y=24.9, color='red', linestyle='--', label='Normal Upper Limit (24.9)')
plt.legend()

# 5. Display the Graph Window
print("Opening the colorful graph window now...")
plt.show()

# Keep terminal alive
input("\nPress Enter to exit...")