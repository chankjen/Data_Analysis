# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.offline as pyo

# Step 1: Load datasets
# Beverages dataset (Excel .xlsx)
beverages_df = pd.read_excel('beverages.xlsx')

# Fruits dataset (CSV .csv)
fruits_df = pd.read_csv('fruits.csv')

# Step 2: Basic Data Analysis
# Beverages dataset
average_price = beverages_df['Price ($)'].mean()
most_popular = beverages_df.loc[beverages_df['Popularity (1-10)'].idxmax(), 'Beverage']

# Fruits dataset
average_sweetness = fruits_df['Sweetness (1-10)'].mean()
red_fruits = fruits_df[fruits_df['Color'] == 'Red']

# Print analysis results
print("Beverages Dataset Analysis:")
print(f"Average Price of Beverages: ${average_price:.2f}")
print(f"Most Popular Beverage: {most_popular}\n")

print("Fruits Dataset Analysis:")
print(f"Average Sweetness of Fruits: {average_sweetness:.1f}")
print(f"Number of Red Fruits: {len(red_fruits)}")
print(red_fruits)

# Step 3: Visualizations
# Histogram: Distribution of Beverage Prices
plt.figure(figsize=(8, 6))
sns.histplot(beverages_df['Price ($)'], bins=5, kde=True, color='skyblue')
plt.title('Distribution of Beverage Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.show()

# Pie Chart: Popularity of Beverages
plt.figure(figsize=(8, 6))
plt.pie(beverages_df['Popularity (1-10)'], labels=beverages_df['Beverage'], autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet'])
plt.title('Popularity of Beverages')
plt.show()

# Histogram: Distribution of Fruit Sweetness
plt.figure(figsize=(8, 6))
sns.histplot(fruits_df['Sweetness (1-10)'], bins=5, kde=True, color='lightgreen')
plt.title('Distribution of Fruit Sweetness')
plt.xlabel('Sweetness (1-10)')
plt.ylabel('Frequency')
plt.show()

# Pie Chart: Distribution of Fruit Colors
color_counts = fruits_df['Color'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(color_counts, labels=color_counts.index, autopct='%1.1f%%', colors=['red', 'yellow', 'purple', 'orange'])
plt.title('Distribution of Fruit Colors')
plt.show()

# Step 4: Advanced Visualization - 3D Mesh Chart
# Create 3D Mesh Chart for Beverages
fig = go.Figure(data=[go.Mesh3d(
    x=beverages_df['Price ($)'],
    y=beverages_df['Popularity (1-10)'],
    z=beverages_df['Calories'],
    color='lightblue',
    opacity=0.8,
    name='Beverages'
)])

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title='Price ($)',
        yaxis_title='Popularity (1-10)',
        zaxis_title='Calories'
    ),
    title='3D Mesh Chart: Beverages (Price, Popularity, Calories)'
)

# Render the chart
pyo.plot(fig, filename='3d_mesh_chart.html')  # Opens in browser
