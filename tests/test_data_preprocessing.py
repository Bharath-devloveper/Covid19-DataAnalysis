import sys
import os
import pandas as pd

# Add the my_scripts directory to sys.path
script_dir = os.path.dirname(__file__)  # Get the directory where this script is located
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))  # Go one level up
my_scripts_path = os.path.join(parent_dir, 'my_scripts')  # Path to 'my_scripts' directory

# Add 'my_scripts' to the system path
sys.path.append(my_scripts_path)

# Now you can import the functions directly from data_preprocessing.py
from data_preprocessing import load_data, clean_data  # Absolute import

def test_load_data():
    data = load_data("D:/DataScienceProject/Data/covid19_global_data.csv")
    assert data is not None, "Data should be loaded successfully."

def test_clean_data():
    data = load_data("D:/DataScienceProject/Data/covid19_global_data.csv")
    cleaned_data = clean_data(data)
    assert cleaned_data.isnull().sum().sum() == 0, "Cleaned data should not have missing values."

if __name__ == "__main__":
    test_load_data()
    test_clean_data()
    print("All tests passed!")
