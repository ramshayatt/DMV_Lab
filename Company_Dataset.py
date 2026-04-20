import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (replace with your file path)
df = pd.read_csv('companies.csv')

# Extract columns
companies = df['Company']
employees = df['Employees']

# Create pie chart
plt.figure(figsize=(8,8))
plt.pie(employees, labels=companies, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Employee Distribution Across Companies')

# Show chart
plt.axis('equal')  # Ensures circle shape
plt.show()
