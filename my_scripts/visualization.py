# This script will include functions 
# for visualizing the COVID-19 data using Matplotlib and Seaborn.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load the processed COVID-19 data."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_total_cases(data):
    """Plot total cases over time."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='date', y='total_cases', marker='o')
    plt.title('Total COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_new_cases(data):
    """Plot new cases over time."""
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x='date', y='new_cases', color='orange')
    plt.title('New COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('New Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    processed_data_filepath = r"D:/DataScienceProject/Data/processed_covid19_data.csv"
    data = load_data(processed_data_filepath)
    
    if data is not None:
        plot_total_cases(data)
        plot_new_cases(data)

if __name__ == '__main__':
    main()
