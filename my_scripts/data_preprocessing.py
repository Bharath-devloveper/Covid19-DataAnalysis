# This script will include functions 
# to load the raw COVID-19 data, clean
#  it, and prepare it for analysis.
import pandas as pd
import os

def create_data_directory():
    """Create data directory if it doesn't exist."""
    os.makedirs('D:/DataScienceProject/Data', exist_ok=True)

def load_data(filepath):
    """Load the COVID-19 data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Clean the COVID-19 data (handle missing values, correct data types)."""
    df.fillna(0, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

def aggregate_country_data(df):
    """Aggregate data on a country level."""
    country_data = df.groupby('country').agg(
        total_cases=('total_cases', 'sum'),
        new_cases=('new_cases', 'sum'),
        active_cases=('active_cases', 'sum'),
        total_deaths=('total_deaths', 'sum'),
        new_deaths=('new_deaths', 'sum')
    ).reset_index()
    return country_data

def save_processed_data(df, output_filepath):
    """Save the processed data to a CSV file."""
    df.to_csv(output_filepath, index=False)
    print(f"Processed data saved to {output_filepath}")

def main():
    create_data_directory()  # Ensure the data directory exists

    # Define file paths
    raw_data_filepath = r"D:/DataScienceProject/Data/covid19_global_data.csv"  # Raw COVID-19 dataset
    processed_data_filepath = r"D:/DataScienceProject/Data/processed_covid19_data.csv"  # Cleaned dataset
    country_data_filepath = r"D:/DataScienceProject/Data/country_wise_data.csv"  # Aggregated country data

    # Load the raw data
    df = load_data(raw_data_filepath)
    
    if df is not None:
        # Clean the data
        cleaned_data = clean_data(df)
        
        # Save the processed cleaned data
        save_processed_data(cleaned_data, processed_data_filepath)
        
        # Aggregate data by country
        country_data = aggregate_country_data(cleaned_data)
        
        # Save the country-wise data
        save_processed_data(country_data, country_data_filepath)

if __name__ == '__main__':
    main()
