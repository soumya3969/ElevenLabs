# Task 5: Sales Data Analysis with Pandas

## 📋 Overview
A comprehensive data analysis project using Pandas to analyze sales data from CSV files. This project demonstrates data loading, exploration, statistical analysis, and visualization techniques using Python's data science ecosystem.

## ✨ Features Implemented

### Core Functionality
- ✅ **CSV Data Loading** - Load and parse sales data using Pandas
- ✅ **Data Exploration** - Inspect data structure and statistics
- ✅ **Data Preprocessing** - Clean and prepare data for analysis
- ✅ **GroupBy Analysis** - Aggregate data by multiple dimensions
- ✅ **Statistical Analysis** - Calculate sums, means, counts, and percentages
- ✅ **Data Visualization** - Create charts and graphs with Matplotlib/Seaborn
- ✅ **Insights Generation** - Extract actionable business insights

### Analysis Dimensions
- 📊 **Product Performance** - Revenue, quantities, and transaction counts by product
- 🌍 **Regional Analysis** - Sales distribution across different regions
- 📅 **Time-Based Trends** - Monthly sales patterns and growth
- 📦 **Category Comparison** - Electronics vs Accessories performance
- 🔥 **Heatmap Analysis** - Product-Region performance matrix

## 🛠️ Technologies Used
- **Python**: 3.12
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization (charts and graphs)
- **Seaborn**: Statistical data visualization
- **Jupyter Notebook**: Interactive development environment

## 📁 Project Structure
```
Task 5/
├── sales_analysis.ipynb    # Main Jupyter notebook with complete analysis
├── sales_data.csv          # Generated sample sales data (created by notebook)
├── requirements.txt        # Python dependencies
├── requirement.md          # Task requirements
└── README.md              # This file
```

## 🚀 How to Run

### Prerequisites
Make sure you have Python 3.12+ and Jupyter Notebook installed.

### 1. Install Dependencies
```bash
cd "/workspaces/ElevenLabs/Task 5"
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install pandas numpy matplotlib seaborn
```

### 2. Open the Notebook
In VS Code:
- Open `sales_analysis.ipynb`
- VS Code will automatically open it in the notebook interface
- Select the Python kernel when prompted

Or use Jupyter:
```bash
jupyter notebook sales_analysis.ipynb
```

### 3. Run the Analysis
- Click "Run All" to execute all cells
- Or run cells individually to follow along step-by-step
- Visualizations will appear inline in the notebook

## 💡 Notebook Contents

### Section 1: Import Required Libraries
- Import Pandas, NumPy, Matplotlib, Seaborn
- Configure visualization settings
- Set display options

### Section 2: Generate Sample Sales Data
- Create realistic sample dataset with 1000 records
- 8 products across 2 categories
- 5 regions
- 6 months of data (Jan-Jun 2025)
- Save to CSV file

### Section 3: Load and Explore Data
- Load CSV using `pd.read_csv()`
- Display first records with `.head()`
- Check data types with `.info()`
- Statistical summary with `.describe()`
- Missing values check

### Section 4: Data Preprocessing
- Extract date components (month, year, day of week)
- Create calculated fields
- Prepare data for analysis

### Section 5: Sales Analysis with GroupBy
#### 5.1 Sales by Product
- Total revenue, average revenue, transaction count
- Total quantity sold, average price

#### 5.2 Sales by Region
- Regional revenue distribution
- Revenue percentages
- Transaction counts

#### 5.3 Monthly Sales Trends
- Monthly revenue progression
- Seasonal patterns
- Growth analysis

#### 5.4 Category Performance
- Electronics vs Accessories comparison
- Market share analysis

### Section 6: Data Visualization

#### 6.1 Top 5 Products by Revenue (Bar Chart)
- Visual comparison of best-selling products
- Revenue labels on bars

#### 6.2 Monthly Revenue Trend (Line Chart)
- Time series visualization
- Growth tracking over 6 months

#### 6.3 Regional Sales Distribution (Pie Chart)
- Market share by region
- Percentage breakdown

#### 6.4 Category Revenue Comparison (Horizontal Bar Chart)
- Clear comparison between categories
- Revenue values displayed

#### 6.5 Sales Heatmap by Region and Product
- Advanced cross-dimensional analysis
- Identify best product-region combinations
- Color-coded performance matrix

### Section 7: Key Insights and Conclusions
- Overall performance metrics
- Top performers identification
- Key findings summary
- Actionable recommendations

### Section 8: Summary
- Complete overview of accomplishments
- Skills demonstrated
- Next steps for improvement

## 📊 Sample Insights Generated

The analysis provides insights such as:
- **Total Revenue**: Overall sales performance
- **Top Products**: Highest revenue generators (e.g., Laptop, Monitor)
- **Best Region**: Leading geographical market
- **Sales Trends**: Month-over-month growth patterns
- **Category Mix**: Electronics vs Accessories split
- **Best Combinations**: Optimal product-region pairs

## 🎯 Learning Outcomes

Through this project, you'll learn:
- ✅ Loading data from CSV files with Pandas
- ✅ Data exploration techniques (head, info, describe)
- ✅ Using `groupby()` for data aggregation
- ✅ Applying aggregate functions (sum, mean, count)
- ✅ Creating pivot tables for multi-dimensional analysis
- ✅ Data visualization with Matplotlib and Seaborn
- ✅ Creating bar charts, line charts, pie charts, and heatmaps
- ✅ Extracting business insights from data
- ✅ Working with dates and time series data
- ✅ Professional data presentation

## 📈 Visualization Examples

The notebook includes:
1. **Bar Chart** - Top 5 products comparison
2. **Line Chart** - Monthly revenue trends
3. **Pie Chart** - Regional distribution
4. **Horizontal Bar Chart** - Category comparison
5. **Heatmap** - Product-Region performance matrix

All visualizations include:
- Clear titles and labels
- Custom colors and styling
- Data value annotations
- Grid lines for readability
- Professional formatting

## 🔧 Key Pandas Operations Used

### Data Loading
```python
df = pd.read_csv('sales_data.csv', parse_dates=['Date'])
```

### GroupBy Aggregation
```python
df.groupby('Product').agg({
    'Revenue': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
})
```

### Pivot Table
```python
df.pivot_table(values='Revenue', index='Product', columns='Region', aggfunc='sum')
```

### Time Series Operations
```python
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.strftime('%B')
```

## 📊 Data Schema

### Sales Data Columns
| Column | Type | Description |
|--------|------|-------------|
| Date | datetime | Transaction date |
| Product | string | Product name |
| Category | string | Product category (Electronics/Accessories) |
| Region | string | Sales region (North/South/East/West/Central) |
| Quantity | integer | Units sold |
| Unit_Price | float | Price per unit ($) |
| Revenue | float | Total revenue ($) |

## 🔮 Future Enhancements (Optional)

Potential additions to extend the project:
- Customer segmentation analysis
- Predictive sales forecasting
- Seasonal decomposition
- Correlation analysis
- Interactive dashboards with Plotly
- Automated report generation
- Real-time data integration
- Advanced statistical tests
- Machine learning models
- Export to PowerPoint/PDF reports

## 📝 Requirements

### Python Packages
```
pandas         # Data manipulation
numpy          # Numerical operations
matplotlib     # Visualization
seaborn        # Statistical plots
```

All packages are specified in `requirements.txt`

## 🎓 Pandas Techniques Demonstrated

1. **Data Loading**: `pd.read_csv()`, `parse_dates`
2. **Exploration**: `.head()`, `.info()`, `.describe()`, `.shape`
3. **Selection**: Column selection, filtering, indexing
4. **Aggregation**: `groupby()`, `.agg()`, `sum()`, `mean()`, `count()`
5. **Transformation**: Date extraction, calculated columns
6. **Pivot Tables**: Multi-dimensional aggregation
7. **Sorting**: `.sort_values()`, ascending/descending
8. **Missing Data**: `.isnull()`, `.sum()`

## 💡 Tips for Running

1. **Run Sequentially**: Execute cells in order from top to bottom
2. **Data Generation**: The first cells generate sample data - run these first
3. **Visualizations**: Charts will display inline in VS Code
4. **Customization**: Feel free to modify parameters and explore different analyses
5. **Save Work**: Notebook auto-saves, but manually save after major changes

## 🐛 Troubleshooting

### Import Errors
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Kernel Not Found
**Solution**: Select Python kernel in VS Code
- Click "Select Kernel" in top-right
- Choose Python 3.12 (or your Python version)

### Plots Not Showing
**Solution**: Ensure matplotlib backend is set correctly
```python
%matplotlib inline  # Add this to first cell if needed
```

### CSV File Not Found
**Solution**: Run Section 2 first to generate the CSV file

## 👨‍💻 Author

Developed as part of the ElevenLabs coding assessment - Task 5

## 📄 License

This project is created for educational purposes.

---

## 🎉 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Open notebook in VS Code
code sales_analysis.ipynb

# Or start Jupyter
jupyter notebook sales_analysis.ipynb
```

**Happy Analyzing! 📊**
