# This script will focus on building a 
# forecasting model for predicting future COVID-19 cases.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def load_data(filepath):
    """Load the processed data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def prepare_data(data):
    """Prepare the features and target variable for the model."""
    data['date'] = pd.to_datetime(data['date'])
    data['date_ordinal'] = data['date'].apply(lambda x: x.toordinal())

    X = data[['date_ordinal']]  # Features
    y = data['total_cases']      # Target variable

    return X, y

def train_model(X, y):
    """Train the linear regression model."""
    model = LinearRegression()
    model.fit(X, y)
    print("Model trained successfully.")
    return model

def forecast(model, future_dates):
    """Forecast future cases based on the trained model."""
    future_dates_ordinal = np.array([pd.to_datetime(date).toordinal() for date in future_dates]).reshape(-1, 1)

    # Predictions should only use the date ordinal
    predictions = model.predict(future_dates_ordinal)
    return predictions

def main():
    processed_data_filepath = r"D:/DataScienceProject/Data/processed_covid19_data.csv"
    data = load_data(processed_data_filepath)
    
    if data is not None:
        X, y = prepare_data(data)
        model = train_model(X, y)

        # Example: Forecasting for the next 7 days
        future_dates = pd.date_range(start=data['date'].max() + pd.Timedelta(days=1), periods=7)  # Next 7 days
        predictions = forecast(model, future_dates)
        
        for date, prediction in zip(future_dates, predictions):
            print(f"Predicted new cases for {date.date()}: {prediction:.2f}")

if __name__ == "__main__":
    main()
