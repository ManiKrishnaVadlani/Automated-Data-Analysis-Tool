import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)
    
    # Handle missing values
    data.fillna(data.mean(numeric_only=True), inplace=True)
    
    # Remove duplicates
    data.drop_duplicates(inplace=True)
    
    # Generate summary statistics
    summary = data.describe()
    print("Summary Statistics:\n", summary)
    return data, summary
def analyze_data(data):
    # Calculate total sales, average sales per month, etc.
    data['Total_Sales'] = data['Quantity'] * data['Price']
    monthly_sales = data.groupby('Month')['Total_Sales'].sum()
    
    print("Monthly Sales:\n", monthly_sales)
    return monthly_sales
import matplotlib.pyplot as plt

def visualize_data(monthly_sales):
    # Create bar plot for monthly sales
    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title('Monthly Sales Analysis')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    # File path to the dataset
    file_path = "sales_data.csv"  # Replace with your dataset
    
    # Step 1: Load and clean data
    data, summary = load_and_clean_data(file_path)
    
    # Step 2: Analyze data
    monthly_sales = analyze_data(data)
    
    # Step 3: Visualize results
    visualize_data(monthly_sales)
