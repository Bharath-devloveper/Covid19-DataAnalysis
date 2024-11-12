import sys
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Add the my_scripts directory to sys.path
script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
my_scripts_path = os.path.join(parent_dir, 'my_scripts')

sys.path.append(my_scripts_path)

from forecasting_model import train_model, forecast  # Absolute import

def test_train_model():
    # Load the data
    df = pd.read_csv("D:/DataScienceProject/Data/covid19_global_data.csv")
    
    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    
    # Create features and target variable
    X = df[['new_cases']].copy()
    y = df['total_cases'].copy()

    # Check for missing values
    print("Checking for missing values before filling...")
    print("X NaNs:", X.isnull().sum().sum())
    print("y NaNs:", y.isnull().sum())

    # Display rows with NaN in X
    print("Rows in X with NaN values:\n", X[X.isnull().any(axis=1)])

    # Imputation: Replace NaN values with mean
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    # Convert imputed array back to DataFrame
    X_imputed = pd.DataFrame(X_imputed, columns=X.columns)

    # Verify there are no NaN values after imputation
    assert not X_imputed.isnull().values.any(), "There are still NaN values in X!"

    # Call train_model with imputed X and y
    model = train_model(X_imputed, y)
    assert model is not None, "Model should be trained successfully."
def test_forecast():
    # Load the data
    df = pd.read_csv("D:/DataScienceProject/Data/covid19_global_data.csv")
    
    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    
    # Prepare input features and target for training
    X = df[['new_cases']]
    y = df['total_cases']
    
    # Imputation: Replace NaN values with mean
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    # Convert imputed array back to DataFrame
    X_imputed = pd.DataFrame(X_imputed, columns=X.columns)

    # Train the model first
    model = train_model(X_imputed, y)
    
    # Generate a range of future dates
    future_dates = pd.date_range(start=df['date'].max() + pd.Timedelta(days=1), periods=30, freq='D')
    
    # Forecast for the next 30 days
    forecasted_values = forecast(model, future_dates)  # Adjust as needed
    assert len(forecasted_values) == 30, "Should forecast 30 days of data."

if __name__ == "__main__":
    test_train_model()
    test_forecast()
    print("All tests passed!")