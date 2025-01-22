# Data_Analysis
PLP Academy Practice

Here’s a concise summary of the analysis, highlighting the importance of each step:

---

### **Summary of the Analysis**

#### **1. Dataset Creation**
   - **Beverages Dataset (Excel `.xlsx`)**:
     - Contains columns: `Beverage`, `Price ($)`, `Popularity (1-10)`, `Calories`.
     - Used to analyze beverage prices, popularity, and calorie content.
   - **Fruits Dataset (CSV `.csv`)**:
     - Contains columns: `Fruit`, `Color`, `Sweetness (1-10)`.
     - Used to analyze fruit sweetness and color distribution.
   - **Importance**:
     - Real-world datasets make the analysis relatable and engaging for beginners.
     - Demonstrates handling different file formats (Excel and CSV).

---

#### **2. Loading Datasets**
   - Used `pandas` to load:
     - Excel file: `pd.read_excel('beverages.xlsx')`.
     - CSV file: `pd.read_csv('fruits.csv')`.
   - **Importance**:
     - Introduces data import using `pandas`, a fundamental skill in data analysis.
     - Highlights the need for libraries like `openpyxl` for Excel files.

---

#### **3. Basic Data Analysis**
   - Calculated:
     - Average price of beverages.
     - Most popular beverage.
     - Average sweetness of fruits.
     - Number of red fruits.
   - **Importance**:
     - Teaches basic statistical operations (e.g., mean, max).
     - Demonstrates filtering and querying data.

---

#### **4. Visualizations**
   - **Histograms**:
     - Visualized distribution of beverage prices and fruit sweetness.
     - Used `seaborn.histplot()` for clean and informative plots.
   - **Pie Charts**:
     - Showed popularity of beverages and distribution of fruit colors.
     - Used `matplotlib.pyplot.pie()` for simple and effective visuals.
   - **Importance**:
     - Visualizations make data trends and patterns easier to understand.
     - Introduces libraries like `matplotlib` and `seaborn` for plotting.

---

#### **5. Advanced Visualization: 3D Mesh Chart**
   - Created a 3D mesh chart using `plotly` to visualize the relationship between beverage price, popularity, and calories.
   - **Importance**:
     - Adds interactivity and depth to data exploration.
     - Introduces `plotly`, a powerful library for advanced visualizations.

---

#### **6. Debugging and Troubleshooting**
   - Addressed common errors:
     - `ModuleNotFoundError` for missing libraries (`plotly`, `openpyxl`).
     - `NameError` for undefined variables.
   - Provided fixes:
     - Installed missing libraries using `pip`.
     - Ensured proper imports and initialization of `plotly.offline`.
   - **Importance**:
     - Teaches problem-solving and debugging skills.
     - Highlights the importance of understanding dependencies and environment setup.

---

#### **7. Key Takeaways**
   - **For Beginners**:
     - Learn to load, analyze, and visualize data using Python.
     - Understand the importance of libraries like `pandas`, `matplotlib`, `seaborn`, and `plotly`.
     - Gain confidence in debugging and fixing errors.
   - **For Data Analysis**:
     - Visualizations (histograms, pie charts, 3D charts) are essential for exploring and communicating insights.
     - Different file formats (Excel, CSV) require specific tools and libraries.

---

### **Why This Analysis is Fun and Engaging**
- Uses relatable datasets (beverages and fruits).
- Combines basic and advanced techniques to keep learners challenged.
- Interactive 3D charts add a "wow" factor.
- Step-by-step debugging makes the process approachable for beginners.
